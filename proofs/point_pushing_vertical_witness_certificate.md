# Point-pushing vertical witness certificate

Date: 2026-05-30

This note records the concrete one-row certificate extracted from the paired
graph criterion.  It does not prove outcome B by itself: outcome B still
requires an infinite product-prefix or symmetric-tail family.  The point is to
make each finite row self-contained and checkable.

## Setup

Fix a finite group `G`, a finite bijective YBE solution `X`, and an arity
`k>=1`.  Put `n=k+1`.

As in `proofs/point_pushing_paired_graph_criterion.md`, let

```text
D_k(G)=<d_1,...,d_k>
```

be the Artin derivative detector image of the last-strand point-pushing
generators `A_{1,n},...,A_{k,n}`, and let

```text
P_k(X)=<h_1,...,h_k>
```

be the corresponding YBE point-pushing action image, where

```text
h_i = rho_{X,n}(A_{i,n}).
```

For a free word `w in F_k`, write

```text
alpha = iota_n(w) = w(A_{1,n},...,A_{k,n}) in P_n.
```

## Certificate

A finite vertical witness row consists of:

1. a word `w in F_k`;
2. a verification that

   ```text
   w(d_1,...,d_k)=1 in D_k(G);
   ```

3. a verification that

   ```text
   w(h_1,...,h_k) != 1 in P_k(X);
   ```

4. an explicit tuple `x in X^n` moved by the direct braid action:

   ```text
   rho_{X,n}(alpha)(x) != x;
   ```

5. a check that the evaluated action `w(h_i)` agrees with the direct braid
   action `rho_{X,n}(alpha)`.

Then `alpha` is a genuine detector-kernel mover:

```text
alpha in K_G(n)
```

but

```text
rho_{X,n}(alpha) != 1.
```

## Proof

The first displayed identity says that `w` is trivial in the full Artin
derivative detector image `D_k(G)`.  By
`proofs/point_pushing_marked_quotient_criterion.md`, this is equivalent to
the point-pushed braid `alpha=iota_n(w)` having identity finite-`G`
Artin-longitude data:

```text
alpha in K_G(n).
```

The second and fourth checks say that the same word acts nontrivially on
`X^n`.  The fifth check prevents a convention error: the action obtained by
evaluating `w` on the point-pushing generators `h_i` is exactly the direct
braid action of `alpha`.

Therefore the row is not merely a relation in an auxiliary finite group.  It
is a concrete braid in `K_G(n)` which moves an explicit tuple of `X^n`.  QED.

## Product-Prefix Use

Let

```text
P_j = G_1 x ... x G_j
```

be a product prefix of a fixed enumeration of finite groups.  If, for every
`j`, one supplies a vertical witness certificate for `G=P_j`, with arities
`k_j`, words `w_j`, and moved tuples, then

```text
alpha_j=iota_{k_j+1}(w_j)
```

satisfies

```text
alpha_j in K_{P_j}(k_j+1)
```

and still moves `X`.  Right-stabilizing by `j` unused strands gives braid
indices tending to infinity and eventual invisibility to every finite group,
exactly as in `proofs/point_pushing_product_prefix_obstruction.md`.

Thus a product-prefix family of vertical witness certificates is a complete B
obstruction sequence.

## Symmetric-Tail Use

The same certificate can be used with `G=S_j`.  If one supplies such a row for
every sufficiently large `j`, then the left-regular embedding of any fixed
finite group into a sufficiently large symmetric group gives eventual
finite-group invisibility after right stabilization.  This is the symmetric
tail version recorded in `proofs/symmetric_derivative_quotient_fork.md`.

## Audit Hook

The helper

```text
point_pushing_vertical_witness_certificate(...)
```

checks exactly one finite row:

```text
detector_word_identity
direct_matches_evaluated
moved_tuple -> moved_tuple_image
```

and exposes the combined predicate

```text
valid_vertical_witness.
```

It is intentionally a certificate-shape checker.  It cannot replace the
infinite all-`j` construction required for outcome B, and it cannot prove the
all-`k` vertical-kernel vanishing required for outcome A.
