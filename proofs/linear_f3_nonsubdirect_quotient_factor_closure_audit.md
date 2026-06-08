# Linear F3 Nonsubdirect Quotient-Factor Closure Audit

This generated audit closes the `80` non-subdirect rows in the
six-point linear skew-over-flip degenerate non-involutive family.

## Summary

- source artifact: `proofs\linear_f3_skew_flip_monolith_audit.json`;
- non-subdirect rows: `80`;
- certified rows: `80`;
- failures: `0`;
- all claimed checks passed: `True`.

For each row, the audit selects only proper quotient factors that are
already known dominated: rack-form, nondegenerate, or involutive.
Those selected quotients still reconstruct the original point and pass
the active-factor finite certificate.

## Known Quotient Reasons

| quotient size | reason | count |
|---:|---|---:|
| 2 | rack | 176 |
| 3 | involutive | 160 |
| 3 | nondegenerate | 4 |
| 3 | rack | 52 |
| 4 | involutive | 176 |
| 4 | nondegenerate | 64 |
| 4 | rack | 16 |
| 5 | involutive | 48 |

## Distribution

| cases | known factors | quotient sizes | reconstructs | finite conditions | certified |
|---:|---:|---|---|---|---|
| 20 | 9 | [2, 2, 2, 3, 3, 4, 4, 4, 5] | True | True | True |
| 20 | 13 | [2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5] | True | True | True |
| 16 | 4 | [2, 3, 4, 4] | True | True | True |
| 16 | 6 | [2, 3, 3, 3, 4, 4] | True | True | True |
| 4 | 10 | [2, 2, 2, 3, 3, 3, 4, 4, 4, 5] | True | True | True |
| 4 | 14 | [2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5] | True | True | True |
