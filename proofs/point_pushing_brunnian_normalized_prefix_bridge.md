# Point-Pushing Brunnian Normalized-Prefix Bridge

Date: 2026-05-30

This note connects the finite Brunnian failure certificates to the standard
symmetric normalized-law prefix checker.  It does not prove outcome B; it
shows that each certified non-base Brunnian row has exactly the row shape
needed by the normalized-law diagonal argument after right stabilization.

## Statement

Let `X` be a finite bijective YBE solution.  Fix a symmetric degree `j`, an
arity `k`, and a certified non-base Brunnian failure row for `G=S_j`:

```text
w in F_k,
w=1 in D_k(S_j),
w!=1 in P_k(X),
r_{k-1}(w)=1.
```

Let

```text
beta=iota_{k+1}(w).
```

Then:

```text
beta in K_{S_j}(k+1),
rho_{X,k+1}(beta) != 1.
```

Choose a moved tuple `x in X^{k+1}` and any fill element `x_0 in X`.  Right
stabilize by adding `j` unused strands, so the target braid index is

```text
q=k+1+j.
```

The stabilized row satisfies:

```text
beta in K_{S_j}(q),
rho_{X,q}(beta)(x,x_0,...,x_0) != (x,x_0,...,x_0).
```

Thus every certified Brunnian row is one valid symmetric-tower normalized-law
prefix row.

## Proof

The certificate gives `w=1` in the derivative detector `D_k(S_j)`.  By the
point-pushing derivative-detector criterion, this is equivalent to

```text
iota_{k+1}(w) in K_{S_j}(k+1).
```

The same certificate directly evaluates the point-pushing braid on `X^{k+1}`
and records a moved tuple, so `rho_X(beta)` is nonidentity in braid degree
`k+1`.

Right stabilization by unused strands preserves Artin data: the old recursive
longitudes are unchanged on the original strands, and the added strands have
trivial longitudes.  Therefore membership in `K_{S_j}` persists in degree
`q`.  The braid acts on the original coordinates exactly as before and fixes
the added coordinates, so the moved tuple remains moved after appending
`x_0`.

This is precisely the finite-row condition checked by
`symmetric_normalized_law_prefix_witness_audit(...)`.  QED.

## Infinite Tail Consequence

If a symbolic construction supplies such rows for `j->infinity`, then every
fixed finite group `H` is eventually covered by the left-regular embedding

```text
H -> S_|H| -> S_j.
```

Symmetric tower monotonicity gives

```text
K_{S_j}(q_j) <= K_H(q_j)
```

for all sufficiently large `j`.  Therefore the right-stabilized certified
rows form the normalized-law obstruction sequence required for outcome B.

The missing part is still the symbolic infinite family.  This note only proves
the row-level bridge from Brunnian certificates to the normalized-law prefix
format.

## Audit Hook

The helper

```text
point_pushing_brunnian_normalized_prefix_audit(...)
```

first builds a `PointPushingBrunnianFailureCertificate` for `S_j`.  If that
certificate is valid, it feeds the braid word, moved tuple, fill value, and
right-stabilization count into
`symmetric_normalized_law_prefix_witness_audit(...)`.

The property

```text
proves_one_symmetric_normalized_prefix
```

means exactly that this finite Brunnian row is also one valid row of the
symmetric normalized-law B certificate.
