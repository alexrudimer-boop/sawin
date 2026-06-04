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

## Conclusion

The Stage A code separates one-sided nondegenerate rack rows from everywhere-singular U-data.  The size-4 affine Type A row passes Stage A and is therefore a useful regression example for the planned d=5,6 enumeration.

## Next Prompt

`prompts/gpt55_pro/2026-06-04-stage-a-u-array-enumeration_ask_now.md`.
