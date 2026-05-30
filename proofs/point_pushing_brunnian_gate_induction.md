# Point-Pushing Brunnian Gate Induction

Date: 2026-05-30

This note assembles the one-new-strand Brunnian gates into an exact induction
criterion.  It replaces the family of all marked quotient checks

```text
D_k(G) -> P_k(X)
```

by a base arity check plus one relative extension gate at each new arity.

It does not prove outcome A or B.  It gives the exact all-arity criterion that
a positive proof must satisfy for one fixed detector, and the exact first-row
failure format for a negative tail.

## Setup

Fix a finite group `G` and a finite bijective YBE solution `X`.
For each arity `k`, let

```text
R_{G,k}=ker(F_k -> D_k(G)),
N_{X,k}=ker(F_k -> P_k(X)).
```

The marked quotient condition at arity `k` is

```text
R_{G,k} <= N_{X,k}.
```

For `k>=2`, let

```text
Gate_{G,X}(k)
```

denote the one-new-strand Brunnian gate at arity `k`, in the sense of
`proofs/point_pushing_brunnian_orbit_quotient_certificate.md`.  The finite row
passes exactly when

```text
failure_kind(k)="none".
```

## Theorem

For a fixed finite group `G`, the following are equivalent.

1. For every `k>=1`, the marked quotient

   ```text
   D_k(G) -> P_k(X)
   ```

   exists.

2. The base arity marked quotient exists at `k=1`, and for every `k>=2`,

   ```text
   failure_kind(k)="none".
   ```

Consequently, `A_G` dominates `X` if and only if the base arity and all
Brunnian gates pass.

## Proof

By `proofs/point_pushing_marked_quotient_criterion.md`, the marked quotient at
arity `k` exists exactly when

```text
R_{G,k} <= N_{X,k}.
```

Assume first that the marked quotient exists for every `k`.  The base case
`k=1` is immediate.  For `k>=2`, the old suffix arity `k-1` is detected.
If the one-new-strand gate at arity `k` failed, then
`proofs/point_pushing_jump_normalization.md` and
`proofs/point_pushing_brunnian_orbit_criterion.md` would provide a word

```text
w in R_{G,k} cap ker(F_k -> F_{k-1})
```

with

```text
w notin N_{X,k}.
```

That contradicts `R_{G,k} <= N_{X,k}`.  Therefore every gate has
`failure_kind="none"`.

Conversely, assume the base arity is detected and every Brunnian gate passes.
We prove by induction on `k` that

```text
R_{G,k} <= N_{X,k}.
```

The case `k=1` is the base assumption.  Suppose it holds at arity `k-1`.
Let

```text
u in R_{G,k}.
```

Delete the newly added far-left stationary strand:

```text
v=r_{k-1}(u) in F_{k-1}.
```

Deletion compatibility gives

```text
v in R_{G,k-1}.
```

By the induction hypothesis, `v in N_{X,k-1}`.  Its suffix lift `s(v)` acts
trivially at arity `k`.  Therefore

```text
w=u s(v)^{-1}
```

lies in the Brunnian kernel `ker(r_{k-1})`, still has detector value `1`, and
has the same action value as `u`.

Since the arity-`k` Brunnian gate passes, no such Brunnian detector relation
can move `X`.  Thus `w in N_{X,k}`, hence `u in N_{X,k}`.  This proves the
induction step.

Therefore the marked quotients exist for all `k`.  Applying the marked
quotient criterion again, `A_G` dominates `X`.  QED.

## Symmetric Form

For the global Sawin question, it is enough to take `G=S_m`.
Thus outcome A is equivalent to:

```text
for every finite X, there exists m=m(X)
such that base arity 1 passes and every Brunnian gate has failure_kind="none".
```

Outcome B is equivalent to an explicit finite `X` such that for every `j`
there is a first failing row for `S_j`, either:

```text
base_marked_quotient,
stabilizer,
orbit_label,
orbit_relation.
```

The non-base failures come with right-based Brunnian witness words.  The base
failures are ordinary one-generator point-pushing detector-kernel movers.
Right stabilization and the symmetric-tower argument then give the
normalized-law obstruction sequence.

## Audit Hook

The helper

```text
point_pushing_brunnian_gate_prefix_audit(...)
```

checks this induction criterion on a finite prefix.  It stops at the first
failure and records:

- `base_marked_quotient` or `truncated_base` at arity `1`;
- otherwise the first extension `failure_kind`;
- or no failure, meaning the finite prefix is detected.

This is still finite diagnostic evidence only.  A proof of A needs a symbolic
all-arity argument for one fixed `G`; a proof of B needs an infinite symmetric
tail of first failures with witness words.
