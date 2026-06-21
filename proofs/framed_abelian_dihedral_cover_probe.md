# Framed abelian dihedral cover probe

In arity 2, the doubled generalized dihedral detector Dih(C_{2e}) covers A_Ce for exponents 2 through 8.  The naive Dih(C_e) detector can fail at even exponents, which is the parity issue addressed in the theorem.

## Scope

- arity: `2`;
- exponents checked: `[2, 3, 4, 5, 6, 7, 8]`;
- proves all-arity theorem: `False`;
- theorem artifact: `proofs/framed_abelian_dihedral_cover_theorem.md`;

## Rows

| e | detector | rotation order | group order | A_Ce sigma order | detector sigma order | kernel contains nonidentity | certified | witness |
| ---: | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| 2 | naive_Dih_Ce | 2 | 4 | 4 | 2 | True | False | (1, 1) |
| 2 | doubled_Dih_C2e | 4 | 8 | 4 | 4 | False | True | None |
| 3 | naive_Dih_Ce | 3 | 6 | 6 | 12 | False | True | None |
| 3 | doubled_Dih_C2e | 6 | 12 | 6 | 12 | False | True | None |
| 4 | naive_Dih_Ce | 4 | 8 | 8 | 4 | True | False | (1, 1, 1, 1) |
| 4 | doubled_Dih_C2e | 8 | 16 | 8 | 8 | False | True | None |
| 5 | naive_Dih_Ce | 5 | 10 | 10 | 20 | False | True | None |
| 5 | doubled_Dih_C2e | 10 | 20 | 10 | 20 | False | True | None |
| 6 | naive_Dih_Ce | 6 | 12 | 12 | 12 | False | True | None |
| 6 | doubled_Dih_C2e | 12 | 24 | 12 | 12 | False | True | None |
| 7 | naive_Dih_Ce | 7 | 14 | 14 | 28 | False | True | None |
| 7 | doubled_Dih_C2e | 14 | 28 | 14 | 28 | False | True | None |
| 8 | naive_Dih_Ce | 8 | 16 | 16 | 8 | True | False | (1, 1, 1, 1, 1, 1, 1, 1) |
| 8 | doubled_Dih_C2e | 16 | 32 | 16 | 16 | False | True | None |

## Boundary

This is a small arity-2 parity probe.  The all-arity proof is the
separate theorem artifact; this probe is only a guardrail against
choosing the naive even-exponent dihedral detector.
