# Stage A U-Array Audit

Record reusable Stage A checks for the size 5/6 everywhere-singular search: balanced U counts, singular U rows, Y1-derived A_xy feasibility, and simultaneous-relabeling canonicalization.

## Constraints

- each symbol occurs exactly d times in U;
- each row map y -> U[x,y] is singular;
- A_xy={v : L_{U[x,y]} L_v = L_x L_y} is nonempty for every cell;
- U is canonicalized under simultaneous relabeling;

## Example Rows

### identity_3

- size: `3`;
- tags: `('involutive', 'identity_table', 'affine_cyclic')`;
- YBE: `True`;
- balanced symbol counts: `True`;
- rows singular: `True`;
- A_xy nonempty: `True`;
- Stage A candidate: `True`;
- feasibility size range: `3..3`;
- feasibility size counts: `((3, 9),)`;
- canonical: `True`.

### trivial_rack_3

- size: `3`;
- tags: `('rack_type', 'involutive', 'permutation_form', 'left_nondegenerate', 'right_nondegenerate', 'nondegenerate', 'affine_cyclic')`;
- YBE: `True`;
- balanced symbol counts: `True`;
- rows singular: `False`;
- A_xy nonempty: `True`;
- Stage A candidate: `False`;
- feasibility size range: `3..3`;
- feasibility size counts: `((3, 9),)`;
- canonical: `True`.

### dihedral_rack_3

- size: `3`;
- tags: `('rack_type', 'left_nondegenerate', 'right_nondegenerate', 'nondegenerate', 'affine_cyclic')`;
- YBE: `True`;
- balanced symbol counts: `True`;
- rows singular: `False`;
- A_xy nonempty: `True`;
- Stage A candidate: `False`;
- feasibility size range: `1..1`;
- feasibility size counts: `((1, 9),)`;
- canonical: `True`.

### size4_affine_type_a

- size: `4`;
- tags: `()`;
- YBE: `True`;
- balanced symbol counts: `True`;
- rows singular: `True`;
- A_xy nonempty: `True`;
- Stage A candidate: `True`;
- feasibility size range: `2..2`;
- feasibility size counts: `((2, 16),)`;
- canonical: `False`.

## Canonicalization Check

- example: `size4_affine_type_a`;
- canonical equal after relabeling: `True`;

## Enumeration Baseline

### exact_size_2

- size: `2`;
- nodes: `9`;
- completed balanced arrays: `2`;
- row-singular arrays: `2`;
- A_xy feasible arrays: `1`;
- canonical arrays: `1`;
- emitted examples: `1`;
- truncated: `False`.

### exact_size_3

- size: `3`;
- nodes: `2326`;
- completed balanced arrays: `492`;
- row-singular arrays: `492`;
- A_xy feasible arrays: `19`;
- canonical arrays: `6`;
- emitted examples: `6`;
- truncated: `False`.

### budgeted_size_4

- size: `4`;
- nodes: `50000`;
- completed balanced arrays: `15733`;
- row-singular arrays: `15733`;
- A_xy feasible arrays: `107`;
- canonical arrays: `30`;
- emitted examples: `3`;
- truncated: `True`.

## Conclusion

The Stage A code separates one-sided nondegenerate rack rows from everywhere-singular U-data.  The exact size-2 and size-3 enumerations now give a regression baseline, while the budgeted size-4 run confirms the Stage A feasibility test has many nontrivial candidates and needs the requested Pro sharpening before d=5,6 exhaustive enumeration.

## Next Prompt

`prompts/gpt55_pro/2026-06-04-stage-a-u-array-enumeration_ask_now.md`.
