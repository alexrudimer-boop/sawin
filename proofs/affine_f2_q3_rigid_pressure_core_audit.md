# Affine F2^3 Rigid Pressure Core Audit

This generated audit applies the rigid-pressure-core filters to the
affine-linear `F_2^3` family using the linear YBE block equations
and affine offset equations.  It is a finite-prefix pressure audit,
not a Sawin counterexample.  The bounded ordered prefix used
below is not the full product of all racks of size at most `3`;
it stops at detector size `36`.

## Census

- linear YBE blocks: `26153`;
- affine YBE tables: `226241`;
- failed bidegeneracy: `149184`;
- failed noninvolutivity: `18369`;
- bidegenerate noninvolutive rows before flip testing: `58688`;
- failed observer-rigidity: `29120`;
- observer-rigid rows: `29568`;
- failed subsolution-rigidity: `21168`;
- subsolution-rigid rows: `8400`;
- failed quotient-rigidity: `5040`;
- rigid structural survivors: `3360`.

Rank histogram:

```text
B_rank=0,C_rank=0: 1
B_rank=1,C_rank=1: 448
B_rank=2,C_rank=2: 14616
B_rank=3,C_rank=3: 11088
```

Valid-offset histogram:

```text
1 valid offsets: 1 linear blocks
2 valid offsets: 336 linear blocks
4 valid offsets: 10584 linear blocks
8 valid offsets: 8616 linear blocks
16 valid offsets: 6090 linear blocks
32 valid offsets: 525 linear blocks
64 valid offsets: 1 linear blocks
```

## First Rigid Pressure Candidate

Matrix rows:

```text
010100
100100
000001
001101
110110
110101
```

- offset: `001100`;
- branch tags: `[]`;
- pair-generated quotient-rigid: `True`;
- not flip-across: `True`;
- bounded-prefix pressure repaired by size-3 rack: `True`.

First pressure row for the bounded ordered rack prefix:

- detector prefix length: `5`;
- detector size: `36`;
- arity: `2`;
- obstruction found: `True`;
- truncated: `False`;
- witness word: `(1, 1, 1, 1)`;
- moved tuple: `((0, 0, 0), (0, 0, 0))`;
- moved image: `((0, 0, 1), (1, 0, 0))`.

Size-three dihedral repair check:

- detector index in `small_rack_representatives(3)`: `8`;
- detector size: `3`;
- two-strand order: `3`;
- kernel inclusion holds through checked arities: `True`;
- image orders match through checked arities: `True`.

Checked repair rows:

- arity `2`: joint `3`, detector `3`, solution `3`, obstruction `False`, truncated `False`.
- arity `3`: joint `24`, detector `24`, solution `24`, obstruction `False`, truncated `False`.
- arity `4`: joint `648`, detector `648`, solution `648`, obstruction `False`, truncated `False`.

## Conclusion

The affine F_2^3 family contains 3360 rows that survive the bidegenerate, noninvolutive, observer-rigid, subsolution-rigid, and pair-generated quotient-rigid filters. The first survivor has kernel pressure against the bounded ordered rack prefix of size 36, but that pressure is repaired by the missing three-element dihedral rack representative: exact checks through arity 4 show matching braid image orders and no detector-kernel obstruction. This is therefore not a valid pressure core yet; the companion native-image audit tests this repair at arity 5, where it fails.
