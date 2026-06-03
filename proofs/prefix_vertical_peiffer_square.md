# Prefix vertical Peiffer square

Date: 2026-06-03

The vertical-defect transport audit shows that each already-vertical diagonal
defect is functorial under one additional stationary deletion.  This note
records the next square-boundary datum: the Peiffer commutator of the two
diagonal defects on a two-deletion face.

Fix source point-pushing arity `5`, so the source braid index is `6`.  For a
deleted stationary pair `{i,j}`, the two deleted generators `alpha_{i,6}` and
`alpha_{j,6}` both become vertical after deleting `{i,j}`.  The audit forms
their two vertical defect permutations on the post-deletion target tuple space
and computes the commutator:

```text
[defect_i, defect_j].
```

The generated audit is:

```text
proofs/prefix_vertical_peiffer_square_audit.md
```

It checks all `10` two-deletion faces.  For the nondegenerate two-point prefix
witness, all pair-face diagonal defects have order `2`, but every Peiffer
commutator is identity.  The Peiffer order spectrum is `(1,)`, the
nontrivial-boundary count is `0`, and the total moved-tuple count is `0`.

For the degenerate identity row, all diagonal defects are identity
permutations, and all Peiffer commutators are identity as well.

Thus the first square-boundary pressure test does not produce a counterexample
on this toy prefix surface.  The remaining obstruction must be subtler:
normalize section choices, include mixed/higher square data, and decide
whether the resulting classes are pullbacks from one fixed finite
operator-label Hurwitz base.
