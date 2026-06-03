# Prefix vertical defect transform audit

Date: 2026-06-03

This generated audit extracts the diagonal/deleted-generator
point-forgetting defects as transformations of the remaining target
tuple space.  It is the first coefficient-candidate step after the
single, square, and cube deletion ledgers.

For each deleted-generator row it groups source tuples by the tuple
left after deleting the stationary strands.  If every group has one
deleted-after-source value, the defect descends to a transformation
of the target tuple space; if that transformation is bijective, it is
a finite vertical coefficient candidate.

## Rows

### nondegenerate_prefix_witness

- element count: `2`;
- left-prefix monoid size: `2`;
- nonunit prefix count: `0`;
- row count: `54`;
- all defects well-defined on post-deletion target tuples: `True`;
- all defects are permutations: `True`;
- nontrivial defect count: `54`;
- order spectrum: `(2,)`;
- verifies extraction: `True`.

Level summaries:

- deletion level `1`: rows `4`, target tuple counts `(16,)`, orders `(2,)`, identity rows `0`, nontrivial rows `4`, distinct defects `1`.
- deletion level `2`: rows `20`, target tuple counts `(16,)`, orders `(2,)`, identity rows `0`, nontrivial rows `20`, distinct defects `1`.
- deletion level `3`: rows `30`, target tuple counts `(8,)`, orders `(2,)`, identity rows `0`, nontrivial rows `30`, distinct defects `1`.

Defect rows:

- level `1`, forget `(1,)`, source `alpha_{1,5}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `1`, forget `(2,)`, source `alpha_{2,5}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `1`, forget `(3,)`, source `alpha_{3,5}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `1`, forget `(4,)`, source `alpha_{4,5}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(1, 2)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(1, 2)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(1, 3)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(1, 3)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(1, 4)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(1, 4)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(1, 5)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(1, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(2, 3)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(2, 3)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(2, 4)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(2, 4)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(2, 5)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(2, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(3, 4)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(3, 4)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(3, 5)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(3, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(4, 5)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `2`, forget `(4, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0, 0)` and maps to `(0, 0, 0, 1)`.
- level `3`, forget `(1, 2, 3)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(1, 2, 3)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(1, 2, 3)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(1, 2, 4)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(1, 2, 4)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(1, 2, 4)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(1, 2, 5)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(1, 2, 5)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(1, 2, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(1, 3, 4)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(1, 3, 4)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(1, 3, 4)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(1, 3, 5)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(1, 3, 5)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(1, 3, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(1, 4, 5)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(1, 4, 5)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(1, 4, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(2, 3, 4)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(2, 3, 4)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(2, 3, 4)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(2, 3, 5)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(2, 3, 5)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(2, 3, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(2, 4, 5)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(2, 4, 5)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(2, 4, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(3, 4, 5)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(3, 4, 5)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.
- level `3`, forget `(3, 4, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `2`, identity `False`, witness `(0, 0, 0, 0, 0, 0)` has target input `(0, 0, 0)` and maps to `(0, 0, 1)`.

### degenerate_identity_vertical_defects

- element count: `2`;
- left-prefix monoid size: `3`;
- nonunit prefix count: `2`;
- row count: `54`;
- all defects well-defined on post-deletion target tuples: `True`;
- all defects are permutations: `True`;
- nontrivial defect count: `0`;
- order spectrum: `(1,)`;
- verifies extraction: `True`.

Level summaries:

- deletion level `1`: rows `4`, target tuple counts `(16,)`, orders `(1,)`, identity rows `4`, nontrivial rows `0`, distinct defects `1`.
- deletion level `2`: rows `20`, target tuple counts `(16,)`, orders `(1,)`, identity rows `20`, nontrivial rows `0`, distinct defects `1`.
- deletion level `3`: rows `30`, target tuple counts `(8,)`, orders `(1,)`, identity rows `30`, nontrivial rows `0`, distinct defects `1`.

Defect rows:

- level `1`, forget `(1,)`, source `alpha_{1,5}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `1`, forget `(2,)`, source `alpha_{2,5}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `1`, forget `(3,)`, source `alpha_{3,5}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `1`, forget `(4,)`, source `alpha_{4,5}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(1, 2)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(1, 2)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(1, 3)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(1, 3)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(1, 4)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(1, 4)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(1, 5)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(1, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(2, 3)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(2, 3)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(2, 4)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(2, 4)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(2, 5)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(2, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(3, 4)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(3, 4)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(3, 5)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(3, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(4, 5)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `2`, forget `(4, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 2, 3)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 2, 3)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 2, 3)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 2, 4)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 2, 4)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 2, 4)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 2, 5)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 2, 5)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 2, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 3, 4)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 3, 4)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 3, 4)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 3, 5)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 3, 5)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 3, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 4, 5)`, source `alpha_{1,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 4, 5)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(1, 4, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(2, 3, 4)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(2, 3, 4)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(2, 3, 4)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(2, 3, 5)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(2, 3, 5)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(2, 3, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(2, 4, 5)`, source `alpha_{2,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(2, 4, 5)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(2, 4, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(3, 4, 5)`, source `alpha_{3,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(3, 4, 5)`, source `alpha_{4,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.
- level `3`, forget `(3, 4, 5)`, source `alpha_{5,6}`: well-defined `True`, permutation `True`, order `1`, identity `True`, witness `none`.

## Meaning

For the nondegenerate prefix witness, all `54` deleted-generator
defects descend to permutations of the remaining tuple space and
all have order `2`.  At each deletion level there is one distinct
nontrivial defect permutation.  This turns the raw mismatch ledgers
into a concrete finite coefficient candidate.

For the degenerate identity row, all `54` defects are identity
permutations.  Thus nonunit prefix memory alone does not produce
vertical point-forgetting coefficients.

This still does not compute a gauge-invariant Peiffer class.  It
identifies the vertical groups on which such a class would live:
a positive proof must show that these coefficient candidates and
their face transports pull back from one fixed finite operator-label
Artin envelope; a negative proof must find incompatible transported
square boundaries.
