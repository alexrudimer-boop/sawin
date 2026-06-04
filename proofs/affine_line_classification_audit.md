# Affine-Line Classification Audit

This generated audit upgrades the finite affine-line scans to a
symbolic all-field lemma for one-dimensional affine YBE maps.

## Ansatz

`r(x,y)=(a x+b y+c, d x+e y+f) over a field`.

The Yang-Baxter equation is equivalent to the following polynomial
relations:

- `a(a+bd-1)=0`;
- `abe=0`;
- `a(bf+c)=0`;
- `ade=0`;
- `ae(e-a)=0`;
- `-ace+aef-af-bf+cd+ce-c+f=0`;
- `e(1-e-bd)=0`;
- `e(cd+f)=0`;

The left-degenerate condition is `b=0`, the right-degenerate
condition is `d=0`, and bijectivity is `ae-bd != 0`.

## Bidegenerate Classification

Assume `b=d=0 and ae != 0`.

- a(a-1)=0 and a != 0 force a=1;
- e(1-e)=0 and e != 0 force e=1;
- e(cd+f)=0 with d=0 and e=1 forces f=0;
- the middle constant equation then forces c=0;

Conclusion: the only bidegenerate bijective affine-line YBE solution is r(x,y)=(x,y).

Consequence: no bidegenerate non-involutive affine-line rigid core exists over any field.

## Finite Spot Checks

### `F_2`

- affine YBE count: `5`;
- terminal survivor count: `0`;
- bidegenerate bijective YBE row count: `1`;
- all bidegenerate rows identity: `True`.

### `F_3`

- affine YBE count: `31`;
- terminal survivor count: `0`;
- bidegenerate bijective YBE row count: `1`;
- all bidegenerate rows identity: `True`.

### `F_5`

- affine YBE count: `221`;
- terminal survivor count: `0`;
- bidegenerate bijective YBE row count: `1`;
- all bidegenerate rows identity: `True`.

### `F_7`

- affine YBE count: `715`;
- terminal survivor count: `0`;
- bidegenerate bijective YBE row count: `1`;
- all bidegenerate rows identity: `True`.

## Conclusion

The prime-line scans over F_3, F_5, and F_7 are instances of an all-field lemma: bidegenerate bijective affine-line YBE maps are forced to be the identity solution.  Hence the one-dimensional affine-line family cannot contain a minimal rigid core.
