# Point-Pushing Noncentral Module Tail

Date: 2026-05-30

This note refines the noncentral elementary-abelian case from
`proofs/point_pushing_abelian_monolith_split.md`.

It does not prove outcome A or B.  It gives the exact parameter split for an
unbounded noncentral irreducible-module tail.

## Setup

Let a product-prefix first failure have been compressed to a smallest
separating quotient

```text
phi:P_k(X)->H,
M normal H,
m = phi(w(h_1,...,h_k)) in M \ {1},
```

where `H` is finite monolithic and

```text
M ~= (C_p)^r
```

is noncentral.  By `proofs/point_pushing_abelian_monolith_split.md`,

```text
[H,M]=M,
A := H/C_H(M) <= GL_r(p)
```

acts faithfully and irreducibly on `M`.

## Parameter Factorization

Because `M <= C_H(M)`, the size of `H` factors as

```text
|H| = |M| * |A| * |C_H(M)/M|
    = p^r * |A| * |C_H(M)/M|.
```

Here:

- `p^r` is the module size;
- `|A|` is the conjugation-action shadow;
- `|C_H(M)/M|` is the centralizer-extension layer over the monolith.

Every product-prefix failure also satisfies

```text
|H| > b(j)
```

by monolithic compression.

## Theorem

Any infinite noncentral elementary-abelian monolith B tail has an infinite
subsequence of one of the following forms.

1. **Module prime escape.**

   ```text
   p_j -> infinity.
   ```

2. **Fixed-prime module-dimension escape.**

   For some fixed prime `p`,

   ```text
   r_j -> infinity.
   ```

3. **Bounded-module centralizer-layer escape.**

   The module parameters `(p,r)` are bounded, hence after passing to a
   subsequence the module `M ~= F_p^r` and the finite irreducible action shadow
   `A <= GL_r(p)` are both bounded, but

   ```text
   |C_H(M)/M| -> infinity.
   ```

## Proof

Consider an infinite noncentral tail with `|H_j|>b(j)` and `b(j)->infinity`.
If the module orders `|M_j|=p_j^{r_j}` are unbounded, then either the primes
`p_j` are unbounded, giving prime escape, or some fixed prime `p` occurs
infinitely often and the dimensions `r_j` must be unbounded.  This gives the
first two cases.

Suppose instead that the module orders are bounded.  Then, after passing to a
subsequence, the pair `(p,r)` is fixed.  There are only finitely many subgroups
of the finite group `GL_r(p)`, so the action shadow orders `|A_j|` are bounded
as well.  Since

```text
|H_j| = p^r * |A_j| * |C_{H_j}(M_j)/M_j|
```

and `|H_j|>b(j)->infinity`, the centralizer-layer orders
`|C_{H_j}(M_j)/M_j|` must be unbounded.  QED.

## Consequence For B

The noncentral irreducible-module branch of a negative proof is not arbitrary.
It must produce one of:

```text
unbounded module primes,
fixed-prime unbounded module dimension,
bounded-module unbounded centralizer layer.
```

The third case is the deepest extension case: the actual irreducible module
and its finite linear action shadow stay bounded, while the quotient grows in
the centralizer over that module.

The follow-up notes close the cyclic p-power branch and further constrain the
remaining module branch.  In
`proofs/point_pushing_bounded_normal_generator_tail.md`, the monolith is shown
to lie in the normal closure of one bounded-order point-pushing generator.  In
`proofs/point_pushing_abelian_chief_relation_module.md`, every abelian-chief
first failure is linearized as a nonzero quotient of the detector orbit
relation module.  Thus the noncentral module branch is now a relation-module
tail with the parameter escapes listed above.

## Audit Hook

The helper

```text
point_pushing_monolithic_compression_audit(...)
```

now records the finite-row noncentral module parameters:

```text
noncentral_module_dimension,
noncentral_centralizer_layer_order,
noncentral_size_product_matches_quotient,
noncentral_parameter_regime.
```

The regime labels are:

```text
module_prime_escape,
module_dimension_escape,
action_shadow_escape,
centralizer_layer_escape,
mixed_parameter_escape,
prefix_covers_noncentral_quotient,
noncentral_irreducible_module,
invalid_noncentral_module_data.
```

For an actual infinite B tail, the theorem converts these finite row regimes
to the three subsequential unbounded cases listed above.
