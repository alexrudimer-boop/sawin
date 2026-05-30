# Point-Pushing Nonabelian Monolith Tail

Date: 2026-05-30

This note refines the nonabelian branch from
`proofs/point_pushing_monolith_type_split.md`.

It does not prove outcome A or B.  It shows that nonabelian monolithic
product-prefix failures cannot hide an arbitrary extension layer: the
centralizer of the monolith is trivial, so the quotient embeds in the
automorphism group of the simple-product monolith.

## Setup

Let a product-prefix first failure be compressed to a smallest separating
quotient

```text
phi:P_k(X)->H,
M normal H,
m = phi(w(h_1,...,h_k)) in M \ {1},
```

where `H` is finite monolithic and

```text
M ~= S^r
```

for a nonabelian finite simple group `S`.  The conjugation action of `H` on
the `r` simple factors is transitive by
`proofs/point_pushing_monolith_type_split.md`.

## Theorem

The centralizer of the monolith is trivial:

```text
C_H(M)=1.
```

Consequently conjugation embeds `H` into

```text
Aut(M) ~= Aut(S) wr Sym(r).
```

In particular, any infinite nonabelian monolith B tail has an infinite
subsequence of one of the following two forms.

1. **Simple-factor escape.**

   ```text
   |S_j| -> infinity.
   ```

2. **Multiplicity escape.**

   There is a fixed nonabelian finite simple group `S` such that

   ```text
   r_j -> infinity
   ```

   along a subsequence.

## Proof

The centralizer `C_H(M)` is normal in `H`, because `M` is normal.  Also

```text
C_H(M) cap M = Z(M).
```

Since `M=S^r` with `S` nonabelian simple, `Z(M)=1`.  If `C_H(M)` were
nontrivial, then because `H` is monolithic every nontrivial normal subgroup of
`H` contains the unique minimal normal subgroup `M`.  Thus `M <= C_H(M)`,
contradicting `C_H(M) cap M=1`.  Hence `C_H(M)=1`.

Conjugation therefore gives an injective homomorphism

```text
H -> Aut(M).
```

Since `M=S^r`, its automorphism group is the wreath product

```text
Aut(M) ~= Aut(S) wr Sym(r).
```

Now consider an infinite nonabelian monolith failure tail.  Monolithic
compression gives

```text
|H_j| > b(j),
```

and `b(j)->infinity`.  If the monolith orders `|M_j|` were bounded, then only
finitely many finite groups could occur as `M_j`.  For each fixed `M`,
`Aut(M)` is finite, and `H_j` embeds in `Aut(M)`.  Hence the orders `|H_j|`
would be bounded on a subsequence, contradicting `|H_j|>b(j)->infinity`.
Therefore `|M_j|=|S_j|^{r_j}` is unbounded.

If the simple factor orders `|S_j|` are unbounded, we have simple-factor
escape.  Otherwise the simple factor orders are bounded, so only finitely many
nonabelian finite simple groups can occur.  Passing to a subsequence fixes
`S`, and unboundedness of `|S|^{r_j}` forces `r_j->infinity`.  QED.

## Consequence For B

The nonabelian simple-product branch of a negative proof is now exact.  It
must produce either:

```text
unbounded nonabelian simple factor size,
```

or

```text
fixed simple factor with unbounded product multiplicity.
```

There is no separate centralizer-extension tail in the nonabelian case.

The follow-up notes close the cyclic p-power branch and linearize the
abelian-chief branch.  Thus the complementary nonabelian branch can be viewed
as a nonabelian simple-power relation-group quotient tail by
`proofs/point_pushing_nonabelian_chief_relation_quotient.md`, with the two
unbounded parameters above: simple-factor escape or fixed-factor multiplicity
escape.
The sharper normal form in
`proofs/point_pushing_nonabelian_wreath_coordinate_lift.md` identifies the
actual failure as a detector-orbit relation whose lifted value has a
nontrivial coordinate in `S^r` inside a transitive subgroup of
`Aut(S) wr Sym(r)`.
Rule those out together with the abelian relation-module tails and outcome A
follows from the product-prefix criterion; construct one such infinite tail
and outcome B follows after right stabilization.

## Audit Hook

The helper

```text
point_pushing_monolithic_compression_audit(...)
```

now records the finite-row nonabelian monolith data:

```text
nonabelian_centralizer_trivial,
nonabelian_over_monolith_order,
nonabelian_prefix_regime.
```

For a valid nonabelian monolithic row, `nonabelian_centralizer_trivial` should
be true.  The finite prefix regime is one of:

```text
nonabelian_monolith_order_escape,
over_monolith_action_escape,
mixed_nonabelian_parameter_escape,
prefix_covers_nonabelian_quotient,
nonabelian_simple_product,
invalid_nonabelian_monolith_data.
```

The symbolic theorem above converts any infinite valid tail to simple-factor
escape or multiplicity escape.
