# Point-Pushing Module Prime Characteristic Split

Date: 2026-05-30

This note refines the noncentral irreducible relation-module branch from
`proofs/point_pushing_abelian_relation_action_split.md`.

It does not prove outcome A or B.  It shows that an actual module-prime escape
is forced into cross-characteristic representation theory relative to the
fixed point-pushing generator order bound.

## Setup

Let `X` be a finite bijective YBE solution, and set

```text
B_X = ord(rho_{X,2}(sigma_1^2)).
```

In a noncentral abelian-chief first failure, the monolith is an irreducible
module

```text
M ~= F_p^r
```

for the detector orbit group `N_D`, and the relation lift gives a surjective
module quotient

```text
Rel_D tensor F_p ->> M.
```

By `proofs/point_pushing_bounded_normal_generator_tail.md`, the monolith is
contained in the normal closure of one transported newest point-pushing
generator `t`, with

```text
ord(t) | B_X.
```

## Theorem

Every infinite noncentral module-prime escape tail has, after discarding
finitely many terms,

```text
p_j does not divide B_X.
```

Equivalently, module-prime escape is necessarily cross-characteristic with
respect to the bounded-order normal generator.

## Proof

The integer `B_X` is fixed once `X` is fixed.  Hence it has only finitely many
prime divisors.

In a module-prime escape tail, the module characteristics satisfy

```text
p_j -> infinity.
```

Therefore only finitely many `p_j` can divide the fixed integer `B_X`.
Passing to the cofinal tail gives

```text
p_j not | B_X.
```

For each remaining row, `ord(t_j)|B_X`, so `p_j` also does not divide
`ord(t_j)`.  Thus the newest point-pushing normal generator is a `p_j'`-element
in the quotient acting on the `F_{p_j}`-module `M_j`.

This proves the claim.  QED.

## Consequence For The Fork

The noncentral irreducible module branch now separates into:

1. **bounded-characteristic rows**, where `p|B_X`;
2. **cross-characteristic prime-escape rows**, where `p` is unbounded and
   `p` does not divide `B_X`.

The first class cannot support prime escape, because only finitely many primes
divide `B_X`; it can only contribute to fixed-prime dimension or
centralizer-layer tails.  Therefore any genuine module-prime B tail must be
cross-characteristic.

The remaining positive target for this branch is sharper:

```text
rule out unbounded cross-characteristic irreducible quotients of the detector
orbit relation modules,
and rule out fixed-characteristic dimension/centralizer-layer tails.
```

Constructing either kind explicitly would still give B after the usual
product-prefix right stabilization.

The follow-up note `proofs/point_pushing_active_module_generator_split.md`
splits the noncentral module branch by the image of the bounded newest
generator in the linear action shadow.  If that image is trivial, the row is a
centralizer-layer generator tail.  If it is nontrivial, its conjugate
commutator images generate the irreducible module, and prime escape is
cross-characteristic for this bounded-order linear operator.

## Audit Hook

The helper

```text
point_pushing_module_prime_characteristic_audit(...)
```

records whether a row prime divides the fixed bound `B_X`.  It labels rows as

```text
bounded_prime_divides_generator_bound
cross_characteristic_prime_escape
```

This is finite bookkeeping only; the theorem above supplies the symbolic
tail-level reduction.
