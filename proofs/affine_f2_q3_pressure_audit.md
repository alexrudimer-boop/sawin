# Affine F2 Q3 Pressure Audit

This generated audit reconstructs the affine-linear `F_2^3` YBE
linear-block count from the block equations and then tests the first
left-degenerate non-involutive affine row against the exact `Q_3`
bounded-deletion obstruction.

## Linear Blocks

- dimension: `3`;
- invertible linear YBE blocks: `26153`;
- singular left block `B`: `15065`;
- singular right block `C`: `15065`.

Rank histogram:

```text
B_rank=0,C_rank=0: 1
B_rank=1,C_rank=1: 448
B_rank=2,C_rank=2: 14616
B_rank=3,C_rank=3: 11088
```

The count `26153` matches the previously recorded aggregate
`F_2^3` affine scan.

## First Pressure Row

Matrix rows:

```text
100000
000001
000010
000100
001000
010000
```

Offset: `000011`.

This row is left-degenerate, non-involutive, and has no current
`branch_tags` classification.  Its cheap front-end readout is:

```text
a_X(2) = 2
first pure nontrivial arity = 2
```

Exact `Q_3` deletion checks:

```text
affine compressed n=3: E=1, joint=1728, nontrivial=False
stabilizer n=4: E=1, joint=1119744, nontrivial=False
```

The follow-up hidden-gauge proof in
`proofs/affine_f2_hidden_cyclic_gauge.md` closes this row in all
arities: after a position-dependent change of coordinates, this
row is braid-kernel equivalent to the two-element cyclic rack.
Thus `Q_2` already dominates it, and

```text
E^{(3)}_{X,h,n} = 1 for every h,n.
```

The finite `n=3,4` computations above are retained as regression
checks of the compressed and stabilizer implementations.
