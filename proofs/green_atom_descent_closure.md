# Green atom descent closure

Date: 2026-05-29

This note makes the Green atom-action gap exact.  It does not prove the
Master Local-Minimal Residual Theorem.  It gives the canonical finite
obstruction object that must either be shown trivial in every local-minimal
Green branch, or upgraded to the normalized-law escape required for outcome B.

## Setup

For one regular Green `R`-class audit, write retained edge-germs as

```text
E_C = { (s,x) : s in C, s tau_x in C }.
```

A completed row has the form

```text
a=(s,x),          q=(s tau_x,y),
R(x,y)=(u,v),
q^a=(s,u),        a^q=(s tau_u,v).
```

The atom relation used in `proofs/green_atom_quotient_layer.md` is generated
by

```text
q^a ~ q
```

over all completed rows.  This relation is exactly what forces the first
output of the atom crossing to be the second input atom.  It is not, by
definition alone, the same thing as saying that the second output `a^q`
depends only on the two input atoms.

## Descent Closure

Define the descent closure of the atom partition to be the least coarsening
closed under the two implications below, for all completed rows `r,r'`.

Forward stability:

```text
a_r ~ a_{r'} and q_r ~ q_{r'}
    => a_r^{q_r} ~ a_{r'}^{q_{r'}}.
```

Inverse bookkeeping stability:

```text
a_r^{q_r} ~ a_{r'}^{q_{r'}} and q_r ~ q_{r'}
    => a_r ~ a_{r'}.
```

Because the edge-germ set is finite, repeated application of these
implications stabilizes.  The executable helper

```text
atom_descent_closure_summary(audit)
```

computes this least coarsening and records:

- initial and closed atom counts;
- the closure depth;
- how many related edge-pairs were added;
- whether the closed relation makes the completed-row action well-defined;
- whether any atom pair remains unsupported after closure.

The helper is not a search for the theorem.  For a fixed finite audit it is
the exact finite closure forced by the definition of an atom-level action.

## Exact Sufficient Criterion

For one Green audit, if

```text
atom_descent_closure_summary(audit).proves_stable_atom_action
```

holds, then the original saturated atom partition already gives a total
well-defined atom action.  Therefore `atom_quotient_solution(audit)` is the
finite crossing

```text
R_A(A,Q) = (Q, A triangleright Q),
```

and `atom_quotient_rack_audit(audit)` checks the right-rack laws:

```text
(A triangleright B) triangleright C
  =
(A triangleright C) triangleright (B triangleright C).
```

Thus the atom layer contributes only the finite rack detector built from

```text
G_A = < right translations of A >.
```

## Obstruction Fork

If the descent closure coarsens the atom partition, the failure is no longer
vague.  It is a concrete finite quotienting demand: two edge-germs that were
distinct saturated atoms must be identified before the completed-row action
descends.

For outcome A, the symbolic task is to prove that in every relevant
local-minimal Green/corridor interval this closure is trivial, or that any
nontrivial closure is absorbed by an already handled quotient/refinement
branch and still yields a fixed finite detector group independent of `n`.

For outcome B, a coarsening event by itself is not enough.  It must be
realized inside an explicit finite bijective YBE solution, survive
local-minimality and semisplit checks, and produce a normalized-law sequence
whose finite-group Artin-longitude data is eventually trivial for every
finite group while the original residual action still moves an explicit
tuple.

## Current Audit Result

The regenerated `proofs/green_branch_audit.json` records the descent closure
for each Green audit.  In the current exhaustive scans:

```text
size 2: descent-closure coarsening solutions 0,
        descent-closure failure solutions 0.

size 3: descent-closure coarsening solutions 0,
        descent-closure failure solutions 0.
```

For the dihedral quandle of size `3`, the size-three affine commutator
fixture, and the trivial rack of size `2`, the closure has stable depth `0`,
adds no related pairs, and proves stable total atom action.

Again, this is finite diagnostic evidence only.  The proof obligation is the
symbolic statement that local-minimal Green/corridor intervals cannot force a
new descent closure outside the already controlled branches.
