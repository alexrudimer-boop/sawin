# Prefix vertical Peiffer square audit

Date: 2026-06-03

This generated audit computes the first Peiffer square boundary for
diagonal vertical deletion defects.  It fixes source point-pushing
arity `5`.  For each deleted stationary pair `{i,j}`, it forms the
two vertical defect permutations on the target tuple space after
deleting both strands and computes their commutator

```text
[defect_i, defect_j]
```

using the repository's left-after-right permutation convention.

## Rows

### nondegenerate_prefix_witness

- element count: `2`;
- left-prefix monoid size: `2`;
- nonunit prefix count: `0`;
- source point-pushing arity: `5`;
- row count: `10`;
- all defects are permutations: `True`;
- all single transports commute: `True`;
- all Peiffer boundaries identity: `True`;
- nontrivial Peiffer boundary count: `0`;
- total Peiffer moved tuple count: `0`;
- defect order-pair spectrum: `((2, 2),)`;
- Peiffer order spectrum: `(1,)`;
- verifies Peiffer square audit: `True`.

Pair summaries:

- `(1, 2)`: defect orders `((2, 2),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(1, 3)`: defect orders `((2, 2),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(1, 4)`: defect orders `((2, 2),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(1, 5)`: defect orders `((2, 2),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(2, 3)`: defect orders `((2, 2),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(2, 4)`: defect orders `((2, 2),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(2, 5)`: defect orders `((2, 2),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(3, 4)`: defect orders `((2, 2),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(3, 5)`: defect orders `((2, 2),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(4, 5)`: defect orders `((2, 2),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.

Peiffer rows:

- delete `(1, 2)`: defect orders `(2, 2)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(1, 3)`: defect orders `(2, 2)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(1, 4)`: defect orders `(2, 2)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(1, 5)`: defect orders `(2, 2)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(2, 3)`: defect orders `(2, 2)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(2, 4)`: defect orders `(2, 2)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(2, 5)`: defect orders `(2, 2)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(3, 4)`: defect orders `(2, 2)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(3, 5)`: defect orders `(2, 2)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(4, 5)`: defect orders `(2, 2)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.

### degenerate_identity_peiffer_square

- element count: `2`;
- left-prefix monoid size: `3`;
- nonunit prefix count: `2`;
- source point-pushing arity: `5`;
- row count: `10`;
- all defects are permutations: `True`;
- all single transports commute: `True`;
- all Peiffer boundaries identity: `True`;
- nontrivial Peiffer boundary count: `0`;
- total Peiffer moved tuple count: `0`;
- defect order-pair spectrum: `((1, 1),)`;
- Peiffer order spectrum: `(1,)`;
- verifies Peiffer square audit: `True`.

Pair summaries:

- `(1, 2)`: defect orders `((1, 1),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(1, 3)`: defect orders `((1, 1),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(1, 4)`: defect orders `((1, 1),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(1, 5)`: defect orders `((1, 1),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(2, 3)`: defect orders `((1, 1),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(2, 4)`: defect orders `((1, 1),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(2, 5)`: defect orders `((1, 1),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(3, 4)`: defect orders `((1, 1),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(3, 5)`: defect orders `((1, 1),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.
- `(4, 5)`: defect orders `((1, 1),)`, Peiffer orders `(1,)`, moved tuples `0`, nontrivial boundaries `0`.

Peiffer rows:

- delete `(1, 2)`: defect orders `(1, 1)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(1, 3)`: defect orders `(1, 1)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(1, 4)`: defect orders `(1, 1)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(1, 5)`: defect orders `(1, 1)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(2, 3)`: defect orders `(1, 1)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(2, 4)`: defect orders `(1, 1)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(2, 5)`: defect orders `(1, 1)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(3, 4)`: defect orders `(1, 1)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(3, 5)`: defect orders `(1, 1)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.
- delete `(4, 5)`: defect orders `(1, 1)`, transports `(True, True)`, Peiffer order `1`, identity `True`, moved tuples `0`, witness `none`.

## Meaning

For the nondegenerate prefix witness, the first Peiffer commutator
boundary is trivial on every two-deletion face.  The diagonal
vertical defects are order-two permutations, but their pair-face
commutators are identity.

For the degenerate identity row, the same Peiffer boundaries are
identity for the trivial reason that all diagonal defects are
identity permutations.

This rules out the simplest square-boundary obstruction for this
toy prefix surface.  It still does not prove finite rack domination:
the next obstruction layer must normalize section choices and test
whether higher or mixed square classes pull back from one fixed
finite operator-label Hurwitz base.
