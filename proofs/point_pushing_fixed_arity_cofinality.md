# Point-pushing fixed-arity cofinality

Date: 2026-05-30

This note records the next symbolic consequence of the corrected derivative
detector criterion.  It does not prove outcome A or B.  It proves that no
fixed point-pushing arity can be the obstruction: every finite marked quotient
of `F_k` is seen by some finite derivative detector `D_k(G)`.

Thus the remaining global question is a growth question in `k`.

## Setup

Fix `k>=1` and write

```text
F_k=<x_1,...,x_k>.
```

Let

```text
iota_{k+1}:F_k -> P_{k+1}
```

be the last-strand point-pushing embedding

```text
x_i |-> A_{i,k+1}.
```

For a finite group `G`, let

```text
D_k(G)=<d_1,...,d_k>
```

be the marked Artin derivative detector image of the point-pushing generators
`A_{1,k+1},...,A_{k,k+1}` on `(G x G)^{k+1}`.

Let `Theta_k in Aut(F_k)` be the triangular Nielsen automorphism determined
by the last recursive Artin longitude:

```text
L_{k+1}(iota_{k+1}(w)) = Theta_k(w).
```

This is the surviving correct part of the last-strand law calculation.  In
the repository's longitude convention, each generator is sent to a conjugate
of the corresponding meridian by later meridians, so `Theta_k` is triangular
Nielsen and therefore an automorphism of `F_k`.

## Theorem

For every finite-index normal subgroup

```text
N normal F_k,
```

there exists a finite group `G_N` such that

```text
ker(F_k -> D_k(G_N)) subset N.
```

Equivalently, every finite `k`-marked quotient of `F_k` is a marked quotient
of some derivative detector `D_k(G_N)`.

In symmetric form, there is an integer `m_N` such that

```text
ker(F_k -> D_k(S_{m_N})) subset N.
```

Hence

```text
D_k(S_{m_N}) -> F_k/N
```

is a marked quotient.

## Proof

Let `N normal F_k` have finite index.  Define

```text
N^Theta = Theta_k(N).
```

Since `Theta_k` is an automorphism, `N^Theta` is again finite-index and
normal.  Set

```text
G_N = F_k / N^Theta.
```

This group is finite.  Let

```text
q:F_k -> G_N
```

be the quotient map.

Take any word `w notin N`.  Then

```text
Theta_k(w) notin N^Theta,
```

so

```text
q(Theta_k(w)) != 1.
```

Under the meridian assignment

```text
x_i |-> q(x_i)
```

into `G_N`, the last recursive longitude of the point-pushed braid evaluates
to

```text
q(L_{k+1}(iota_{k+1}(w))) = q(Theta_k(w)) != 1.
```

Therefore

```text
iota_{k+1}(w) notin K_{G_N}(k+1).
```

By `proofs/point_pushing_marked_quotient_criterion.md`, point-pushing
membership in `K_G` is exactly identity in the derivative detector image:

```text
iota_{k+1}(w) in K_G(k+1)
iff
w(d_1,...,d_k)=1 in D_k(G).
```

Thus `w` is nontrivial in `D_k(G_N)`.  Since this holds for every
`w notin N`,

```text
ker(F_k -> D_k(G_N)) subset N.
```

Now embed the finite group `G_N` into a symmetric group by its left-regular
action:

```text
G_N -> S_{|G_N|}.
```

Identity finite-longitude data for `S_{|G_N|}` implies identity
finite-longitude data for `G_N`, hence

```text
ker(F_k -> D_k(S_{|G_N|}))
subset
ker(F_k -> D_k(G_N))
subset
N.
```

Taking `m_N=|G_N|` proves the symmetric form.  QED.

## Corollary 1: Fixed Arity Is Always Detected

Let `X` be any finite bijective YBE solution.  For fixed `k`, let

```text
P_k(X)=<h_1,...,h_k> <= Sym(X^{k+1})
```

be the marked point-pushing image.  Let

```text
psi_X:F_k -> P_k(X)
```

send `x_i` to `h_i`, and put

```text
N_k(X)=ker psi_X.
```

Because `P_k(X)` is finite, `N_k(X)` has finite index.  Applying the theorem
to `N=N_k(X)` gives a finite symmetric group `S_{m_k}` such that

```text
ker(F_k -> D_k(S_{m_k})) subset ker(F_k -> P_k(X)).
```

Equivalently,

```text
D_k(S_{m_k}) -> P_k(X)
```

is a marked quotient.

So for every fixed point-pushing arity `k`, some finite symmetric detector
works.

## Corollary 2: Finite Arity Prefixes Are Detected

Fix `K>=1`.  For each `1<=k<=K`, choose `m_k` as above, and let

```text
M=max(m_1,...,m_K).
```

Symmetric tower monotonicity gives

```text
K_{S_M}(n) subset K_{S_{m_k}}(n)
```

whenever `M>=m_k`.  Restricting to point-pushing layers gives

```text
ker(F_k -> D_k(S_M)) subset ker(F_k -> D_k(S_{m_k})).
```

Therefore

```text
D_k(S_M) -> P_k(X)
```

is a marked quotient for every `1<=k<=K`.

Thus every finite point-pushing arity prefix is harmless.

## Consequence: The Remaining Problem Is A Growth Question

For a finite solution `X`, define

```text
mu_X(k)=min { m : D_k(S_m) -> P_k(X) is a marked quotient }.
```

The theorem proves that `mu_X(k)` is finite for every fixed `k`.

Outcome A is equivalent to the boundedness statement

```text
sup_k mu_X(k) < infinity
```

for every finite bijective YBE solution `X`.  If the supremum is bounded by
`m`, then the sharp detector rack `A_{S_m}` dominates `X` in all braid
degrees by the point-pushing layer criterion.

Outcome B requires genuine unbounded arity escape:

```text
sup_k mu_X(k) = infinity
```

for some explicit finite solution `X`, together with explicit words

```text
w_j in F_{k_j}
```

such that

```text
w_j=1 in D_{k_j}(S_j),
w_j!=1 in P_{k_j}(X).
```

Then `iota_{k_j+1}(w_j)` is a genuine point-pushing `K_{S_j}` mover, and
right stabilization gives the normalized-law obstruction sequence.

This eliminates fixed-arity counterexamples.  Any B construction must make
the required detector degree grow with the point-pushing arity.
