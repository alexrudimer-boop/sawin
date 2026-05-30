# Unit-continuation abelian quotient audit

Date: 2026-05-30

This note follows `proofs/terminal_gauge_abelianization_barrier.md` and
`proofs/unit_continuation_abelian_kernel_lift.md`.  It does not prove the
unit-continuation longitude theorem.  It records the exact first checkpoint
for the remaining terminal unit endpoint.

## Setup

Let `M` be one fixed finite continuation or endpoint transition monoid, and
let

```text
U = U(M)
```

be its unit group.  A residual branch contributes a finite word of transition
sections whose composite is

```text
S_beta in U.
```

The desired endpoint theorem is

```text
S_beta in V_beta(U).
```

The terminal-gauge abelianization barrier says that a pure Artin permutation
defect display can only see the commutator subgroup `[U,U]`.  Therefore the
first required test is the abelian quotient

```text
q : U -> U_ab = U/[U,U].
```

## Abelian quotient criterion

If

```text
q(S_beta) notin V_beta(U_ab),
```

then the current fixed abelian quotient already detects a missing terminal
unit witness.  This is not by itself outcome B, but it is the correct finite
place where a normalized-law obstruction would have to start.

If

```text
q(S_beta) in V_beta(U_ab),
```

then the abelian part is closed.  A proof may choose a lift of that abelian
witness to `U` and reduce the remaining endpoint to the commutator correction

```text
K_beta = S_beta v_beta^-1 in [U,U].
```

This is exactly the normal quotient-plus-kernel certificate in
`proofs/unit_continuation_abelian_kernel_lift.md`.

## Executable audit

The helper

```text
unit_composite_abelianization_audit(M,n,beta,factors)
```

computes:

- the unit group `U(M)`;
- its commutator subgroup `[U,U]`;
- the finite abelianization `U/[U,U]`;
- the image `q(S_beta)` of the final unit composite;
- the subgroup `V_beta(U_ab)`.

The audit returns:

- whether the supplied branch is actually a permutation/unit branch;
- whether the abelian endpoint lies in the abelian longitude subgroup;
- whether identity abelian longitude data would kill the projection;
- whether the commutator correction is the only remaining endpoint problem
  after the abelian quotient route.

This complements `unit_composite_detection_audit(...)`: the latter checks the
full endpoint directly in `U`, while the new audit isolates the abelian layer
that pure Artin-defect displays cannot handle.

## Consequence for the final target

The honest terminal gauge target is now staged:

1. project every terminal unit endpoint to `U_ab`;
2. prove the projected endpoint by the abelian longitude matrix criterion;
3. lift the abelian witness to `U`;
4. prove the correction in `[U,U]`, possibly by iterating through the derived
   series or by a commutator-level Artin-defect display.

If every fixed terminal unit group is solvable, the derived-series reduction
turns this into finitely many abelian quotient checks.  If a nontrivial
perfect residual survives, the only remaining nonabelian obstruction lives
there.

No finite search or timeout evidence is used in this reduction.  The audit is
only a certificate checker for the finite quotient step supplied by a
symbolic corridor proof.
