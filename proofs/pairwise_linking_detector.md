# Pairwise-Linking Cyclic Detector

This note isolates the all-`n` detector used whenever a local residual branch
has only pairwise-linking dependence.  It is not a finite search result.

## Setup

Fix a local interval `pi:X->Z` and suppose that, after the quotient colour
action is fixed, every residual fibre coordinate map is a product of finitely
many fixed fibre permutations raised to integer linear combinations of the
abelianized Artin longitude matrix

```text
E_i(beta)_j = exponent sum of x_j in L_i(beta).
```

Equivalently, for each colour tuple `z` and output coordinate `r`, there are
finite permutations `p_{r,s,z}` and integers `c_{r,s,z,i,j}` such that

```text
delta_{n,z}(beta)_r =
  product_s p_{r,s,z}^{ sum_{i,j} c_{r,s,z,i,j} E_i(beta)_j }.
```

This is the pairwise-linking case: no coordinate label depends on a nonabelian
word in the longitudes, only on the linking/exponent entries of those
longitudes.  The one-colour swapped product branch and the identity-base
cyclic product branch reduce to this form in
`proofs/one_colour_product_branch.md` and
`proofs/identity_base_product_branch.md`.

## Detector

Let `m` be any common multiple of the orders of all permutations
`p_{r,s,z}` appearing in the branch.  This number depends only on the finite
local interval and the quotient detector data, not on the braid index `n`.
Take

```text
G = C_m.
```

By the sharp obstruction convention, `Lambda_{C_m,n}(beta)=Lambda_{C_m,n}(1)`
includes the `T_2` purity factor from `A_G`.  Therefore the Artin permutation
of `beta` is trivial before any pure-braid formula is used.  For pure braids,
evaluation of the recursive longitude `L_i(beta)` in the cyclic group `C_m`
depends exactly on the exponent vector

```text
(E_i(beta)_1, ..., E_i(beta)_n) mod m.
```

Since the longitude identity is required for every assignment in `C_m^n`, it
forces

```text
E_i(beta)_j = 0 mod m  for all i,j.
```

Every integer linear combination of the entries is then zero modulo `m`.
Because each fibre permutation order divides `m`, each factor
`p_{r,s,z}^{...}` is the identity.  Hence

```text
Lambda_{C_m,n}(beta)=Lambda_{C_m,n}(1)
    => Delta_n(beta)=1
```

for every `n`.

Thus the local detector for a pairwise-linking branch is the fixed cyclic
group `C_m`, and the dominating interval rack is `Q x A_{C_m}`.

## Product-Branch Instances

For a one-colour swapped product table

```text
T(x,y) = (L(y), R(x)),
```

the coloured Yang-Baxter equation is exactly `LR=RL`.  For pure braids the
coordinate exponents are:

```text
L exponent on coordinate j = row sum of E_j(beta)
R exponent on coordinate j = column sum of E_*(beta)_j.
```

The helper `one_color_swapped_label_exponent_action(n,beta)` records these
exponents, and `artin_longitude_row_column_sums(n,beta)` computes the same
numbers from the recursive longitudes.  The cyclic detector above kills both
exponents modulo the common order of `L` and `R`.

For identity-base swapped product tables, the reduction in
`proofs/identity_base_product_branch.md` produces central labels `K_a`.  The
nontrivial local-minimal case has a single prime cycle on each fibre, so the
same argument applies with `m=p`.

## Boundary

This detector covers only branches whose residual labels are abelian
linear functions of the longitude matrix.  Genuinely coloured holonomy, where
the residual coordinate map depends on nonabelian longitude words or on a
colour-context groupoid label not reduced to the above matrix, is outside this
note.  Those cases remain assigned to the coboundary/product-label reduction
or to the bi-free universal corridor target.

The semisplit local-minimality audit is orthogonal to this detector: it
decides whether the branch is a genuine local-minimal interval.  Once the
branch has survived that audit, the cyclic detector proof above is uniform in
`n` and uses only the fixed finite permutation orders of the interval.
