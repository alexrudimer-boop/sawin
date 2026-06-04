# Affine F2^3 Period-3 Shear Split Audit

The period-3 hidden shear space is pointwise fixed in every checked arity, but the generator shear is not a global linear coboundary through arity 30.  Thus the remaining domination question cannot be closed by a simple section change that splits the extension.  The kernel question remains subtler: the nonsplit extension may still be trivial on the tetrahedral rack kernel.

## Rows

| n | quotient dim | hidden fixed | variables | equations | section coboundary exists | rank |
|---|---:|---|---:|---:|---|---:|
| 3 | 7 | True | 14 | 28 | False | 4 |
| 6 | 16 | True | 32 | 160 | False | 16 |
| 9 | 25 | True | 50 | 400 | False | 28 |
| 12 | 34 | True | 68 | 748 | False | 40 |
| 15 | 43 | True | 86 | 1204 | False | 52 |
| 18 | 52 | True | 104 | 1768 | False | 64 |
| 21 | 61 | True | 122 | 2440 | False | 76 |
| 24 | 70 | True | 140 | 3220 | False | 88 |
| 27 | 79 | True | 158 | 4108 | False | 100 |
| 30 | 88 | True | 176 | 5104 | False | 112 |

## Interpretation

For `n=3k`, the map `D_n` plus invariant observers leaves a two-dimensional hidden space.  Since this hidden space is fixed, one might hope that the generator shear is merely a coboundary `P(A_i q)+P(q)` and can be removed by changing the section.  This audit solves exactly that finite linear system.  It is inconsistent in every checked arity, including `n=3` and `n=6` where the full joint-kernel check is already known to pass.  So the all-arity proof must use relations in the tetrahedral rack image, not just a split-extension gauge.
