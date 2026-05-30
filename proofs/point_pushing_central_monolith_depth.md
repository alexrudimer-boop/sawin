# Point-Pushing Central Monolith Depth

Date: 2026-05-30

This note refines the central elementary-abelian case from
`proofs/point_pushing_abelian_monolith_split.md`.

It does not prove outcome A or B.  It separates the central abelian tail into
the part already visible in abelianization and the genuinely deep central
part.

## Setup

Let a product-prefix first failure have been compressed to a smallest
separating quotient

```text
phi:P_k(X)->H
```

with monolith `M`, and suppose

```text
M ~= C_p^r,
M <= Z(H),
m = phi(w(h_1,...,h_k)) in M \ {1}.
```

Here `w=1` in the product-prefix derivative detector but `m` is nontrivial in
the action quotient.

## Theorem

Under these hypotheses exactly one of the following holds.

1. **Cyclic p-power depth.**  The quotient `H` is abelian.  Since `H` is
   finite abelian and monolithic, it is cyclic of prime-power order, say

   ```text
   H ~= C_{p^e}.
   ```

   Its monolith `M` is the unique subgroup of order `p`.  The moved element
   lies in this bottom subgroup.  No proper quotient of `H` separates it.

2. **Central stem depth.**  The monolith lies in the derived subgroup:

   ```text
   M <= [H,H].
   ```

   Hence the obstruction lies in

   ```text
   Z(H) cap [H,H].
   ```

   It is invisible to abelianization and is a genuine stem central-extension
   obstruction.

## Proof

Because `M` is central, the subgroup

```text
M cap [H,H]
```

is normal in `H`.  Since `M` is the unique minimal nontrivial normal subgroup,
either

```text
M cap [H,H] = 1
```

or

```text
M cap [H,H] = M.
```

If `M cap [H,H]=M`, then `M <= [H,H]`, giving the central stem case.

Suppose instead that `M cap [H,H]=1`.  Then the moved value
`m in M\{1}` has nontrivial image in the abelianization

```text
H_ab = H/[H,H].
```

Thus the quotient map `H->H_ab` separates `m`.  But `H` was chosen as a
smallest finite quotient of `P_k(X)` separating the moved action element.  If
`[H,H]` were nontrivial, `H_ab` would be a strictly smaller separating
quotient, a contradiction.  Hence `[H,H]=1`, so `H` is abelian.

It remains to identify finite abelian monolithic groups.  A finite abelian
group has a unique minimal nontrivial subgroup if and only if it is cyclic of
prime-power order.  Indeed, if two primes divide the order, the corresponding
order-prime subgroups give distinct minimal subgroups; if the `p`-primary part
is not cyclic, its subgroup of elements of order dividing `p` has dimension at
least two over `F_p` and again contains multiple minimal subgroups.  Conversely,
`C_{p^e}` has exactly one subgroup of order `p`.

Therefore the abelian case is exactly cyclic p-power depth.  QED.

## Consequence For B

A central elementary-abelian monolith B tail cannot be arbitrary.  After
passing to first failures and smallest separating quotients, it must be one of
two forms:

```text
unbounded cyclic p-power bottom-layer depth,
unbounded central stem-extension depth.
```

The first form is abelian but not killed by any smaller quotient because the
moved element lies in the bottom order-`p` subgroup of a cyclic `p^e` quotient.
The follow-up note `proofs/point_pushing_cyclic_p_power_tail.md` splits this
again into prime escape and p-power depth escape.

The second form is nonabelian but abelianization-invisible because the moved
monolith is contained in `Z(H) cap [H,H]`.

Thus the current global point-pushing obstruction fork is now:

1. cyclic prime escape;
2. cyclic p-power depth escape;
3. stem central depth;
4. noncentral irreducible `F_p` module tails;
5. nonabelian simple-product monolith tails.

Rule out all four uniformly for finite YBE point-pushing action images and
outcome A follows from the product-prefix criterion.  Construct one unbounded
tail of any one type and outcome B follows after right stabilization.

## Audit Hook

The helper

```text
point_pushing_monolithic_compression_audit(...)
```

now records:

```text
quotient_commutator_order,
monolith_in_quotient_commutator,
projected_value_in_quotient_commutator,
central_abelian_depth_regime.
```

For central elementary-abelian monoliths, the regime is:

```text
cyclic_p_power_depth
central_stem
abelianization_visible
```

The last value is a guardrail: under the smallest-separating-quotient
hypothesis it should not survive as a final compressed witness, because
abelianization would provide a smaller separating quotient.
