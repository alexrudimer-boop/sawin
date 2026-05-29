# Dual Green symmetry

Date: 2026-05-28

The Green detector audit was initially left-handed: it used the
first-coordinate transformations

```text
tau_x(y) = pr_1 R(x,y).
```

For a full residual detector this is not enough bookkeeping.  The same braid
action can also carry recurrent information through the right-coordinate
maps

```text
rho_x(y) = pr_2 R(y,x).
```

This note records the exact dualization used by the proof code.

## Opposite solution

For a finite braided set `R`, define the side-opposite braided set

```text
R^op(x,y) = P R P (x,y),
```

where `P(x,y)=(y,x)`.  Equivalently, if

```text
R(x,y) = (lambda_x(y), rho_y(x)),
```

then

```text
R^op(x,y) = (rho_x(y), lambda_y(x)).
```

The braid equation is invariant under this simultaneous side reversal, so
`R^op` is again a finite bijective YBE solution whenever `R` is.  The
first-coordinate maps of `R^op` are exactly the right-coordinate maps of
`R`.

## Dual structure relation

The usual left coordinate-action relation is

```text
tau_x tau_y = tau_u tau_v
when R(x,y)=(u,v).
```

Applying the same identity to `R^op`, or reading the third coordinate in the
YBE directly, gives the right-coordinate relation

```text
rho_y rho_x = rho_v rho_u
when R(x,y)=(u,v).
```

Thus every kernel-block and Schutzenberger construction from the Green audit
has a right-handed copy obtained by applying the original audit to `R^op`.

## Detector consequence

The finite detector candidate should include both sides:

```text
G_green(X) =
  product over left regular Green classes of Sym(kernel blocks)
  x
  product over right regular Green classes of Sym(kernel blocks)
  x
  the corresponding finite Schutzenberger factors when used.
```

This group is finite and depends only on the local interval data, not on the
braid index `n`.  The new helper
`two_sided_kernel_symmetric_groups(X)` returns the full symmetric
kernel-block factors from both `X` and `X^op`, with duplicate finite groups
removed.

The candidate group has now been made fully explicit in
`proofs/green_detector_group_candidate.md`.  In addition to the symmetric
kernel-block factors, the code exposes the finite Schutzenberger action
groups by `schutzenberger_action_groups()`, `schutzenberger_groups()`, and
`two_sided_schutzenberger_groups()`.  The helper
`two_sided_green_detector_groups(X)` returns the combined finite factor list,
and `two_sided_green_detector_product(X)` multiplies it into one finite group
for use in the sharp obstruction theorem.

This still does not prove the Master Local-Minimal Residual Theorem.  It
closes an asymmetry in the candidate detector: an A-proof must show that the
two-sided Green data detects all recurrent branch choices, and a B
counterexample must escape both the left and right finite kernel-block
detectors.

There is now also a theorem-level closure statement in
`proofs/opposite_detectability_closure.md`.  It proves that if one fixed
finite group `G` detects a whole solution `X` in the sharp longitude sense,
then the same `G` detects the side-opposite solution `X^op=P R P`.  The proof
uses strand reversal of braid words and does not rely on finite search.  Thus
the right-handed detector layer is not merely a diagnostic mirror; it is
compatible with the actual finite-G domination criterion.

## Executable checks

The proof code now includes:

- `opposite_solution(X)`;
- `right_coordinate_action_maps(X)`;
- `right_coordinate_action_relation_failures(X)`;
- `opposite_green_branch_audits(X)`;
- `two_sided_kernel_symmetric_groups(X)`.

Unit tests verify that `opposite_solution` preserves YBE on a nontrivial rack,
that the right-coordinate relation holds on the size-three affine commutator
candidate, and that the two-sided symmetric kernel detector deduplicates the
left/right `S_3` factor in that candidate.

## Generated tiny-corpus audit

The generated report is `proofs/dual_green_audit.json`.

For all size-2 and size-3 bijective YBE tables in the tiny corpus:

- opposite-solution YBE failures: `0`;
- right-coordinate structure-relation failures: `0`;
- maximum two-sided symmetric kernel group order: `2` in size `2`, `6` in
  size `3`;
- commutator-law movers: `0` in size `2`, `12` in size `3`;
- commutator movers blind to the two-sided symmetric kernel groups: `0`.

For the local-minimal congruence-cover intervals in the same size range:

- local-minimal covers: `5` in size `2`, `134` in size `3`;
- opposite-solution YBE failures: `0`;
- right-coordinate structure-relation failures: `0`;
- commutator-law mover intervals: `0` in size `2`, `12` in size `3`;
- commutator mover intervals blind to the two-sided symmetric kernel groups:
  `0`.

These are bounded checks only.  They are useful because they show that adding
the right-handed Green layer does not create a new tiny obstruction and that
the existing size-three commutator movers remain visible to the strengthened
two-sided finite detector.
