# Symmetric derivative quotient fork

Date: 2026-05-30

This note replaces the false last-strand ordinary-law theorem with the exact
symmetric derivative-detector version.  It does not prove outcome A or B, but
it gives the corrected global fork in the same simple symmetric format.

## Statement

Let `X` be a finite nonempty bijective YBE solution.  For `k>=1`, let

```text
P_k(X)=<h_1,...,h_k> <= Sym(X^{k+1})
```

be the marked point-pushing action image of

```text
A_{1,k+1},...,A_{k,k+1}.
```

For a finite group `G`, let

```text
D_k(G)=<d_1^G,...,d_k^G> <= Sym((G x G)^{k+1})
```

be the marked Artin derivative detector image.

Then the following are equivalent.

1. `X` is finitely rack-dominated.

2. There is an integer `m>=1` such that for every `k>=1`, `P_k(X)` is a
   marked quotient of `D_k(S_m)`:

   ```text
   D_k(S_m) -> P_k(X),
   d_i^{S_m} |-> h_i.
   ```

3. There is no symmetric derivative obstruction sequence: there do not exist
   words `w_j in F_{k_j}` with

   ```text
   w_j(d_1^{S_j},...,d_{k_j}^{S_j})=1
   ```

   but

   ```text
   w_j(h_1,...,h_{k_j}) != 1
   ```

   for every `j`, after right stabilization to braid indices tending to
   infinity.

## Proof

By `proofs/normalized_law_domination_dichotomy.md`, finite rack domination is
equivalent to the existence of a finite group `G` such that

```text
K_G(n) subset ker rho_{X,n}
```

for every `n`.

By `proofs/point_pushing_marked_quotient_criterion.md`, this is equivalent to
saying that for every `k`, `P_k(X)` is a marked quotient of `D_k(G)`.

If such a finite group `G` exists, let `m=|G|`.  The left-regular embedding

```text
G -> S_m
```

is injective.  By `proofs/point_pushing_derivative_functoriality.md`, this
embedding gives a marked restriction quotient

```text
D_k(S_m) -> D_k(G)
```

for every `k`.  Composing with the quotients

```text
D_k(G) -> P_k(X)
```

gives the marked quotients in (2).

Conversely, if (2) holds, then
`proofs/point_pushing_marked_quotient_criterion.md` applied to `G=S_m` gives

```text
K_{S_m}(n) subset ker rho_{X,n}
```

for every `n`, so the finite rack `A_{S_m}` dominates `X`.

Thus (1) and (2) are equivalent.

Now suppose (2) fails for every `m`.  In particular, for each `j`, the marked
quotient

```text
D_k(S_j) -> P_k(X)
```

fails for some `k=k_j`.  Failure of the marked quotient means exactly that
the assignment `d_i^{S_j} |-> h_i` is not well-defined.  Hence there is a word
`w_j in F_{k_j}` such that

```text
w_j(d_1^{S_j},...,d_{k_j}^{S_j})=1
```

but

```text
w_j(h_1,...,h_{k_j}) != 1.
```

Let

```text
alpha_j=iota_{k_j+1}(w_j).
```

The first displayed identity says, by the derivative detector criterion, that

```text
alpha_j in K_{S_j}(k_j+1).
```

The second says that `alpha_j` moves `X^{k_j+1}`.

Right-stabilize by adding `j` unused strands:

```text
q_j=k_j+1+j,
beta_j=alpha_j with j trivial right strands.
```

Then `q_j -> infinity`, the moved tuple remains moved after adding fixed
entries, and right stabilization preserves identity finite-longitude data.
For any fixed finite group `G`, let `g=|G|`.  For all `j>=g`,
the left-regular embedding `G->S_g` and the inclusion `S_g->S_j` imply

```text
K_{S_j}(q_j) subset K_G(q_j).
```

Therefore `beta_j` is eventually invisible to every finite group but still
moves `X`.  This is the normalized-law obstruction format.

Conversely, any such obstruction sequence prevents finite rack domination by
the rack-inner-group argument in
`proofs/normalized_law_domination_dichotomy.md`.

Thus the corrected global fork is:

```text
either one S_m supplies all marked derivative quotients D_k(S_m)->P_k(X),
or symmetric derivative relations for S_j produce a normalized-law obstruction.
```

## Why This Replaces The False Law Shortcut

The old failed target used ordinary laws:

```text
w_j in Law(S_j).
```

The corrected target uses derivative relations:

```text
w_j(d_1^{S_j},...,d_k^{S_j})=1.
```

This is strictly the right condition because it is equivalent to

```text
iota_{k+1}(w_j) in K_{S_j}(k+1).
```

So no stationary-strand Artin derivative longitude is being ignored.
