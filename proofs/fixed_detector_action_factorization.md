# Fixed Detector-Action Factorization

Date: 2026-05-28

This note records a stricter but useful form of finite-G detectability.  It
does not prove the Master Local-Minimal Residual Theorem by itself.  It gives
a clean target for any branch where the residual fibre dynamics can be read
from the fixed rack detector action `A_G`.

## Setup

Let `G` be a finite group and let

```text
A_G = T_2 x (G x G)
```

be the sharp Artin-longitude detector rack.  Write

```text
rho_A,n : B_n -> Sym(A_G^n)
```

for its braid action.  The sharp obstruction theorem gives

```text
ker rho_A,n
  =
{ beta in B_n : Lambda_{G,n}(beta)=Lambda_{G,n}(1) }.
```

Now let `pi:X -> Z` be a local interval whose quotient is dominated by the
finite rack `Q`, and set

```text
N_n = ker rho_{Q,n}.
```

For `z in Z^n`, let

```text
delta_{n,z}:N_n -> Sym(X_z)
```

be the residual fibre action.

## Action-Factor Criterion

Suppose that for one fixed finite group `G`, independent of `n`, the following
condition holds for every braid degree `n` and every base tuple `z in Z^n`:

```text
rho_A,n(beta)=rho_A,n(gamma)  with beta,gamma in N_n
        =>  delta_{n,z}(beta)=delta_{n,z}(gamma).
```

Equivalently, the residual representation

```text
delta_{n,z}:N_n -> Sym(X_z)
```

factors through the restricted finite detector image

```text
rho_A,n(N_n) <= Sym(A_G^n).
```

Then `G` satisfies the sharp local kernel implication:

```text
Lambda_{G,n}(beta)=Lambda_{G,n}(1)  =>  delta_{n,z}(beta)=1
```

for every `n`, `z`, and `beta in N_n`.  Therefore `Q x A_G` dominates this
local interval.

## Proof

If `Lambda_{G,n}(beta)=Lambda_{G,n}(1)`, then the sharp detector theorem says
`rho_A,n(beta)=rho_A,n(1)`.  Since `beta` and `1` both lie in `N_n`, the
factorization hypothesis gives

```text
delta_{n,z}(beta)=delta_{n,z}(1)=1.
```

This is exactly the kernel form required by the sharp obstruction theorem.

## Readout Form

The factorization hypothesis often appears in a more concrete form.  It is
enough to give, for every `n`, `z`, and input fibre tuple `x in X_z`, a
detector state

```text
s_{n,z,x} in A_G^n
```

and a readout function on its detector orbit such that

```text
delta_{n,z}(beta)(x)
  =
readout_{n,z,x}( rho_A,n(beta)(s_{n,z,x}) )
```

for every `beta in N_n`.  The detector state and the readout may depend on
the input tuple, but all braid-word dependence must pass through the fixed
rack `A_G`; the finite group itself is not allowed to grow with `n`.

## Fixed-Index Audit Form

The helper

```text
exact_detector_readout_audit(quotient_map,Q,groups,n)
```

materializes the finite version of the readout statement for one braid
degree.  It enumerates the reachable joint image of the base detector, the
listed finite-group longitude detectors, and the total residual action.  If
the audit is nontruncated and `proves_fixed_n_readout` is true, then every
reachable base-kernel detector state has a well-defined residual permutation
readout at that fixed `n`.
The readout rows also check that the residual permutation preserves quotient
fibres and record how many base fibres and total tuples it moves.  Thus the
finite table is aligned with the quotient/residual maps `delta_{n,z}` used in
the sharp obstruction theorem.

This is a convention and certificate tool only.  The Sawin theorem still
requires the readout construction for every `n` from one fixed finite group
`G`, not a growing list of fixed-degree tables.

## Relation To The Verbal-Quotient Criterion

The older criterion in `proofs/finite_longitude_factorization_criterion.md`
asks that the residual action factor through the Artin action on the finite
verbal quotient

```text
W_G(n)=F_n/K_G(n).
```

The present criterion is equivalent at the kernel level but often easier to
audit in finite branches: instead of building a residual action on `W_G(n)`,
one proves that residual motion is a quotient or readout of the already
constructed finite rack action `A_G^n`.  The quotient image
`rho_A,n(B_n)` may vary with `n`; this is harmless because the rack `A_G` and
the group `G` are fixed.

## Use In The Remaining Branches

For the genuinely coloured product branch, this criterion says that closed
normalized holonomy should be readable from the fixed product of the product
label group and the known-branch detector factors acting through `A_G`.

For the bi-free universal-corridor branch, it says that completed-context
Green or Schutzenberger motion must be a readout of the detector action for
the fixed product of the two-sided kernel-block groups, Schutzenberger
groups, and known-branch factors.

The product of detector readouts is legitimate.  By
`proofs/detector_action_products.md`, the active state of
`A_{G_1 x ... x G_r}` projects to the active states of each `A_{G_j}`.  Thus
separate readouts through product-label, normalized holonomy, unit-holonomy,
Green kernel-block, Schutzenberger, quotient, and known-branch detectors can
be assembled into one readout through a single fixed product detector rack.

A proof of either readout statement closes the corresponding branch uniformly
in `n`.  A counterexample must do the opposite: give a normalized-law sequence
whose detector action is eventually identity for every fixed finite `G`, but
whose residual readout remains nontrivial.
