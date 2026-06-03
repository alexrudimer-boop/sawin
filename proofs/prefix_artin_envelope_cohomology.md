# Prefix Artin-envelope cohomology pressure

Date: 2026-06-03

The finite-rack point-pushing structure shows that a rack tower is an
operator-label Hurwitz quotient with bounded-exponent vertical kernel.  The
corresponding missing lemma for arbitrary finite bijective YBE solutions can
be phrased as a finite action-groupoid cohomology problem.

## Missing Lemma Form

For every finite bijective YBE solution `X`, there should exist one finite
operator-label Hurwitz model `(H_X,C_X)` and one exponent `e_X` such that, for
all `n`, the point-pushing image

```text
Q_X(n) <= G_X(n+1)
```

admits a marked quotient to the group-Hurwitz point-pushing image
`Q_{H_X,C_X}(n)`, with vertical kernel exponent dividing `e_X`, and these data
are compatible under point-forgetting.

Equivalently, after choosing the quotient action groupoid, the residual
motion of `Q_X(n)` should be represented by a vertical cocycle whose values
live in one uniformly bounded-exponent finite group.  The cocycle must be
natural under the maps `Q_X(n+1) -> Q_X(n)` induced by forgetting a point.

In groupoid language, this is a bounded Artin-equivariant transgression
lemma: every finite local quotient-fibre interval should admit one finite
operator-label groupoid, one finite coefficient system of vertical groups, and
one bounded cohomology class whose pullbacks produce the abelianized residual
point-pushing extension classes in all arities.  The pullbacks must commute
with the Artin insertion, deletion, and relabelling maps.

## Why This Is Cohomological

At fixed `n`, the Fadell-Neuwirth kernel `K_n` is free.  Thus the obstruction
is not simply a relation in the abstract point-pushing kernel.  The pressure
comes from three finite structures:

- the image relations in `Q_X(n)`;
- the stabilizer loops of the action groupoid `Q_X(n) ⋉ X^{n+1}`;
- the restriction maps relating the action groupoids for successive `n`.

A finite operator-label envelope would quotient this action groupoid to a
finite group-Hurwitz action groupoid.  The remaining vertical labels form a
nonabelian cocycle over that quotient.  The positive theorem needs this
cocycle to become bounded-exponent uniformly in `n`.

## First Executable Surface

The generated audit

```text
proofs/prefix_artin_envelope_cohomology_audit.md
```

computes the first two rows:

```text
Q_X(3) <= G_X(4),       Q_X(4) <= G_X(5).
```

For each row it records the point-pushing image size, orbit count, action
groupoid arrow count, stabilizer-loop count, generator-indexed cocycle value
count, and the first point-forgetting naturality squares from `Q_X(4)` down
to `Q_X(3)`.

This is still only a finite-prefix audit.  Its purpose is to make the missing
lemma falsifiable: a candidate obstruction should produce action-groupoid
cocycle data on this surface that cannot be pushed to a fixed finite
group-Hurwitz base with uniformly bounded vertical exponent.

## Obstruction Criterion

A genuine negative route should provide a finite table or local
quotient-fibre interval such that, for every finite `(H,C)` and every
exponent `e`, the compatible tower of action-groupoid cocycles has one of the
following failures:

- no marked quotient to the group-Hurwitz action groupoid exists;
- a stabilizer-loop cocycle class has order not bounded by `e`;
- restriction from `Q_X(n+1)` to `Q_X(n)` changes the cocycle class
  incompatibly with any fixed finite base.

The first concrete place to look remains the marked `Q_X(3),Q_X(4)` surface.
The tiny whole-table audit shows that no size-2 or size-3 whole table gives
such a left-degenerate nonunit-prefix obstruction, so the next negative
search must move to larger whole tables or to quotient-fibre local intervals.
