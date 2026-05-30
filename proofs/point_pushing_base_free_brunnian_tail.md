# Point-Pushing Base-Free Brunnian Tail

Date: 2026-05-30

This note combines the base-arity gate with the Brunnian first-failure
stratification.  It removes base failures from the asymptotic symmetric tail
with an explicit cutoff.

It does not prove outcome A or B.  It sharpens the exact remaining fork:
after the cutoff, every first failure must be a one-new-strand Brunnian
extension failure.

## Setup

For a finite bijective YBE solution `X`, set

```text
s_X = ord(rho_{X,2}(A_{1,2})).
```

By `proofs/point_pushing_base_arity_gate.md`, every symmetric detector `S_m`
with

```text
m >= s_X
```

passes the arity-`1` marked quotient gate.

For such an `m`, the Brunnian gate induction from
`proofs/point_pushing_brunnian_gate_induction.md` says that `A_{S_m}`
dominates `X` if and only if every one-new-strand extension row has

```text
failure_kind="none".
```

## Theorem

The following are equivalent:

1. `X` is dominated by a finite rack through the symmetric derivative fork.
2. There exists `m>=s_X` such that every Brunnian extension row for `S_m` has
   `failure_kind="none"`.

If no such `m` exists, then for every `j>=s_X` there is a first failing row for
`S_j`, and that row has one of the three non-base kinds:

```text
stabilizer,
orbit_label,
orbit_relation.
```

After passing to an infinite subsequence, the failure kind is constant and the
first failing arities tend to infinity.

## Proof

The implication from (2) to (1) is exactly the Brunnian gate induction, using
the closed base arity supplied by `m>=s_X`.

Conversely, if a symmetric detector `S_m` dominates `X`, then all marked
quotients `D_k(S_m)->P_k(X)` exist.  In particular, the base gate and every
Brunnian extension gate pass.  Enlarging `m` if necessary to also satisfy
`m>=s_X` preserves detection by symmetric tower monotonicity.  Hence (1)
implies (2) in the symmetric fork.

Now assume no such `m>=s_X` exists.  For every `j>=s_X`, the base arity gate
passes by the base-arity theorem.  Therefore the first failure in the
base-plus-Brunnian gate induction cannot be `base_marked_quotient`; it must be
one of the non-base Brunnian extension statuses unless a finite audit is
truncated.

For the symbolic, nontruncated theorem branch, the mathematical failure kinds
are finite:

```text
stabilizer,
orbit_label,
orbit_relation.
```

Fixed-arity cofinality still implies that first failing arities tend to
infinity: for every finite arity prefix there is a symmetric degree detecting
that entire prefix.  The infinite pigeonhole principle then gives an infinite
subsequence with one constant non-base failure kind.  QED.

## Consequence For B

A negative solution can be searched for only in a base-free tail:

```text
j >= s_X,
failure_kind_j in {stabilizer, orbit_label, orbit_relation},
k_j -> infinity.
```

Each certified row is then converted to a symmetric normalized-law prefix by
`proofs/point_pushing_brunnian_normalized_prefix_bridge.md`.  Right
stabilization gives the normalized-law obstruction sequence once a symbolic
infinite family is supplied.

## Consequence For A

A positive proof no longer has to manage the base gate.  It is enough to prove
that for some fixed

```text
m>=s_X
```

all one-new-strand Brunnian extension rows have status `none`.

## Audit Hook

The helper

```text
point_pushing_base_free_brunnian_tail_prefix(...)
```

computes the base cutoff `s_X`, skips symmetric degrees below that cutoff, and
then records finite prefix rows only for the base-free range.  It exposes:

```text
base_cutoff
checked_degrees
base_failures_after_cutoff
base_cutoff_respected
certified_nonbase_degrees
uncertified_failure_degrees
```

This remains finite-prefix infrastructure.  A final proof must still either
give a uniform all-arity no-tail theorem for one `S_m`, or construct the
infinite certified non-base tail.
