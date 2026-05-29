# Fixed detector readout audit

Date: 2026-05-28

This note records the executable fixed-index version of the readout form in
`proofs/fixed_detector_action_factorization.md`.  It is not a proof of the
Master Local-Minimal Residual Theorem.  Its purpose is to make the remaining
all-`n` Green/corridor target completely explicit.

## Setup

Let `pi:X -> Z` be a finite quotient map, let `Q` be a finite base detector
for `Z`, and let `G_1,...,G_r` be a finite list of candidate detector groups.
For a fixed braid degree `n`, consider the joint detector state

```text
D_n(beta) =
  ( rho_{Q,n}(beta),
    Lambda_{G_1,n}(beta), ...,
    Lambda_{G_r,n}(beta) ).
```

For braids in the base kernel `ker rho_{Q,n}`, the residual action is the
permutation induced by `rho_{X,n}(beta)` on each fibre over a fixed base
tuple.

## Readout Criterion At Fixed n

For this fixed `n`, the candidate detector has a residual readout exactly
when

```text
D_n(beta)=D_n(gamma),  beta,gamma in ker rho_{Q,n}
    => rho_{X,n}(beta)=rho_{X,n}(gamma).
```

Equivalently, the residual action of the base-kernel subgroup is a function
of the reachable detector state.  In that case one may choose one
representative braid word for each reachable base-kernel detector state and
record the residual permutation of that representative.  This finite table is
the fixed-`n` readout.

The all-`n` theorem needed for Sawin domination is the symbolic version of
this statement: construct these readouts uniformly from one fixed finite
group `G`, independent of `n`, or prove a normalized-law sequence for which
no such fixed finite detector can work.

## Executable Audit

The helper

```text
exact_detector_readout_audit(quotient_map,Q,groups,n)
```

enumerates the exact finite joint image at degree `n` up to a state limit and
returns:

- the number of reachable joint states;
- the number of reachable detector and residual states;
- the number of base-kernel detector and residual states;
- a finite readout table whose rows contain a representative braid word and
  the residual permutation it induces;
- for each readout row, whether that permutation preserves every quotient
  fibre, how many base fibres contain moved points, and how many total tuples
  are moved;
- a `kernel_failure`, if the identity detector state carries nontrivial
  residual action;
- a `collision_failure`, if two base-kernel words have the same detector
  state but different residual actions.

The property `proves_fixed_n_readout` is true exactly when the search is not
truncated, there is no kernel failure, there is no collision failure, and the
readout table covers every reachable base-kernel detector state.  The property
also requires each row to preserve quotient fibres, so a successful audit is
really a readout of the residual maps `delta_{n,z}`, not merely a readout of
an unrelated total-set permutation.

The companion helper

```text
exact_detector_product_readout_audit(quotient_map,Q,groups,n)
```

compares this readout table for a displayed list of detector factors with the
readout table for the single direct-product detector group `prod_i G_i`, when
the product group is small enough to enumerate.  This is the fixed-index
readout analogue of `proofs/detector_action_products.md`.

For the direct whole-solution route there is now also a named wrapper:

```text
symmetric_detector_readout_audit(X,n)
```

It forms the one-point quotient `X -> {*} ` and uses the single detector
group `Sym(X)`.  A successful nontruncated audit proves the fixed-degree
implication

```text
Lambda_{Sym(X),n}(beta)=Lambda_{Sym(X),n}(1)
    => rho_{X,n}(beta)=1
```

for that particular `n`.  The regression test on the size-three affine stress
row proves this fixed-`n=2` readout exactly: there are `12` reachable
base-kernel detector states and `3` residual action states, with every row
preserving the one quotient fibre.  This is still only fixed-index evidence;
it does not replace the missing all-`n` factorization.

## Relation To The Corridor Target

For the bi-free universal-corridor branch, the proposed detector list is the
two-sided Green kernel-block and Schutzenberger factor list.  The existing
fixed-index exact-image audit says whether this detector list separates
residual actions at one degree.  The readout audit strengthens the diagnostic
by displaying the finite table that would be read out from the detector
state.

This still cannot be cited as a global proof.  A complete A proof must show,
without fixed-degree enumeration, that the Green/corridor residual motion is
always such a readout of `A_G^n` for one finite `G=G(pi,Q)`.  A complete B
proof must instead produce a normalized-law sequence that defeats every
finite group, not merely a collision against one listed fixed-index detector.
