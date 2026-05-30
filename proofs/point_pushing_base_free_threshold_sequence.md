# Point-Pushing Base-Free Threshold Sequence

Date: 2026-05-30

This note records the finite-prefix form of the base-free threshold invariant
from `proofs/point_pushing_base_free_thresholds.md`.

It does not prove outcome A or B.  It makes the current growth problem
auditable as a sequence rather than isolated rectangle checks.

## Definition

For a finite bijective YBE solution `X`, let

```text
epsilon_X(K)
```

be the least symmetric degree `m>=b_X` such that `S_m` detects every
one-new-strand Brunnian extension row through arity `K`, where

```text
s_X=ord(rho_X(A_{1,2})).
```

Equivalently, one may replace the displayed lower bound by the minimal
symmetric base cutoff

```text
b_X = min { m>=1 : s_X divides lcm(1,...,m) }.
```

The helper uses this sharper cutoff.

The finite-prefix sequence is

```text
(epsilon_X(1), epsilon_X(2), ..., epsilon_X(K)).
```

## Monotonicity

The sequence is weakly increasing:

```text
epsilon_X(1) <= epsilon_X(2) <= ... .
```

Indeed, if `S_m` passes every extension gate through arity `K+1`, then it
passes every extension gate through arity `K`.  Therefore the least detector
degree for the shorter prefix cannot be larger than the least detector degree
for the longer prefix.

By symmetric tower monotonicity, once one degree `m` detects a fixed prefix,
every larger degree also detects that prefix.

## Exact Remaining Fork

The Sawin point-pushing fork is:

```text
sup_K epsilon_X(K) < infinity
```

or

```text
epsilon_X(K_j) -> infinity
```

along an infinite subsequence.  The first case gives the rack `A_{S_m}` for a
single fixed `m`.  The second case gives the base-free non-base Brunnian tail
target after choosing first failures and passing to a homogeneous subsequence.

Finite prefixes can suggest either behavior, but they prove neither.

## Audit Hook

The helper

```text
point_pushing_base_free_threshold_prefix_audit(...)
```

computes a bounded approximation to

```text
(epsilon_X(1),...,epsilon_X(K)).
```

It returns `None` for an arity whose threshold is not seen within the supplied
symmetric-degree bound.  The fields

```text
threshold_sequence
detected_arities
unresolved_arities
detected_thresholds_weakly_increase
```

are finite diagnostics.  In particular, a bounded displayed prefix is not an
A proof, and an unresolved displayed prefix is not a B proof.
