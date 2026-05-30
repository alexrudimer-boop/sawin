# Unit-continuation derived-series reduction

Date: 2026-05-29

This note follows `proofs/unit_continuation_abelian_kernel_lift.md`.  It does
not prove the unit-continuation longitude theorem.  It iterates the
abelian-kernel split through the derived series of the fixed finite unit group.

## Setup

Let

```text
U = U(M_cont)
```

be the fixed finite unit group in the final constant-observer
universal-continuation case, and let

```text
S_beta in U
```

be the residual unit endpoint.  The remaining goal is still

```text
S_beta in V_beta(U).
```

Define the finite derived series

```text
U^(0)=U,
U^(r+1)=[U^(r),U^(r)].
```

Because `U` is finite, the sequence stabilizes at a perfect residual

```text
P = U^(m).
```

The group `P` may be trivial.  If it is trivial, `U` is solvable.

## Iterated lift criterion

Suppose we construct endpoint corrections

```text
S_0 = S_beta,
S_{r+1} = S_r * v_r^-1
```

with `S_r in U^(r)`, where each `v_r` is a longitude-witness value in
`U^(r)` whose projection to the finite abelian quotient

```text
U^(r) / U^(r+1)
```

equals the projection of `S_r`.

Then each correction satisfies

```text
S_{r+1} in U^(r+1).
```

After finitely many steps,

```text
S_beta = S_m * v_{m-1} * ... * v_0.
```

Therefore:

```text
If every abelian quotient step has a longitude witness and the final
perfect-residual endpoint S_m lies in V_beta(P), then S_beta lies in V_beta(U).
```

Proof.  Apply the normal quotient lift criterion at each stage.  The quotient
`U^(r)->U^(r)/U^(r+1)` is finite abelian, so the quotient endpoint is governed
by the abelian longitude matrix criterion.  The correction after the lifted
witness lands in the kernel `U^(r+1)`.  Multiplying the successive lifted
witnesses with the final residual witness gives a literal word in recursive
longitude values inside `U`.  QED.

## Consequence for solvable unit groups

If the perfect residual is trivial, then the final endpoint `S_m` is identity.
Thus a solvable unit-continuation group is closed once every derived abelian
quotient endpoint has a matrix-longitude witness.

This is a strict simplification of the final unit endpoint theorem in the
solvable case:

```text
S_beta in V_beta(U)
```

is reduced to finitely many abelian matrix checks in the fixed groups

```text
U^(r) / U^(r+1).
```

None of these groups depends on the braid index `n`.

## Remaining obstruction for nonsolvable unit groups

If the perfect residual `P` is nontrivial, the only nonabelian endpoint
obstruction left by this reduction is

```text
S_m in V_beta(P).
```

Thus a future B route in the constant-observer continuation channel must
eventually locate normalized-law movement either:

1. in one finite abelian derived quotient, contradicting the matrix-longitude
   witness target; or
2. in the perfect residual endpoint `P`.

A raw nonunit continuation label, a raw Green defect, or a bounded miss in a
single derived quotient is still not B.

## Executable audit

The finite group helper

```text
derived_series_audit(U)
```

records:

- the orders of the derived-series subgroups;
- the perfect residual;
- whether the series terminates at identity;
- the derived length when it is solvable.

The helper

```text
subgroup_as_group(U,U^(r))
```

turns each derived subgroup into a finite group with restricted
multiplication, so the quotient tools and abelian matrix witness tools can be
applied stage by stage.

These helpers do not prove the all-`n` endpoint theorem.  They identify the
finite quotient stages that any proof must supply with symbolic
recursive-longitude witnesses.

The endpoint certificate checker

```text
unit_composite_derived_series_lift_audit(M,n,beta,factors,
                                         stage_lifted_witnesses,
                                         final_witness)
```

now records the full supplied lift chain for a finite transition monoid
`M`.  At stage `r` it checks:

- the current residual endpoint lies in `U^(r)`;
- the lifted longitude witness uses assignments in `U^(r)`;
- the correction

```text
S_r v_r^-1
```

lies in `U^(r+1)`.

After all derived quotient stages, it checks that the final residual endpoint
in the stable perfect residual is represented by `final_witness`.  It also
evaluates the combined witness

```text
final_witness * v_{m-1} * ... * v_0
```

inside the original unit group and verifies that it equals the terminal unit
composite.

Thus a supplied successful audit is a literal certificate that

```text
S_beta in V_beta(U(M)).
```

For solvable unit groups the perfect residual is trivial, so the final
witness may be empty after all abelian quotient stages pass.  For nonsolvable
groups, the audit isolates the exact perfect-residual witness still needed.

The companion note
`proofs/unit_continuation_perfect_residual_audit.md` packages that last
nonsolvable checkpoint.  The helper
`unit_perfect_residual_longitude_audit(...)` restricts the finite group to
the stable perfect residual `P` and checks the final residual endpoint
against `V_beta(P)`.
