# Point-Pushing Brunnian First-Failure Stratification

Date: 2026-05-30

This note sharpens the B-side of
`proofs/point_pushing_brunnian_gate_induction.md`.  If no fixed symmetric
detector works, then the first failing Brunnian gate for `S_j` can be chosen
with arity tending to infinity and, after passing to a subsequence, with one
stable non-base failure kind.

It does not prove outcome A or B.  It removes another source of ambiguity from
the negative route.

## Setup

For a finite bijective YBE solution `X`, define the symmetric detector-degree
profile as in `proofs/point_pushing_mu_boundedness_dichotomy.md`:

```text
mu_X(k)=min { m : D_k(S_m) -> P_k(X) is a marked quotient }.
```

By fixed-arity cofinality, each `mu_X(k)` is finite.

For each `j`, if `S_j` does not detect every arity, let `k_j` be the least
arity at which the Brunnian gate induction for `S_j` fails.  The first failure
kind is one of:

```text
base_marked_quotient
stabilizer
orbit_label
orbit_relation.
```

The truncation statuses are finite-audit limitations only, not mathematical
failure kinds.

## Theorem

If `X` is not dominated by any finite rack, then there is an infinite sequence
of symmetric degrees `j_r -> infinity` such that:

1. the first failing arities `k_{j_r}` tend to infinity;
2. the failure kind is constant along the sequence; and
3. the constant kind is one of

   ```text
   stabilizer,
   orbit_label,
   orbit_relation.
   ```

Thus a B proof may be sought as one homogeneous infinite tail of
one-new-strand Brunnian failures.

## Proof

If `X` is not finite-rack dominated, then by
`proofs/point_pushing_mu_boundedness_dichotomy.md`,

```text
sup_k mu_X(k)=infinity.
```

Equivalently, no fixed `S_j` detects every arity.  By
`proofs/point_pushing_brunnian_gate_induction.md`, each `S_j` therefore has a
first failing row in the base-plus-Brunnian gate induction.  Let its arity be
`k_j`.

First, `k_j -> infinity`.  Indeed, fix any finite `K`.  Since every
`mu_X(k)` is finite, the finite maximum

```text
M_K=max_{1<=k<=K} mu_X(k)
```

is finite.  For every `j>=M_K`, the detector `S_j` detects all arities
`1,...,K`.  Therefore its first failure, if any, occurs after `K`.

Second, base failures occur only finitely often.  This is the case `K=1`:
for all `j>=mu_X(1)`, the arity-`1` marked quotient holds.

For all sufficiently large `j`, the first failure is therefore a non-base
Brunnian extension failure.  The non-base mathematical failure kinds are
finite:

```text
stabilizer,
orbit_label,
orbit_relation.
```

By the infinite pigeonhole principle, some infinite subsequence has one
constant failure kind.  Since the original `k_j` tend to infinity, the
subsequence arities also tend to infinity.  QED.

## Consequence For B

The negative route no longer needs to mix incompatible witnesses.  A genuine
counterexample may be chosen in one of three homogeneous forms:

1. an infinite stabilizer-centralizer failure tail;
2. an infinite transported orbit-label ambiguity tail;
3. an infinite post-stabilizer orbit-relation failure tail.

Each row supplies a right-based Brunnian word

```text
w_j in F_{k_j}
```

with

```text
w_j=1 in D_{k_j}(S_j),
w_j!=1 in P_{k_j}(X).
```

The corresponding point-pushing braid

```text
beta_j=iota_{k_j+1}(w_j)
```

lies in `K_{S_j}` and moves `X`.  Right stabilization then gives the
normalized-law obstruction sequence because every fixed finite group embeds in
`S_j` for all sufficiently large `j`.

## Consequence For A

The positive route can equivalently prove that no homogeneous infinite tail of
the three non-base failure kinds exists.  Together with fixed-arity cofinality,
that proves the detector-degree profile is bounded and hence gives a finite
rack `A_{S_m}` dominating `X`.

## Audit Hook

The helper

```text
point_pushing_brunnian_tail_prefix_audit(...)
```

checks finite symmetric-degree prefixes.  For each `S_j` in the prefix it runs
the Brunnian gate induction up to a supplied arity bound and records the first
failure kind.  This is diagnostic only; an outcome B proof still needs a
symbolic infinite tail with explicit witness words and moved tuples.
