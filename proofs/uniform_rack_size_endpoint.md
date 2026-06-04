# Uniform rack-size endpoint

This note records the exact endpoint isolated by the latest same-chat Pro
query.  It does not solve Sawin's problem, but it removes one false negative
route: no single braid can be visible to a finite YBE solution and invisible
to every finite rack.  Any counterexample must force the required finite rack
detector size to grow without bound.

## Pointwise rack detection

Let `X` be a finite bijective set-theoretic YBE solution.  For a braid
`beta in B_n` with

```text
rho^X_n(beta) != 1,
```

define

```text
d_X(n,beta)
  =
min { |R| : R is a finite rack and rho^R_n(beta) != 1 }.
```

The supremum below is taken over all pairs `(n,beta)` with
`rho^X_n(beta) != 1`; if there are no such pairs, the supremum is `0`.

The minimum is finite.

Proof.  Since `rho^X_n(beta) != 1`, the braid `beta` is nontrivial in `B_n`.
Use the faithful Artin representation

```text
B_n -> Aut(F_n),        F_n=<x_1,...,x_n>,
```

with the convention

```text
sigma_i:
  x_i     -> x_i x_{i+1} x_i^{-1},
  x_{i+1} -> x_i,
  x_j     -> x_j        for j != i,i+1.
```

Then `beta(x_j) != x_j` for some free generator `x_j`.  Since free groups are
residually finite, there is a finite quotient `q:F_n -> G` with

```text
q(beta(x_j)) != q(x_j).
```

Take the finite conjugation rack on `G`,

```text
a*b = a b a^{-1}.
```

Its associated rack braid action is the usual Hurwitz action

```text
sigma_i(g_1,...,g_n)
  =
(g_1,...,g_i g_{i+1} g_i^{-1},g_i,...,g_n).
```

Evaluating this action at the tuple `(q(x_1),...,q(x_n))`, the `j`-th
coordinate after applying `beta` is `q(beta(x_j))`, not `q(x_j)`.  Hence
`rho^R_n(beta) != 1` for this finite rack `R=Conj(G)`.

Thus every individual braid detected by `X` is also detected by some finite
rack.

## Uniform bound equivalence

For fixed `X`, the following are equivalent.

```text
1. X is dominated by a finite rack.
2. sup_{rho^X_n(beta) != 1} d_X(n,beta) < infinity.
```

Proof of `1 => 2`.  If a finite rack `Y` dominates `X`, then

```text
ker rho^Y_n <= ker rho^X_n       for every n.
```

Therefore every `beta` with `rho^X_n(beta) != 1` also satisfies
`rho^Y_n(beta) != 1`, so `d_X(n,beta) <= |Y|`.

Proof of `2 => 1`.  Let

```text
s_X = sup_{rho^X_n(beta) != 1} d_X(n,beta).
```

There are only finitely many racks of size at most `s_X`, up to isomorphism.
Let

```text
Q_X = product_{|R| <= s_X} R
```

be their finite product rack.  If `rho^{Q_X}_n(beta)=1`, then beta acts
trivially on every rack of size at most `s_X`.  If `rho^X_n(beta) != 1`, the
definition of `s_X` supplies such a rack detecting beta, a contradiction.
Thus `rho^X_n(beta)=1` and

```text
ker rho^{Q_X}_n <= ker rho^X_n
```

for every `n`.  Hence `Q_X` dominates `X`.

Consequently Sawin's question is equivalent to the following uniform
rack-size theorem:

```text
For every finite bijective YBE solution X,
sup_{rho^X_n(beta) != 1} d_X(n,beta) < infinity.
```

## Negative sequence equivalence

Failure for one finite `X` is exactly the normalized-law no-rack sequence.
If the supremum is infinite, then for each size bound `s` there are `n` and
`beta in B_n` such that

```text
rho^X_n(beta) != 1,
rho^R_n(beta) = 1      for every finite rack R with |R| <= s.
```

Enumerate finite racks as `R_1,R_2,...`, set

```text
P_m = R_1 x ... x R_m,
s_m = max_{1 <= j <= m} |R_j|.
```

Choosing the above witness for `s=s_m` gives

```text
rho^{P_m}_{n_m}(beta_m)=1,
rho^X_{n_m}(beta_m) != 1.
```

If necessary, stabilize by adding unused strands so that `n_m -> infinity`.
This is precisely the normalized-law no-rack sequence in the product-prefix
tower.

Conversely, any such sequence forces the detector-size supremum for `X` to be
infinite.

## Relation to the executable tower

Let

```text
Q_s = product_{|R| <= s} R.
```

The existing finite audit closes

```text
Gamma_{s,n}(X)
  =
< (rho^{Q_s}_n(sigma_i),rho^X_n(sigma_i)) : 1 <= i < n >
<= Sym(Q_s^n) x Sym(X^n)
```

and extracts

```text
N_{s,n}(X) = { g_X : (1,g_X) in Gamma_{s,n}(X) }.
```

Then

```text
Q_s dominates X
  iff
N_{s,n}(X)=1 for every n.
```

The uniform rack-size theorem is therefore

```text
forall X exists s forall n, N_{s,n}(X)=1.
```

Its negation is

```text
exists X forall s exists n, N_{s,n}(X) != 1.
```

This is the same quantifier fork already recorded in
`rack_residual_obstruction_tower.md`, now with the additional pointwise
conjugation-rack detection theorem.  The unresolved work is not to find one
braid invisible to all finite racks; no such braid can exist.  The unresolved
work is to prove or refute a uniform detector-size bound along all
`X`-visible braids.
