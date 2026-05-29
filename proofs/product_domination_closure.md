# Product domination closure

Date: 2026-05-28

This note records an all-degree closure property that is useful on both the
A-route and the B-route.  It is not a proof of the Master Local-Minimal
Residual Theorem, but it prevents a false counterexample strategy: taking
Cartesian products of factors that are already dominated.

## Statement

Let `X_1,...,X_r` be finite bijective set-theoretic Yang-Baxter solutions.
Assume each `X_i` is dominated by a finite rack `Y_i`, in the Sawin sense:

```text
ker rho_{Y_i,n} subset ker rho_{X_i,n}
```

for every braid index `n`.

Let

```text
X = X_1 x ... x X_r
```

with product solution

```text
R_X((x_1,...,x_r),(x'_1,...,x'_r))
  =
(
  (pr_1 R_{X_1}(x_1,x'_1), ..., pr_1 R_{X_r}(x_r,x'_r)),
  (pr_2 R_{X_1}(x_1,x'_1), ..., pr_2 R_{X_r}(x_r,x'_r))
).
```

Let `Y = Y_1 x ... x Y_r` with coordinatewise rack operation.  Then `Y` is a
finite rack and dominates `X`:

```text
ker rho_{Y,n} subset ker rho_{X,n}
```

for every `n`.

## Proof

The product of racks is a rack: every left translation is the product of the
left translations in the factors, and self-distributivity is checked
coordinatewise.

For a braid generator `sigma_k`, the product solution crossing acts on the
`k,k+1` coordinates by applying each factor crossing independently.  By
induction on braid-word length, for every braid `beta in B_n`,

```text
rho_{X,n}(beta)
  =
rho_{X_1,n}(beta) x ... x rho_{X_r,n}(beta)
```

as a permutation of `(X_1 x ... x X_r)^n`, after the canonical identification
with `X_1^n x ... x X_r^n`.  The same identity holds for the product rack:

```text
rho_{Y,n}(beta)
  =
rho_{Y_1,n}(beta) x ... x rho_{Y_r,n}(beta).
```

Therefore

```text
ker rho_{Y,n}
  =
intersection_i ker rho_{Y_i,n}.
```

If `beta` lies in this kernel, then `beta in ker rho_{Y_i,n}` for every `i`.
By the domination hypothesis for each factor, `beta in ker rho_{X_i,n}` for
every `i`.  Hence the coordinatewise product action on `X^n` is also the
identity, so `beta in ker rho_{X,n}`.

This proof is uniform in `n`; no finite search and no `n`-dependent rack is
used.

## Consequences

1. A counterexample to finite-rack domination cannot be created merely by
   taking a Cartesian product of already dominated finite solutions.
2. Product closure is stronger than the two-strand direct-symmetric gate in
   `proofs/two_strand_product_gate.md`: it applies to all braid degrees, but
   only when the factors already have domination racks.
3. In an A proof, once branch arguments dominate several independent factor
   solutions, their product is dominated by the product rack without adding a
   new local theorem.

## Executable convention check

The implementation helper `product_solution(X,Y)` is tested against mixed
positive and negative braid words.  The test verifies the only convention
needed by the proof above:

```text
rho_{X x Y,n}(beta)((x_1,y_1),...,(x_n,y_n))
 =
((rho_{X,n}(beta)(x))_1,(rho_{Y,n}(beta)(y))_1), ...
```

The test is not evidence for the theorem by itself; it locks the code
convention to the symbolic coordinatewise proof.
