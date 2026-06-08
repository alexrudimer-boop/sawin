# Theoretical Review: Identity-Extension Completion Lemma

Date: 2026-06-07.

## Verdict

This is useful theorem-level progress inside the positive contextual route.  It
does not prove A by itself, because it assumes two finite identities for the
forced contextual partial translations and still needs all-arity orbit
separation of the contextual readout.  But it removes the vague finite
totalization blocker and replaces it with concrete finite conditions.

## Lemma

Let `P` be the finite two-sided contextual quotient attached to a finite
bijective YBE solution `X`.  For each `p in P`, let

```text
lambda_p : D_p -> P
```

be the forced partial left translation coming from compatible contextual
products.  Define the identity-outside extension

```text
L_p(q) =
  lambda_p(q),  q in D_p,
  q,            q notin D_p.
```

Suppose:

1. **Balanced domain condition.**

```text
lambda_p : D_p -> D_p
```

is a bijection for every `p`.

2. **Conjugacy covariance.**

```text
L_{L_p(q)} = L_p L_q L_p^{-1}
```

for every `p,q in P`.

Then

```text
p*q := L_p(q)
```

defines a finite rack on `P`, extending every forced contextual product.

## Proof Check

The balanced domain condition makes each `L_p` a total permutation of `P`,
because it is a permutation on `D_p` and fixes `P \ D_p`.

Self-distributivity is equivalent to

```text
L_{p*q} L_p = L_p L_q.
```

Since `p*q=L_p(q)`, conjugacy covariance gives

```text
L_{p*q} = L_{L_p(q)} = L_p L_q L_p^{-1}.
```

Multiplying on the right by `L_p` gives the rack identity.  The operation
extends the forced contextual products because `L_p` agrees with `lambda_p` on
`D_p`.

No hidden residual-finiteness or partial-bijection globalization assertion is
used.

## Domination Criterion

If the contextual readout

```text
J_n : X^n -> P^n
```

is braid-equivariant and injective on every `B_n`-orbit for all `n`, then the
rack `P` dominates `X`:

```text
ker rho^P_n <= ker rho^X_n  for every n.
```

Indeed, if `beta` is trivial on `P^n`, then

```text
J_n(rho^X_n(beta)x) = rho^P_n(beta) J_n(x) = J_n(x).
```

The two points are in the same braid orbit, so orbit-injectivity implies
`rho^X_n(beta)x=x` for every `x`.

## Current Positive Target

The positive route is now reduced to three concrete statements for a fixed
finite bijective YBE solution `X`:

```text
lambda_p(D_p)=D_p for every contextual class p;
L_{L_p(q)} = L_p L_q L_p^{-1} for every p,q;
J_n is orbit-injective for every n.
```

The four-point binary skew-over-flip family and the reported six-point linear
skew-over-flip tests pass the first two finite identities.  The first two are
finite checks once `P` is constructed; the third is the remaining all-arity
condition.

## Current Negative Target

A genuine obstruction should now be one of:

1. a finite YBE solution where some forced `lambda_p` is injective but
   `lambda_p(D_p) != D_p`;
2. a finite YBE solution where identity-outside totalization fails
   `L_{L_p(q)} = L_p L_q L_p^{-1}`;
3. a finite YBE solution passing both finite identities but whose contextual
   readout fails all-arity orbit separation, with the failure converted into an
   actual Brunnian detector-kernel braid witness.
