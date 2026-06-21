# Framed-to-conjugation two-strand probe

The framed route is compatible with the familiar S3 bridge in the smallest arity, but a separate framed-to-conjugation cover lemma is still needed for the finite-group detector route.

## Summary

For B_2, a rack action is determined by the order of sigma_1. The framed C2 detector A_C2 has sigma_1 order 4.  S3^conj has sigma_1 order 12, so K_2(S3^conj) is contained in K_2(A_C2). This is only a two-strand compatibility check; it does not prove that framed detector racks are dominated by finite conjugation racks in all arities.

## Framed rows

| name | size | sigma order | sigma^2 order |
| --- | ---: | ---: | ---: |
| A_C2 | 4 | 4 | 2 |
| T2 x A_C2 | 8 | 4 | 2 |

## Conjugation rows

| name | size | sigma order | sigma^2 order | B2 kernel subset framed C2 kernel |
| --- | ---: | ---: | ---: | --- |
| C2^conj | 2 | 2 | 1 | False |
| S3^conj | 6 | 12 | 6 | True |
| S4^conj | 24 | 24 | 12 | True |

## Boundary

- S3 B2 kernel covers framed C2: `True`;
- proves higher-arity conjugation cover: `False`;
