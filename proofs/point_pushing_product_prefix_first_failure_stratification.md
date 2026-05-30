# Point-Pushing Product-Prefix First-Failure Stratification

Date: 2026-05-30

This note makes the product-prefix negative route canonical.  It uses the
exact derivative-detector criterion from
`proofs/point_pushing_marked_quotient_criterion.md`, not ordinary group laws.

It does not prove outcome A or B.  It says that any product-prefix failure can
be chosen as a first-failure, one-new-strand Brunnian row, with the failing
arities tending to infinity.

## Setup

Enumerate finite groups up to isomorphism:

```text
G_1,G_2,G_3,...
```

and set

```text
P_j = G_1 x ... x G_j.
```

For a finite bijective YBE solution `X`, let

```text
D_k(G)
```

be the arity-`k` Artin derivative detector image of the point-pushing
generators, and let

```text
P_k(X)
```

be their action image on `X^{k+1}`.

Define

```text
eta_X(k) = min { j>=1 : D_k(P_j) -> P_k(X) exists as a marked quotient }.
```

## Theorem

For every finite `X`:

1. `eta_X(k)` is finite for every fixed `k`;
2. the sequence is monotone:

   ```text
   eta_X(1) <= eta_X(2) <= eta_X(3) <= ...
   ```

3. `X` is finitely rack-dominated if and only if

   ```text
   sup_k eta_X(k) < infinity.
   ```

If `eta_X(k)` is unbounded, then for every sufficiently large `j` there is a
first failing arity

```text
k_j = min { k : D_k(P_j) -> P_k(X) does not exist },
```

with `k_j -> infinity`.  At that arity the failure may be witnessed by a
right-based one-new-strand Brunnian word

```text
w_j in ker(F_{k_j} -> F_{k_j-1})
```

such that

```text
w_j = 1 in D_{k_j}(P_j),
w_j != 1 in P_{k_j}(X).
```

## Proof

First, fix `k`.  By `proofs/point_pushing_fixed_arity_cofinality.md`, every
finite `k`-marked quotient of `F_k` is a quotient of `D_k(G)` for some finite
group `G`.  Applying this to the finite marked group `P_k(X)` gives a finite
group `H_k` with

```text
D_k(H_k) -> P_k(X).
```

Since the enumeration contains every finite group up to isomorphism, choose
`t` with `G_t isomorphic H_k`.  For every `j>=t`, projection

```text
P_j -> G_t
```

is surjective.  By derivative functoriality,

```text
D_k(P_j) -> D_k(G_t) -> P_k(X).
```

Thus `eta_X(k)` is finite.

Second, the working index set

```text
M_X(k) = { j : D_k(P_j) -> P_k(X) exists }
```

is upward closed.  If `j in M_X(k)` and `J>=j`, the projection

```text
P_J -> P_j
```

is surjective, so functoriality gives

```text
D_k(P_J) -> D_k(P_j) -> P_k(X).
```

Hence `M_X(k)` is the upward ray `{j : j>=eta_X(k)}`.

Third, if `j` works at arity `k+1`, then restricting to the old suffix
point-pushing subgroup gives the arity-`k` marked quotient.  Therefore

```text
M_X(k+1) subset M_X(k),
```

and the thresholds satisfy `eta_X(k)<=eta_X(k+1)`.

Fourth, if `sup_k eta_X(k)<=J`, then

```text
D_k(P_J) -> P_k(X)
```

exists for every `k`.  By the marked quotient criterion, the sharp detector
rack `A_{P_J}` dominates `X`.

Conversely, if `X` is finitely rack-dominated, the repaired group-longitude
dichotomy gives one finite detector group `H` with all marked quotients
`D_k(H)->P_k(X)`.  Since some product prefix `P_J` projects onto an isomorphic
copy of `H`, derivative functoriality gives

```text
D_k(P_J) -> D_k(H) -> P_k(X)
```

for every `k`.  Hence `eta_X(k)<=J` for all `k`.

Now assume `eta_X(k)` is unbounded.  For each `j`, define

```text
k_j = min { k : eta_X(k)>j }.
```

Then

```text
eta_X(k_j-1) <= j < eta_X(k_j),
```

so `P_j` detects arity `k_j-1` but not arity `k_j`.  By
`proofs/point_pushing_jump_normalization.md`, the failure can be chosen in the
relative deletion kernel:

```text
w_j in ker(F_{k_j}->F_{k_j-1}),
w_j=1 in D_{k_j}(P_j),
w_j!=1 in P_{k_j}(X).
```

Finally, the first failing arities tend to infinity.  Fix `K`.  Since the
finite set `eta_X(1),...,eta_X(K)` has finite maximum `J_K`, every `j>=J_K`
detects all arities `1,...,K`.  Hence `k_j>K` for all such `j`.  QED.

## Homogeneous Tail Refinement

For all sufficiently large `j`, the first failure is non-base.  The Brunnian
orbit quotient certificate classifies every non-base row as one of

```text
stabilizer,
orbit_label,
orbit_relation.
```

Therefore any infinite product-prefix failure sequence has an infinite
subsequence with one fixed failure kind.  A negative proof can be sought in
exactly one homogeneous tail: stabilizer-centralizer failures, orbit-label
failures, or orbit-relation failures.

## Audit Hook

The helper

```text
point_pushing_product_prefix_first_failure_audit(...)
```

takes a finite list of group factors, forms the prefixes

```text
G_1, G_1 x G_2, ..., G_1 x ... x G_J,
```

and runs the Brunnian gate prefix audit for each product prefix.  It records
the first failing arity and failure kind, and checks that the finite first
failure arities are weakly increasing.  This is a finite diagnostic only; an
outcome B proof still needs an all-`j` family with explicit Brunnian witness
words and moved tuples.
