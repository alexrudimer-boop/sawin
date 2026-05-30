# Point-Pushing Brunnian Tail Certificate Prefix

Date: 2026-05-30

This note packages the finite prefixes of the symmetric Brunnian first-failure
tail into braid-action certificates.  It is certificate infrastructure for the
B route, not an outcome B proof.

The point of the note is to separate three finite statuses for each symmetric
degree `j`:

```text
S_j detects the checked prefix;
S_j has only a base/truncated failure in the checked prefix;
S_j has a real non-base Brunnian failure with a checked mover certificate.
```

Only the third status is a finite row of a normalized-law obstruction tail.

## Finite Prefix Certificate

Fix a finite bijective YBE solution `X`, a maximum symmetric degree `J`, and a
maximum point-pushing arity `K`.  For each `1<=j<=J`, run the Brunnian gate
induction for `G=S_j` through arity `K`.

If the prefix is detected, record no witness.  If the first failure is

```text
base_marked_quotient
truncated_base
truncated_old_suffix
truncated_relative
```

record it as an uncertified finite failure.  These statuses do not supply the
non-base Brunnian row needed for the current B route.

If the first failure kind is one of

```text
stabilizer
orbit_label
orbit_relation,
```

then attach the finite certificate from
`proofs/point_pushing_brunnian_failure_certificate.md`: a right-based word
`w_j`, deletion-triviality, identity in `D_k(S_j)`, and an explicit moved tuple
of `X^{k+1}`.

Thus every certified non-base row gives

```text
iota_{k+1}(w_j) in K_{S_j}(k+1),
rho_{X,k+1}(iota_{k+1}(w_j)) != 1.
```

## Infinite Tail Consequence

Suppose a symbolic construction supplies such certified non-base rows for an
unbounded sequence of symmetric degrees `j` and arities `k_j`, with
`j->infinity` and `k_j->infinity`.  Then the row certificates assemble into
the normalized-law obstruction sequence exactly as in
`proofs/point_pushing_brunnian_failure_certificate.md`: right-stabilize
`iota_{k_j+1}(w_j)` by adding unused strands.  Membership in `K_{S_j}` is
preserved by stabilization, every fixed finite group embeds into `S_j` for all
large `j`, and the displayed moved tuple persists after filling new
coordinates by a fixed element of `X`.

Therefore a homogeneous infinite family of certified rows is enough for
outcome B.

Conversely, by
`proofs/point_pushing_brunnian_first_failure_stratification.md`, if a negative
solution exists through the symmetric derivative-detector fork, then after
passing to a subsequence its finite first-failure rows are of one fixed
non-base kind.  The finite prefix certificate is exactly the row-level audit
format for that subsequence.

## What This Does Not Prove

This note does not prove that an infinite tail exists.  It also does not prove
that no infinite tail exists.  The remaining A/B fork is unchanged:

```text
prove one fixed S_m passes every Brunnian gate,
or construct an infinite symmetric-tail family of certified non-base rows.
```

## Audit Hook

The helper

```text
point_pushing_brunnian_tail_certificate_prefix(...)
```

runs finite symmetric degrees `S_1,...,S_J`, records the first Brunnian gate
failure through arity `K`, and attaches a
`PointPushingBrunnianFailureCertificate` exactly when the first failure is
`stabilizer`, `orbit_label`, or `orbit_relation`.

The summary fields are:

```text
detected_degrees
certified_nonbase_degrees
uncertified_failure_degrees
certified_failure_kinds
```

They are finite diagnostics.  A complete B proof still requires a symbolic
infinite family of rows, not only a finite prefix.
