# Prefix Artin-envelope cohomology audit

Date: 2026-06-03

This generated audit records the first finite action-groupoid
surface for the missing finite operator-label Artin-envelope lemma.
It is a cohomology pressure ledger, not a computation of group
cohomology.

For each of `Q_X(3)` and `Q_X(4)` it records:

- the point-pushing image size and exponent, when untruncated;
- the number of orbits of the action on `X^{n+1}`;
- the action-groupoid arrow count `|Q_X(n)| |X|^{n+1}`;
- stabilizer-loop arrows, where vertical cocycles must be bounded;
- generator-indexed vertical cocycle values;
- the first point-forgetting naturality squares from `Q_X(4)` to
  `Q_X(3)`.

## Rows

### nondegenerate_prefix_witness

- element count: `2`;
- left-prefix monoid size: `2`;
- nonunit prefix count: `0`;
- operator-label variable count: `4`;
- checked arities: `(3, 4)`;
- all rows untruncated: `True`;
- records cohomology pressure: `True`.

#### Q_X(3) in B_4

- tuple count: `16`;
- generator count: `3`;
- point-pushing group size: `8`;
- point-pushing group exponent: `2`;
- orbit count: `2`;
- max orbit size: `8`;
- action-groupoid arrow count: `128`;
- stabilizer-loop arrow count: `16`;
- generator cocycle value count: `48`;
- restriction to previous required: `False`;
- forgetting-naturality square count: `0`;
- truncated: `False`.

#### Q_X(4) in B_5

- tuple count: `32`;
- generator count: `4`;
- point-pushing group size: `16`;
- point-pushing group exponent: `2`;
- orbit count: `2`;
- max orbit size: `16`;
- action-groupoid arrow count: `512`;
- stabilizer-loop arrow count: `32`;
- generator cocycle value count: `128`;
- restriction to previous required: `True`;
- forgetting-naturality square count: `512`;
- truncated: `False`.

### degenerate_identity_cohomology_surface

- element count: `2`;
- left-prefix monoid size: `3`;
- nonunit prefix count: `2`;
- operator-label variable count: `6`;
- checked arities: `(3, 4)`;
- all rows untruncated: `True`;
- records cohomology pressure: `True`.

#### Q_X(3) in B_4

- tuple count: `16`;
- generator count: `3`;
- point-pushing group size: `1`;
- point-pushing group exponent: `1`;
- orbit count: `16`;
- max orbit size: `1`;
- action-groupoid arrow count: `16`;
- stabilizer-loop arrow count: `16`;
- generator cocycle value count: `48`;
- restriction to previous required: `False`;
- forgetting-naturality square count: `0`;
- truncated: `False`.

#### Q_X(4) in B_5

- tuple count: `32`;
- generator count: `4`;
- point-pushing group size: `1`;
- point-pushing group exponent: `1`;
- orbit count: `32`;
- max orbit size: `1`;
- action-groupoid arrow count: `32`;
- stabilizer-loop arrow count: `32`;
- generator cocycle value count: `128`;
- restriction to previous required: `True`;
- forgetting-naturality square count: `512`;
- truncated: `False`.

## Meaning

At a fixed arity, `K_n` is free, so the cohomology pressure is
not a pure-braid presentation-relator issue.  The finite
obligations are instead action-groupoid obligations: choose a
fixed finite group-Hurwitz quotient, express the remaining
motion as a vertical cocycle over its orbits and stabilizers,
and make those cocycles compatible under point-forgetting.
Equivalently, a positive proof needs a bounded
Artin-equivariant transgression lemma: one finite operator-label
groupoid, one finite coefficient system, and one bounded class
whose pullbacks recover the residual point-pushing extension
classes in every arity.

The nondegenerate witness has two orbits at both checked
arities and action-groupoid arrow counts `128` and `512`.
The degenerate identity row has nonunit prefix memory but
trivial point-pushing image, so every tuple is a singleton
orbit and the only stabilizer loops are identity loops.

A positive proof must show that this ledger is controlled by
one finite operator-label model with uniformly bounded vertical
exponent in every arity.  A negative proof must find a local
interval or larger finite table where these orbit-stabilizer
cocycle ledgers are incompatible with every fixed finite
group-Hurwitz base.
