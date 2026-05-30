# Unit-continuation perfect-residual audit

Date: 2026-05-30

This note follows `proofs/unit_continuation_derived_series_reduction.md`.
It does not prove the terminal unit-continuation theorem.  It records the
last finite certificate check left after all abelian derived quotient stages
have been handled.

## Setup

Let `M` be a fixed finite endpoint or continuation transition monoid, and let

```text
U = U(M)
```

be its unit group.  Write the derived series

```text
U^(0)=U,
U^(r+1)=[U^(r),U^(r)].
```

Because `U` is finite, this stabilizes at a perfect residual

```text
P = U^(m).
```

After the derived-series lift certificate has supplied all abelian quotient
witnesses, the remaining terminal endpoint is a residual element

```text
S_m in P.
```

The final nonsolvable checkpoint is exactly

```text
S_m in V_beta(P).
```

## Certificate criterion

If a witness proves `S_m in V_beta(P)`, then the derived-series lift assembles
that witness with the lifted abelian quotient witnesses and proves the
original unit endpoint lies in `V_beta(U)`.

If `P=1`, the criterion is vacuous: the final residual endpoint is identity.
This is the solvable unit-group case.

If `P` is nontrivial, the audit does not solve the endpoint theorem.  It
isolates the only remaining nonabelian endpoint target.  Any future positive
proof must supply recursive-longitude witnesses in `P`; any future negative
proof must eventually produce normalized-law motion surviving in this perfect
residual.

## Executable audit

The helper

```text
unit_perfect_residual_longitude_audit(M,n,beta,S_m)
```

computes:

- the unit group `U(M)`;
- the derived subgroup orders;
- the stable perfect residual `P`;
- the subgroup `V_beta(P)`;
- whether the supplied residual endpoint `S_m` lies in that subgroup.

It also flags the finite-detector failure pattern where finite-`P` longitude
data is identity but `S_m` is nonidentity.  As usual, such a bounded failure
is not outcome B by itself; it must be upgraded to a normalized-law sequence
escaping every finite group.

## Relation to the final theorem

The terminal unit branch is now staged as:

1. prove abelian quotient witnesses in each derived quotient
   `U^(r)/U^(r+1)`;
2. use `unit_composite_derived_series_lift_audit(...)` to verify the
   correction chain;
3. prove the final perfect residual endpoint with
   `unit_perfect_residual_longitude_audit(...)` or an explicit witness in
   the same subgroup.

This is a certificate framework only.  The unresolved all-`n` theorem remains:
the symbolic Green/corridor proof must supply these witnesses uniformly for
every local-minimal bi-free universal-corridor interval.
