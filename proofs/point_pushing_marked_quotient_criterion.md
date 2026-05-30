# Point-pushing marked quotient criterion

Date: 2026-05-30

This note gives the exact replacement for the superseded fixed-variety
criterion.  Ordinary laws on `G` are too weak to characterize
point-pushing membership in `K_G`, but the full Artin derivative detector
image gives a finite marked quotient criterion.

This does not prove outcome A or B.  It converts the remaining global
point-pushing question into a precise family of finite marked quotient
statements.

## Derivative Detector And YBE Point-Pushing Images

Fix a finite group `G` and `k>=1`.  Put `n=k+1`.  Let

```text
d_i in Sym((G x G)^n)
```

be the active Artin detector action of the pure braid `A_{i,n}`, for
`i=1,...,k`, on arbitrary detector states

```text
((m_1,u_1),...,(m_n,u_n)).
```

Define the finite marked derivative detector image

```text
D_k(G)=<d_1,...,d_k>.
```

For a finite bijective YBE solution `X`, define the finite marked
point-pushing action image

```text
P_k(X)=<h_1,...,h_k> <= Sym(X^n),
```

where

```text
h_i = rho_{X,n}(A_{i,n}).
```

## Lemma: Exact Point-Pushing Kernel Condition

For every `w in F_k`,

```text
iota_{k+1}(w) in K_G(k+1)
```

if and only if

```text
w(d_1,...,d_k)=1 in D_k(G).
```

Proof.  Let `beta=iota_{k+1}(w)`.  The braid `beta` is pure.  If
`w(d_1,...,d_k)=1`, then `beta` fixes every active detector state, hence in
particular every endpoint-identity state

```text
((m_1,1),...,(m_n,1)).
```

The terminal endpoint labels of this sweep are exactly the finite evaluations
of the recursive Artin longitudes.  Thus every finite `G` longitude of `beta`
is trivial, so `beta in K_G(n)`.

Conversely suppose `beta in K_G(n)`.  For every meridian assignment
`phi:F_n->G`, all evaluated longitudes `phi(L_i(beta))` are trivial.  Since
`beta` is pure, the Artin action has the form

```text
beta(x_i)=L_i(beta) x_i L_i(beta)^{-1}.
```

Thus the meridian coordinates in the active detector are fixed.  Starting
from arbitrary endpoint labels `(u_i)`, the same detector-lift induction gives
terminal endpoint labels

```text
phi(L_i(beta)) u_i = u_i.
```

So `beta` fixes every state in `(G x G)^n`.  Therefore
`w(d_1,...,d_k)=1`.  QED.

## Theorem: Marked Quotient Criterion

For a finite group `G` and a finite bijective YBE solution `X`, the following
are equivalent.

1. The detector rack `A_G` dominates `X`:

   ```text
   K_G(n) subset ker rho_{X,n}
   ```

   for every braid index `n`.

2. For every `k>=1`, the marked action image `P_k(X)` is a quotient of the
   marked derivative detector image `D_k(G)`: there is a surjective
   homomorphism

   ```text
   q_k:D_k(G)->P_k(X)
   ```

   satisfying

   ```text
   q_k(d_i)=h_i
   ```

   for every `i=1,...,k`.

Proof.  By `proofs/point_pushing_kernel_layer_criterion.md`, (1) is
equivalent to saying that every last-strand point-pushing layer lying in
`K_G` acts trivially on `X`.

Using the lemma above, this says:

```text
w(d_1,...,d_k)=1  =>  w(h_1,...,h_k)=1
```

for every `k` and every `w in F_k`.

That is exactly the kernel-inclusion condition which makes the assignment

```text
d_i |-> h_i
```

well-defined on the generated group `D_k(G)`.  Its image is all of `P_k(X)`,
because the `h_i` generate `P_k(X)`.  Hence it is a surjective marked
homomorphism.

Conversely, if all the marked quotient maps `q_k` exist, then any word
trivial in `D_k(G)` is trivial in `P_k(X)`.  By the lemma this kills every
point-pushing layer in `K_G`, and the kernel-layer criterion gives
`K_G(n) subset ker rho_{X,n}` for every `n`.  QED.

## Consequence For A

A positive proof may now be phrased without ordinary varieties:

```text
Find one finite group G_X such that, for every k>=1,
P_k(X) is a marked quotient of D_k(G_X).
```

Then the finite rack `A_{G_X}` dominates `X`.

## Consequence For B

A negative proof may be phrased as the failure of every fixed derivative
detector family.  For every product-prefix group `P_j`, find `k_j` such that
the marked quotient

```text
D_{k_j}(P_j) -> P_{k_j}(X)
```

does not exist.  Equivalently, find a word `w_j` such that

```text
w_j(d_1,...,d_{k_j})=1
```

but

```text
w_j(h_1,...,h_{k_j}) != 1.
```

Then `iota_{k_j+1}(w_j)` is a genuine point-pushing `K_{P_j}` mover.  The
right-stabilized sequence is the normalized-law obstruction from
`proofs/point_pushing_product_prefix_obstruction.md`.

The important correction is that `w_j` need not be, and cannot merely be, an
ordinary law on `P_j`.  It must be a relation in the marked Artin derivative
detector image `D_{k_j}(P_j)`.
