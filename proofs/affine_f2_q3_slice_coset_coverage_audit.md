# Affine F2^3 Slice Coset Coverage Audit

For every checked arity through 8, every quotient coset of the full shifted-linear X representation induces an affine W-action that is conjugate to the tetrahedral rack action on at least one invariant Alexander slice L_n=s.  This is stronger than checking one fibre: it is finite evidence that the full X action is controlled by the rack slice family.

## Rows

| n | quotient dim | cosets | all covered | slice count 0 | slice count 1 | slice count t | slice count t+1 | seconds |
|---|---:|---:|---|---:|---:|---:|---:|---:|
| 2 | 4 | 16 | True | 16 | 16 | 16 | 16 | 0.001 |
| 3 | 5 | 32 | True | 8 | 24 | 24 | 24 | 0.018 |
| 4 | 6 | 64 | True | 64 | 64 | 64 | 64 | 0.166 |
| 5 | 7 | 128 | True | 128 | 128 | 128 | 128 | 1.231 |
| 6 | 8 | 256 | True | 64 | 192 | 192 | 192 | 6.564 |
| 7 | 9 | 512 | True | 512 | 512 | 512 | 512 | 24.782 |
| 8 | 10 | 1024 | True | 1024 | 1024 | 1024 | 1024 | 98.541 |

## Interpretation

The shifted-linear `X` representation has an invariant fibre module `W_n`, and the quotient `V_n/W_n` is fixed by the braid generators.  Each quotient coset therefore carries an affine action on `W_n`.  This audit checks those affine actions one coset at a time and tests whether each is affine-conjugate to rack24 on some invariant slice `L_n=s` over `F_4`.

A uniform proof of this all-coset slice coverage would be a direct route from the tetrahedral rack action to the full shifted-linear `X` action.
