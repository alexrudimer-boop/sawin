# Bi-free corridor exact audit

Date: 2026-05-28

This generated audit records the exact fixed-index image closure for
the bi-free/corridor detector factor list on the standard size-three
affine commutator stress row.  The row is not itself a remaining
corridor target: the local router sends it to an already known branch.
Its role is to test the corridor certificate layer against a row where
actual kernel-image groups are too small but full symmetric
kernel-block factors see the mover.

## Detector Target

Target applies: `False`.
Router verdict: `locally_nondegenerate_branch`.
Factor orders: `[2, 3, 6]`.
Detector product order: `36`.
Named factor orders: `{'H1_order_6': 6, 'H2_order_3': 3, 'H3_order_2': 2}`.

## Exact n=2 Closure

Visited states: `12`.
Detector states: `12`.
Residual states: `3`.
Base-kernel detector states: `12`.
Base-kernel residual states: `3`.
Truncated: `False`.
Kernel failure: `None`.
Collision failure: `None`.
Proves fixed-n implication: `True`.

## Exact n=2 Closure With Fixed Extra C5 Factor

This row appends one fixed extra detector factor `C5`, representing
the quotient/known/unit detector slot in the corridor target.
Visited states: `60`.
Detector states: `60`.
Base-kernel detector states: `60`.
Truncated: `False`.
Kernel failure: `None`.
Collision failure: `None`.
Proves fixed-n implication: `True`.

## Direct Product Subgroup Check

Braid degree: `2`.
Braid word: `[1, 1]`.
Factor orders: `[6, 3, 2]`.
Product group order: `36`.
Truncated: `False`.
Product subgroup size: `36`.
Expected factor-product subgroup size: `36`.
Product subgroup equals factor product: `True`.
Product identity signature equivalent to all factor identity signatures: `True`.

## Commutator Certificate

Braid degree: `3`.
Braid word: `[2, 1, 1, -2, 2, 2, 2, -1, -1, -2, -2, -2]`.
Quotient fixed: `True`.
Moves residual tuple: `True`.
Visible factors: `['H1_order_6']`.
All listed factors invisible: `False`.
B-shaped failure against listed factors: `False`.

Subgroup profile:

- `H1_order_6` order `6`, subgroup size `3`, identity signature `False`.
- `H2_order_3` order `3`, subgroup size `1`, identity signature `True`.
- `H3_order_2` order `2`, subgroup size `1`, identity signature `True`.

## Consequence

This exact audit does not prove the corridor theorem.  It does make
the fixed-index certificate reusable at the corridor layer: the
same factor list named by `bifree_corridor_detector_target()` can
be fed into exact finite-image closure.  For the affine stress row,
that exact closure proves the `n=2` implication, while the
commutator mover is seen by the order-`6` symmetric factor and is
therefore not a B-shaped failure against the listed detector
factors.  The extra-`C5` row confirms that fixed quotient, known,
or endpoint/unit factors are part of the exact detector state, not
only part of the separate longitude-subgroup profile.
