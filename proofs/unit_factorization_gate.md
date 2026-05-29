# Unit factorization gate

## Purpose

This note strengthens the finite-semigroup holonomy route.  It rules out a
common false obstruction pattern: a residual branch word that contains
reset-like or non-bijective labels but is later treated as if the product could
still be the nontrivial permutation moved by a braid.

## Lemma

Let

```text
f_1,...,f_k : S -> S
```

be total maps of a finite set.  If the composite

```text
f_k ... f_1
```

is a permutation of `S`, then every factor `f_i` is a permutation of `S`.

Proof.  Write `rank(f)=|im(f)|`.  For total endomaps of the same finite set,
composition cannot increase rank, so

```text
rank(f_k ... f_1) <= rank(f_i)
```

for every factor `f_i`: after the prefix through `f_i` the image has at most
`rank(f_i)` points, and applying the remaining suffix cannot increase its
size.  If the full composite is a permutation, its rank is `|S|`; hence every
`rank(f_i)` is also `|S|`.  Each `f_i` is surjective, and therefore bijective
on the finite set `S`.  Equivalently, if any factor loses information, no
later total map can recover it.

Thus, inside a finite transformation monoid, every word representing an actual
residual permutation uses only unit/permutation elements.  Nonunit labels may
appear in a coarse observer, but they cannot be the final residual braid
motion.

## Consequence For A

Suppose a Green/corridor or completed-context proof represents a residual
coordinate motion as a product of labels in a fixed finite transition monoid
`M`.  Since `delta_{n,z}(beta)` is a permutation of the finite fibre block,
any factorization of the moving coordinate through total transformations must
use only labels in the unit group

```text
U(M) = {m in M : m is a permutation}.
```

The A-route can therefore focus on proving membership of these unit labels in

```text
V_beta(U(M)).
```

This is exactly the subgroup checked by
`unit_longitude_subgroup_audit(...)`.

## Consequence For B

A counterexample cannot be certified by showing that a bounded observer has
nonunit or reset-like labels.  A normalized-law obstruction must produce
nontrivial unit/group labels, or group-like corridor holonomy, that survive
while every finite-group Artin-longitude detector is eventually trivial.

## Executable Gate

The helper

```text
unit_factorization_audit(factors)
```

computes the composite of a word of finite transformations and records:

- whether the composite is a permutation;
- which factors are not permutations;
- whether the implication "permutation composite forces unit factors" holds.

The tests verify three cases:

- a product of swaps is a permutation and all factors are units;
- a word containing a reset has non-permutation composite;
- the empty word with explicit degree is the identity permutation.
