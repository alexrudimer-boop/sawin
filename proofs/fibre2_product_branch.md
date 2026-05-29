# Fibre-size-two product branch

Date: 2026-05-28

This note records a symbolic reduction for product-permutation intervals whose
fibres all have size `2`.  It is not a new proof of the user-supplied
finite-G measurability of affine `F_2` branches; it identifies this whole
product subcase with that already eliminated branch for arbitrary quotient
colours.

## Coordinate Choice

Let each fibre `A_a` have two points.  Choose a coordinate bijection

```text
h_a : A_a -> F_2.
```

Every fibre bijection `f : A_a -> A_b` is then a translation

```text
h_b f h_a^{-1}(x) = x + epsilon(f),
```

with `epsilon(f) in F_2`.  Thus every product label is represented by one
bit.

For the swapped product normal form

```text
T_{a,b}(x,y) = (L_{a,b}(y), R_{a,b}(x)),
```

the chosen coordinates rewrite the table as

```text
((a,x),(b,y)) ->
((a.b, y + ell_{a,b}), (a*b, x + r_{a,b})).
```

For the direct product normal form

```text
T_{a,b}(x,y) = (L_{a,b}(x), R_{a,b}(y)),
```

the same coordinates rewrite the table as

```text
((a,x),(b,y)) ->
((a.b, x + ell_{a,b}), (a*b, y + r_{a,b})).
```

## Linear Cocycle Equations

Substituting these forms into the coloured YBE turns the product cocycle
equations into linear equations over `F_2`.

In the swapped case:

```text
ell_{a.b,(a*b).c} + ell_{a*b,c}
  = ell_{a,b.c} + ell_{b,c},
r_{a.b,(a*b).c} + ell_{a,b}
  = ell_{a*(b.c),b*c} + r_{b,c},
r_{a*b,c} + r_{a,b}
  = r_{a*(b.c),b*c} + r_{a,b.c}.
```

In the direct case:

```text
ell_{a.b,(a*b).c} + ell_{a,b} = ell_{a,b.c},
r_{a*b,c} = r_{a*(b.c),b*c} + r_{b,c},
r_{a.b,(a*b).c} + ell_{a*b,c} + r_{a,b}
  = ell_{a*(b.c),b*c} + r_{a,b.c} + ell_{b,c}.
```

The full local table is therefore an affine `F_2` extension of the quotient
colour solution.  No finite enumeration is used in this identification; it is
just the fact that the symmetric group on a two-point fibre is `C_2`.

## Braid Action

The formal product-label normal forms specialize to affine translations.
For any braid word and base-colour tuple, each final fibre bit is an initial
bit, possibly after the swapped dependency permutation, plus the mod-`2` sum
of the labels encountered by that strand.

In the sharp-kernel setting, the base colours are fixed.  In the swapped
branch the Artin permutation is also trivial, so the dependency vector is the
identity; in the direct branch the dependency vector is always the identity.
The residual action is therefore a vector translation over `F_2` whose
coordinates are linear combinations of the product cocycle bits along the
base-colour braid paths.

This is exactly the affine `F_2` local residual type already listed among the
eliminated finite-G-measurable branches.  The relevant finite detector can be
taken from that affine branch reduction; in the purely pairwise subcase it is
the cyclic detector `C_2`.

## Semisplit Local-Minimality

For two-point fibres, each fibre has only two partitions: equality and
universal.  Therefore every possible semisplit congruence family is simply a
choice of equality/universal status for each colour.  Product labels are
bijective, so they transport equality to equality and universal to universal.

Local-minimality is consequently the statement that the source-target colour
graph of the product labels has no proper union of colours on which this
equality/universal status can be constant independently of the complement.
This is the same semisplit condition checked by the general
`LocalInterval` admissible-family definition; no one-sided nondegeneracy or
colour-transitivity assumption is being smuggled in.

## Consequence

A product-permutation local-minimal interval with all fibres of size `2`
cannot be the new arbitrary-fibre product obstruction.  After choosing fibre
coordinates it is an affine `F_2` interval, and that branch is already
bookkept as finite-G measurable in the global reduction program.
