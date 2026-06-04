# Affine F2^3 Period-3 Reduction Audit

The explicit D_n map intertwines the shifted-linear X action with the reduced tetrahedral action on adjacent-difference coordinates through every checked arity.  Its kernel is pointwise fixed by the X generators, and D_n together with all linear invariant observers separates the full X module except for a two-dimensional remainder exactly when n is divisible by 3.  This supports the reduction of the remaining rack24-domination question to a period-3 shear cocycle at arities 3k.

## Intertwiner

For edge `i`, define

```text
p_i = a_i + b_i + a_{i+1}
q_i = c_i + c_{i+1}
D_n(x)_i = C_{n-i mod 3}(p_i,q_i).
```

The three matrices are:

- `C_0=[[1,0],[1,1]]`;
- `C_1=[[1,1],[0,1]]`;
- `C_2=[[0,1],[1,0]]`.

The audit checks

```text
D_n X_i = Ybar_i D_n
```

where `Ybar_i` is the tetrahedral rack action induced on adjacent differences `eta_i=z_i+z_{i+1}`.

## Rank Rows

| n | rank D | dim ker D | dim Inv | ker D fixed | combined rank | missing dim | 3 divides n |
|---|---:|---:|---:|---|---:|---:|---|
| 2 | 2 | 4 | 4 | True | 6 | 0 | False |
| 3 | 4 | 5 | 5 | True | 7 | 2 | True |
| 4 | 6 | 6 | 6 | True | 12 | 0 | False |
| 5 | 8 | 7 | 7 | True | 15 | 0 | False |
| 6 | 10 | 8 | 8 | True | 16 | 2 | True |
| 7 | 12 | 9 | 9 | True | 21 | 0 | False |
| 8 | 14 | 10 | 10 | True | 24 | 0 | False |
| 9 | 16 | 11 | 11 | True | 25 | 2 | True |
| 10 | 18 | 12 | 12 | True | 30 | 0 | False |
| 11 | 20 | 13 | 13 | True | 33 | 0 | False |
| 12 | 22 | 14 | 14 | True | 34 | 2 | True |
| 13 | 24 | 15 | 15 | True | 39 | 0 | False |
| 14 | 26 | 16 | 16 | True | 42 | 0 | False |
| 15 | 28 | 17 | 17 | True | 43 | 2 | True |
| 16 | 30 | 18 | 18 | True | 48 | 0 | False |
| 17 | 32 | 19 | 19 | True | 51 | 0 | False |
| 18 | 34 | 20 | 20 | True | 52 | 2 | True |

## Consequence

If `beta` is trivial in the full tetrahedral rack action, then it is trivial on the reduced adjacent-difference action.  The `D_n` intertwiner therefore forces the non-fixed part of the shifted `X` action to be trivial.  The invariant observers are fixed by every braid.  For `3` not dividing `n`, these data have full rank, so rack24 domination holds in those arities.  For `n=3k`, the only remaining possible mismatch is a two-dimensional shear.

The first unchecked arity after the existing `n=3` and `n=6` joint-kernel computations is therefore `n=9`.
