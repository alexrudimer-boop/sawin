# Product Coboundary Telescope

Date: 2026-05-28

This note closes the coboundary subcase of the swapped and direct
product-permutation branches at braid-action level.  It is an all-`n`
statement.

## Setup

Let

```text
T_{a,b}: A_a x A_b -> A_{a.b} x A_{a*b}
```

be a product-permutation local interval over quotient colours `Z`.

In the swapped branch,

```text
T_{a,b}(x,y) = (L_{a,b}(y), R_{a,b}(x)).
```

In the direct branch,

```text
T_{a,b}(x,y) = (L_{a,b}(x), R_{a,b}(y)).
```

Assume the product labels are a coboundary: there are gauges

```text
g_a : A_a -> B
```

on each connected component of the colour-label graph such that every label
is gauge transport.

For the swapped branch this means

```text
g_{a.b} L_{a,b} = g_b,
g_{a*b} R_{a,b} = g_a.
```

For the direct branch this means

```text
g_{a.b} L_{a,b} = g_a,
g_{a*b} R_{a,b} = g_b.
```

Equivalently, every one-step label `f:s -> t` is

```text
f = g_t^{-1} g_s.
```

The implementation records such gauges in `ProductCoboundaryAudit`, and the
helper

```text
product_coboundary_transport_map(interval,audit,s,t)
```

returns `g_t^{-1} g_s`.

## Telescope Lemma

Let

```text
f_1 : A_{c_0} -> A_{c_1},
f_2 : A_{c_1} -> A_{c_2},
...
f_k : A_{c_{k-1}} -> A_{c_k}
```

be any composable product-label word in a coboundary branch.  Then

```text
f_k ... f_2 f_1 = g_{c_k}^{-1} g_{c_0}.
```

Proof:

```text
f_k ... f_1
= (g_{c_k}^{-1} g_{c_{k-1}})
  (g_{c_{k-1}}^{-1} g_{c_{k-2}})
  ...
  (g_{c_1}^{-1} g_{c_0})
= g_{c_k}^{-1} g_{c_0}.
```

Thus every product-label word is determined only by its initial and final
colours, not by the braid path.

## Residual Consequence

Fix a braid degree `n`, a base colour tuple

```text
z = (z_1,...,z_n),
```

and a braid `beta`.

The product normal-form helpers give one label word for each final coordinate.
In the direct branch, coordinate `j` always depends on the original coordinate
`j`; in the swapped branch, coordinate `j` depends on coordinate
`dependency[j]`.

By the telescope lemma, the coordinate map is

```text
g_{z'_j}^{-1} g_{z_{dependency[j]}}
```

in the swapped branch, and

```text
g_{z'_j}^{-1} g_{z_j}
```

in the direct branch, where `z' = beta.z` is the final quotient-colour tuple.

Therefore:

- In the direct branch, if `beta` fixes the base tuple `z`, every coordinate
  map is `g_{z_j}^{-1}g_{z_j}=1`.
- In the swapped branch, if `beta` fixes the base tuple and the Artin
  permutation of `beta` is trivial, then `dependency[j]=j` and every
  coordinate map is again `g_{z_j}^{-1}g_{z_j}=1`.

The sharp finite-group longitude hypothesis includes trivial Artin
permutation.  Hence a coboundary swapped product branch has trivial residual
action under the sharp-kernel hypothesis, and a coboundary direct product
branch already has trivial residual action under the base-kernel hypothesis.

No additional detector factor is needed for the coboundary product subcase;
equivalently, its detector factor is the trivial group.  If other branch
conditions are present, the trivial factor can be omitted from the direct
product detector group.

## Code-Level Check

Unit tests verify this telescope identity for nontrivial two-colour swapped
and direct coboundary fixtures.  These tests are not the proof; they guard
the implementation convention:

- formal label-word evaluation equals the original product normal form;
- coboundary transport equals `g_target^{-1}g_source`;
- label-word evaluation agrees with that transport for mixed positive and
  negative braid words.

The proof above is the all-degree reason the coboundary product branch cannot
produce the remaining Sawin obstruction.
