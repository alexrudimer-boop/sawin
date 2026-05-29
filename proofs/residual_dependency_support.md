# Residual dependency support

## Purpose

This note records a fixed-degree diagnostic for the quotient/residual action.
It is not a proof of the master theorem.  It identifies whether, after the
base quotient is fixed, a residual output fibre coordinate depends on one
input fibre coordinate or on several.

This matters for the finite-longitude program because the easiest product
and rack subbranches have coordinatewise normal forms, while the remaining
Green/corridor and bi-free branches must control genuine multi-coordinate
holonomy.

## Definition

Let `pi:X -> Z` be a finite quotient and fix a base tuple `z in Z^n`.  Suppose
`beta in B_n` fixes `z`.  For the residual map

```text
delta_{n,z}(beta): X_z -> X_z,
```

define the support of output coordinate `j` to be the set of input
coordinates `k` such that two fibre tuples differing only at coordinate `k`
can have different `j`-th output coordinates.

If every support has size at most `1`, the residual map is coordinatewise on
that fibre block.  If some support has size greater than `1`, the residual
action contains multi-input dependence.  Such dependence is not by itself an
obstruction to finite-rack domination: ordinary racks already have
multi-input dependence at a crossing, and their action is still detected by
Artin longitudes through the rack inner group.  The diagnostic only says that
a naive product-label or single-coordinate formula cannot be the whole proof.

## Executable helper

The helper

```text
residual_coordinate_dependency_summary(qmap,z,beta)
```

returns:

- the base tuple;
- the braid word;
- the essential input support of every output coordinate;
- the maximum support arity;
- whether the residual map is coordinatewise.

The tests verify:

- identity residual action has singleton supports;
- a dihedral rack crossing over the one-point quotient has support
  `({0,1},{0})`, reflecting the usual rack dependence of the first output on
  both input labels;
- non-base-fixed words are rejected.

There is also a classifier for proposed detector failures:

```text
residual_detector_dependency_failures(qmap,Q,groups,n,words)
```

It first applies the bounded sharp-kernel screen: the word must lie in the
base detector kernel, be invisible to the listed finite groups, and still
move a residual fibre tuple.  For every such bounded mover, it attaches the
dependency summaries for the quotient base tuples fixed by the word.  The
returned `max_arity` and `has_multi_input_support` fields distinguish
coordinatewise/product-like failures from genuinely multi-input failures.

The guardrail test uses a deliberately too-small detector on a dihedral rack.
The pure braid `sigma_1^2` is invisible to the trivial group and moves the
rack, but the classifier reports multi-input support.  This is the expected
diagnosis: the failure is not a product-label obstruction, and it disappears
when the correct rack inner group is used.

## Relation to the A/B fork

For outcome A, this diagnostic suggests the local proof should split:

- coordinatewise residual actions should be handled by product-label,
  coboundary, affine, cyclic, or pairwise-linking finite detector groups;
- multi-coordinate residual actions require the Green/corridor,
  Schutzenberger, kernel-block, and semigroup-holonomy machinery.

For outcome B, a normalized-law sequence must move a tuple despite all
finite-group longitude detectors.  The dependency support tells whether the
motion is a product-label closed holonomy or a genuinely multi-coordinate
structure-orbit holonomy.  Either way, finite-degree dependency evidence must
be upgraded to an all-`j` symbolic sequence before it can prove B.
