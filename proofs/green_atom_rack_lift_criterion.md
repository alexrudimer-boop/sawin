# Green atom-rack lift criterion

Date: 2026-05-29

This note packages the Green branch after the atom quotient has been proved
to be a finite rack layer.  It is a sufficient criterion for the Master
Local-Minimal Residual Theorem in a Green/corridor branch, not a proof that
all local-minimal intervals satisfy the criterion.

## Data

Fix a local interval `pi:X->Z` over a quotient dominated by a finite rack `Q`,
and set

```text
N_n = ker rho_{Q,n}.
```

Suppose a residual Green/corridor branch has:

1. a total descended Green atom quotient `A`, either on the saturated atom
   partition or on the least descent-closed coarsening, with crossing

   ```text
   R_A(A_0,A_1) = (A_1, A_0^A_1),
   ```

   so `A` is a finite right-rack layer;
2. its finite atom inner group

   ```text
   G_A = < right translations A_0 |-> A_0^A_1 > <= Sym(A);
   ```

3. finitely many fixed finite transformation monoids

   ```text
   M_1,...,M_r
   ```

   whose unit groups `U_i=U(M_i)` carry all lower section or endpoint
   holonomy for this branch.

Let

```text
G_branch = G_A x U_1 x ... x U_r.
```

This finite group depends on the interval and quotient-detector branch data,
not on the braid index.

The executable helper

```text
atom_quotient_inner_group(audit)
```

constructs `G_A` from a Green audit whenever
`atom_quotient_rack_audit(audit)` proves the right-rack layer.  In the
size-three affine commutator fixture, the atom quotient has three atoms and
`|G_A|=6`.

The audit

```text
atom_descent_quotient_rack_audit(audit)
```

records the controlled-coarsening variant: if saturated atoms must be
identified before the completed-row action descends, but the closed quotient
is still a total rack layer, the atom detector is the inner group of that
closed rack layer.  Any information below the closed quotient must then be
handled by the endpoint/unit part of the criterion.

## Lift Criterion

Assume that for every braid index `n`, every `beta in N_n`, every relevant
base tuple and fibre tuple, the branch readout decomposes into:

- the atom-rack action of `beta` on an atom tuple in `A^n`; and
- endpoint units

  ```text
  h_i(beta) in U_i
  ```

  for the lower section data, with

  ```text
  (h_1(beta),...,h_r(beta)) in
      V_beta(U_1 x ... x U_r).
  ```

Then identity finite-`G_branch` longitude data kills this branch.

## Proof

By projection from `G_branch` to `G_A`, identity finite-`G_branch` longitude
data gives identity finite-`G_A` longitude data.  Since the atom layer is a
finite rack layer, the standard input-dependent rack longitude factorization
forces the atom tuple to be fixed.

By projection from `G_branch` to `U_1 x ... x U_r`, identity finite
`G_branch` longitude data gives identity finite longitude data in the product
unit group.  The product endpoint criterion in
`proofs/unit_section_product_detector.md` and
`proofs/unit_composite_longitude_criterion.md` then forces the endpoint tuple

```text
(h_1(beta),...,h_r(beta))
```

to be the product identity.

The branch readout is determined by the fixed atom tuple and these endpoint
units.  Therefore the branch readout is identity.  Multiplying this branch
detector with the other fixed detector factors is legitimate by
`proofs/detector_action_products.md`, so the sharp obstruction theorem uses
one finite product group.

## A-Route Target

For the remaining bi-free universal-corridor branch, a proof of A may now be
organized as three symbolic statements:

1. Green atom-action descent and totality hold in every relevant
   local-minimal corridor branch, or the least descent-closed coarsening is
   forced and the lost lower information is routed to endpoint/unit holonomy.
2. The resulting saturated or descent-closed atom quotient is the finite
   right-rack layer described in `proofs/green_atom_quotient_layer.md`.
3. Every lower section or endpoint unit lies in the appropriate
   longitude-value subgroup of one fixed product of unit groups.

Together these statements produce an explicit finite detector group
`G_branch`, independent of `n`, and hence a local rack detector

```text
Q x A_{G_branch}.
```

## B-Route Consequence

A counterexample through the Green/corridor branch must violate one of the
three statements above and then upgrade the violation to the required
normalized-law sequence.  In particular:

- a raw atom quotient is not enough if it is a rack layer;
- a reset-like nonunit section label is not enough because residual braid
  actions are permutations;
- a fixed finite endpoint failure is not enough unless it diagonalizes to
  defeat every finite group.

Thus a genuine B construction must either produce an explicit local-minimal
interval where atom-action descent/totality fails in a way that survives the
sharp obstruction theorem, or produce endpoint units escaping every fixed
finite product detector by normalized laws.
