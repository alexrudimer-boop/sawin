# Point-pushing mu boundedness dichotomy

Date: 2026-05-30

This note packages the fixed-arity cofinality theorem into the exact remaining
global point-pushing fork.  It does not prove outcome A or B.  It states the
last growth problem in a form where boundedness gives the finite rack and
unboundedness gives the normalized-law obstruction sequence.

## Definition

Let `X` be a finite bijective YBE solution.  For `k>=1`, let

```text
P_k(X)=<h_1,...,h_k> <= Sym(X^{k+1})
```

be the marked point-pushing action image of

```text
A_{1,k+1},...,A_{k,k+1}.
```

For `m>=1`, let

```text
D_k(S_m)=<d_1^{(m)},...,d_k^{(m)}>
```

be the marked Artin derivative detector image for the symmetric group `S_m`.

By `proofs/point_pushing_fixed_arity_cofinality.md`, for every fixed `k`
there exists some `m` such that

```text
D_k(S_m) -> P_k(X),
d_i^{(m)} |-> h_i
```

is a marked quotient.  Define

```text
mu_X(k)=min { m>=1 : D_k(S_m) -> P_k(X) is a marked quotient }.
```

Also define the finite-prefix maximum

```text
nu_X(K)=max_{1<=k<=K} mu_X(k).
```

## Theorem

For a finite bijective YBE solution `X`, the following are equivalent.

1. `X` is dominated by a finite rack.

2. The sequence `mu_X(k)` is bounded:

   ```text
   sup_k mu_X(k) < infinity.
   ```

3. The finite-prefix sequence `nu_X(K)` is bounded.

If these conditions fail, then `X` admits a symmetric-tail normalized-law
obstruction sequence.

## Proof

If `sup_k mu_X(k)<=m`, then for every `k` there is a marked quotient

```text
D_k(S_m) -> P_k(X).
```

By `proofs/point_pushing_marked_quotient_criterion.md`, this is equivalent to

```text
K_{S_m}(n) subset ker rho_{X,n}
```

for every braid index `n`.  Therefore the sharp detector rack `A_{S_m}`
dominates `X`.

Conversely, suppose `X` is dominated by a finite rack.  By
`proofs/symmetric_derivative_quotient_fork.md`, there is some symmetric group
`S_m` such that

```text
D_k(S_m) -> P_k(X)
```

for every `k`.  Hence `mu_X(k)<=m` for every `k`, so `mu_X` is bounded.

The equivalence of boundedness of `mu_X(k)` and `nu_X(K)` is immediate from
the definition of `nu_X(K)` as finite-prefix maxima.

Now suppose the sequence is unbounded.  For each `j>=1`, choose `k_j` such
that

```text
mu_X(k_j)>j.
```

Then the marked quotient

```text
D_{k_j}(S_j) -> P_{k_j}(X)
```

does not exist.  By `proofs/point_pushing_paired_graph_criterion.md`, the
paired subgroup

```text
M_{k_j}(S_j,X)=< (d_i^{(j)},h_i) >
```

has a nontrivial vertical element.  Equivalently, there is a word

```text
w_j in F_{k_j}
```

such that

```text
w_j(d_1^{(j)},...,d_{k_j}^{(j)})=1
```

but

```text
w_j(h_1,...,h_{k_j}) != 1.
```

Let

```text
alpha_j=iota_{k_j+1}(w_j).
```

The derivative detector criterion gives

```text
alpha_j in K_{S_j}(k_j+1),
```

while the second displayed identity says `alpha_j` moves `X^{k_j+1}`.  Choose
a moved tuple.

Right-stabilize by adding `j` unused strands:

```text
q_j=k_j+1+j,
beta_j=alpha_j with j trivial right strands.
```

Then `q_j->infinity`, and the moved tuple remains moved after filling the new
coordinates with any fixed element of `X`.

For any fixed finite group `G`, let `g=|G|`.  For all `j>=g`, the left-regular
embedding

```text
G -> S_g -> S_j
```

implies

```text
K_{S_j}(q_j) subset K_G(q_j).
```

Thus `beta_j` is eventually invisible to every finite group but still moves
`X`.  This is the normalized-law obstruction sequence.  QED.

## Exact Remaining Problem

The Sawin problem is now equivalent to the following boundedness statement:

```text
For every finite bijective YBE solution X,
the sequence mu_X(k) is bounded.
```

A positive proof must give a symbolic bound `m(X)` and then use `A_{S_m}`.

A negative proof must give an explicit finite solution `X` and an explicit
unbounded sequence of vertical witnesses, equivalently words

```text
w_j in F_{k_j}
```

with

```text
w_j=1 in D_{k_j}(S_j),
w_j!=1 in P_{k_j}(X).
```

Fixed-arity failures and finite-prefix failures cannot be final evidence,
because `mu_X(k)` is finite for every fixed `k` and `nu_X(K)` is finite for
every fixed `K`.

## Audit Hook

The helper

```text
point_pushing_mu_prefix_audit(...)
```

checks a bounded rectangle

```text
1<=k<=K,
1<=m<=M
```

and records, for each `k`, the first symmetric degree found within the bound
or the first vertical witness found before the bound is exhausted.  It is only
a finite diagnostic.  It cannot prove boundedness of `mu_X(k)` and cannot
replace the infinite tail required for outcome B.
