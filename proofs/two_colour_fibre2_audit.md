# Two-colour fibre-2 local audit

## Purpose

This audit searches a structured local interval family that is larger than the
whole-solution size-3 scan but still small enough to enumerate exactly:

- two quotient colours;
- two fibre points over each colour;
- either the identity base `R_Z(a,b)=(a,b)` or the flip base `R_Z(a,b)=(b,a)`;
- all bijective local maps `T_{a,b}` compatible with the chosen base.

This is candidate discovery only.  It is not used as proof evidence for the
global theorem.

## Results

For the identity base:

```text
tables checked: 331776
coloured YBE tables: 33
local-minimal intervals: 32
two-sided retraction split: universal 32
product-permutation witnesses: 32
branch tags: involutive 16, untagged 16
unknown local-minimal primitive examples: 0
```

The tagless half is not an obstruction: every local-minimal interval has the
product-permutation witness from the universal two-sided-retraction branch.

For the flip base:

```text
tables checked: 331776
coloured YBE tables: 520
local-minimal intervals: 12
two-sided retraction split: equality 12
branch tags: involutive 12
unknown local-minimal primitive examples: 0
```

Thus this structured family contains no primitive degenerate local-minimal
example outside the already measurable branches.  In particular, the
two-colour/fibre-2 flip-base primitive cases fall entirely into the
involutive branch, while the identity-base cases fall into the
universal/product-permutation branch.

## Consequence

The scan gives a more targeted failed counterexample search than the raw tiny
whole-solution audit.  It supports the current split of the master gap:

- universal two-sided retraction is product-permutation;
- primitive equality/two-sided-retraction-free intervals seen so far are already
  nondegenerate, involutive, rack-type, or affine/coboundary measurable;
- a B-style counterexample must therefore escape these two-colour/fibre-2
  patterns and evade the symmetric kernel-block detector.
