# Linear F3 Skew-Over-Flip Monolith Audit

This generated audit applies the minimal-counterexample monolith
criterion to the 144 degenerate non-involutive six-point linear
skew-over-flip rows.

## Summary

- rows checked: `144`;
- braided-simple rows: `0`;
- subdirectly irreducible rows with nontrivial monolith: `64`;
- monolith J-separating rows: `32`;
- monolith J-collision rows: `32`;
- monolith check skips: `0`;
- collision mismatch-generation failures: `0`;
- all claimed checks passed: `True`.

Rows whose monolith has a formal contextual collision are checked
further: the mismatch pairs from the finite path generate the
monolith as a braided congruence.

## Distribution

| cases | proper congruences | monolith blocks | nontrivial monolith | collision | skipped |
|---:|---:|---|---|---|---|
| 32 | 2 | [1, 1, 1, 3] | True | True | False |
| 20 | 10 | [1, 1, 1, 1, 1, 1] | False | None | None |
| 20 | 16 | [1, 1, 1, 1, 1, 1] | False | None | None |
| 16 | 3 | [1, 1, 1, 3] | True | False | False |
| 16 | 5 | [1, 1, 1, 1, 1, 1] | False | None | None |
| 16 | 5 | [1, 1, 1, 3] | True | False | False |
| 16 | 9 | [1, 1, 1, 1, 1, 1] | False | None | None |
| 4 | 11 | [1, 1, 1, 1, 1, 1] | False | None | None |
| 4 | 17 | [1, 1, 1, 1, 1, 1] | False | None | None |

## Consequence

None of these 144 degenerate non-involutive six-point rows is
braided-simple.  The subdirectly irreducible rows split between
formal monolith J-separation and formal monolith J-collision.
This is still not a Sawin counterexample: a true minimal
counterexample requires a Brunnian-realized detector-kernel
collision, not merely a formal contextual collision.
