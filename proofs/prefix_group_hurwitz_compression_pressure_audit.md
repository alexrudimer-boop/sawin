# Prefix group-Hurwitz compression pressure audit

Date: 2026-06-03

This generated audit records the finite equation family that a
group-Hurwitz compression of the prefix-edge transducer must solve.
A compression would assign each prefix edge `(P,x,P lambda_x)` a
label in one finite group, with conjugation-stable image, so that
local prefix-edge braid moves descend to ordinary Hurwitz moves.

The audit does not search all finite groups.  It records the
local Hurwitz-label equations, the corresponding total-product
invariance equations, the point-forgetting rescan lumpability
equations, and whether the left-prefix monoid contains nonunits.
Nonunit prefixes cannot be faithfully embedded as a transformation
monoid inside a group, so a true group-Hurwitz model must quotient
or encode that memory with extra bounded vertical noise.

## Rows

### nondegenerate_prefix_witness

- element count: `2`;
- left-prefix monoid size: `2`;
- edge state count: `4`;
- nonunit prefix count: `0`;
- faithful prefix-monoid group embedding obstructed: `False`;
- local Hurwitz-label equation count: `8`;
- product-invariance equation count: `8`;
- forgetting-rescan lumpability equation count: `16`;
- first obstruction arities: `(3, 4)`;
- records group-Hurwitz compression pressure: `True`.

### degenerate_identity_nonunit_prefix

- element count: `2`;
- left-prefix monoid size: `3`;
- edge state count: `6`;
- nonunit prefix count: `2`;
- faithful prefix-monoid group embedding obstructed: `True`;
- local Hurwitz-label equation count: `12`;
- product-invariance equation count: `12`;
- forgetting-rescan lumpability equation count: `36`;
- first obstruction arities: `(3, 4)`;
- records group-Hurwitz compression pressure: `True`.

## Meaning

The prefix-edge transducer is finite, but a finite transducer
tower is weaker than a finite group-Hurwitz tower.  The next
positive route must produce a fixed finite group label model
satisfying these local equations and compatible with rescanning
under point-forgetting.  The next negative route must find a
finite degenerate solution where every such label model leaves
vertical behaviour in `Q_X(3), Q_X(4), ...` that cannot be
bounded by one fixed exponent.
