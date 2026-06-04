# Affine F2 Terminal-Branch Audit

This generated audit applies `terminal_branch_triage_audit(...)` to the
translated affine four-point universe from `proofs/affine_f2_audit.md`.
It is a finite search artifact, not a proof of the universal theorem.

## Summary

- affine maps checked: `1048576`;
- invertible affine maps: `322560`;
- affine YBE tables: `481`;
- untagged affine YBE tables: `24`;
- untagged rows with no terminal entry branch: `0`.

## Entry Counts

| entry signature | count |
| --- | ---: |
| `none` | 138 |
| `quotient_separating` | 6 |
| `quotient_separating+flip+subsolution+subsolution_fibre_congruence` | 10 |
| `quotient_separating+subsolution+subsolution_fibre_congruence` | 180 |
| `quotient_separating+subsolution+subsolution_fibre_congruence+observer` | 25 |
| `subsolution` | 60 |
| `subsolution+subsolution_fibre_congruence` | 38 |
| `subsolution+subsolution_fibre_congruence+observer` | 24 |

## Untagged Rows

| entry signature | count |
| --- | ---: |
| `quotient_separating+subsolution+subsolution_fibre_congruence+observer` | 12 |
| `subsolution+subsolution_fibre_congruence+observer` | 12 |

All 24 untagged affine rows have a terminal entry branch: 12 have
point-separating proper quotients plus subsolution and observer entries,
and 12 have subsolution plus observer entries.  Thus the affine
`F_2^2` residual rows do not supply a terminal-branch evader.
The `subsolution_fibre_congruence` marker records the sharper branch
where a proper quotient has crossing-closed fibre blocks.
