# Point-Pushing Action-Quotient Separation

Date: 2026-05-30

This note sharpens the product-prefix B route.  A product-prefix Brunnian
failure cannot merely move the finite point-pushing action image `P_k(X)`.
The moved element must be invisible in every bounded quotient of `P_k(X)`
itself.

This is not outcome A or B.  It gives a sufficient positive criterion:
uniformly bounded element-separating quotients for the groups `P_k(X)` imply
finite-rack domination of `X`.

## Setup

Enumerate finite groups up to isomorphism:

```text
G_1,G_2,G_3,...
```

and set

```text
Pi_j = G_1 x ... x G_j.
```

Let

```text
b(j)=max { B : every finite group of order <= B occurs among G_1,...,G_j }.
```

Since there are only finitely many groups of each bounded order and the
enumeration contains every finite group, `b(j)->infinity`.

For a finite group `P` and `g in P`, define

```text
sep_P(g)=min {|H| : there is a homomorphism phi:P->H with phi(g)!=1}.
```

Equivalently, `sep_P(g)` is the smallest quotient order separating `g` from
the identity.

## Theorem

Let `X` be a finite bijective YBE solution.  Suppose

```text
w in F_k,
w=1 in D_k(Pi_j),
g=w(h_1,...,h_k)!=1 in P_k(X).
```

Then

```text
sep_{P_k(X)}(g) > b(j).
```

Thus the moved action element is invisible in every quotient of `P_k(X)` of
order at most `b(j)`.

## Proof

Assume instead that there is a quotient

```text
phi:P_k(X)->H
```

with `|H|<=b(j)` and `phi(g)!=1`.  Replacing `H` by the image of `phi`, assume
`phi` is surjective.  Let

```text
pi_X:F_k->P_k(X)
```

be the marked action map `x_i |-> h_i`, and put

```text
N=ker(phi pi_X).
```

Then `F_k/N` has order at most `b(j)`.

By `proofs/point_pushing_fixed_arity_cofinality.md`, applied to this
finite-index normal subgroup `N`, there is a finite group

```text
G_N = F_k / Theta_k(N)
```

such that

```text
ker(F_k->D_k(G_N)) <= N.
```

Equivalently, `D_k(G_N)` has `F_k/N` as a marked quotient.  The construction
uses the triangular Nielsen automorphism `Theta_k` coming from the last
recursive Artin longitude, and

```text
|G_N|=|F_k/N|<=b(j).
```

By the definition of `b(j)`, the group `G_N` occurs among the first `j`
product-prefix factors up to isomorphism.  Hence the projection

```text
Pi_j -> G_N
```

is surjective.  Derivative functoriality gives

```text
D_k(Pi_j) -> D_k(G_N).
```

Therefore there is a chain of marked quotients

```text
D_k(Pi_j) -> D_k(G_N) -> F_k/N -> H.
```

Since `w=1` in `D_k(Pi_j)`, its image in `H` must be trivial.  But that image
is

```text
phi(w(h_1,...,h_k))=phi(g),
```

which was assumed nontrivial.  Contradiction.  QED.

## Consequence For B

If a product-prefix Brunnian obstruction tail exists,

```text
w_j=1 in D_{k_j}(Pi_j),
w_j(h_1,...,h_{k_j})!=1 in P_{k_j}(X),
```

then the moved elements have unbounded quotient-separating depth:

```text
sep_{P_{k_j}(X)}(w_j(h_1,...,h_{k_j})) > b(j) -> infinity.
```

So a genuine counterexample cannot be a bounded cyclic, solvable, simple, or
permutation quotient mover.  It must move deeper and deeper into the finite
residual structure of the growing action groups `P_k(X)`.

## Positive Criterion

Suppose there is a constant `B_X` such that, for every `k` and every
nonidentity element `g in P_k(X)`,

```text
sep_{P_k(X)}(g) <= B_X.
```

Choose `J` with `b(J)>=B_X`.  If

```text
D_k(Pi_J) -> P_k(X)
```

failed for some `k`, the marked quotient criterion would give a word `w`
with

```text
w=1 in D_k(Pi_J),
g=w(h_1,...,h_k)!=1 in P_k(X).
```

The theorem would imply

```text
sep_{P_k(X)}(g)>b(J)>=B_X,
```

contradicting the uniform separation bound.  Hence `D_k(Pi_J)->P_k(X)` exists
for every `k`, and the sharp detector rack `A_{Pi_J}` dominates `X`.

Thus:

```text
uniform bounded quotient separation for {P_k(X)}
=> finite-rack domination of X.
```

The remaining A-side target may therefore be stated as a residual-depth
problem for the finite action images `P_k(X)`.

## Audit Hook

The helper

```text
point_pushing_action_quotient_separation_audit(...)
```

computes finite-prefix diagnostics for small action images.  For each arity in
a bounded prefix, it builds `P_k(X)`, enumerates normal subgroups when the
group is below the supplied size cap, and records the largest quotient size
needed to separate any nonidentity element.  This is only a finite diagnostic;
the theorem target is a uniform symbolic bound across all `k`.
