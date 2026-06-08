# Linear F3 Skew-Over-Flip Completion Audit

This generated audit enumerates six-point linear skew-over-flip
solutions

```text
X={0,1} x F_3
R((a,i),(b,j))=((b,I),(a,J))
(I,J)^T = M_ab (i,j)^T,  M_ab in GL_2(F_3).
```

The audit focuses on the finite hypotheses of the identity-extension
completion lemma: balanced domains and conjugacy covariance.

## Classification

- `GL_2(F_3)` size: `48`;
- tables checked: `5308416`;
- YBE solutions: `1088`;
- classification counts: `{'degenerate_involutive': 96, 'degenerate_noninvolutive': 144, 'nondegenerate_involutive': 32, 'nondegenerate_noninvolutive': 816}`;
- all claimed checks passed: `True`.

## Degenerate Non-Involutive Contextual Summary

| cases | M_L size | M_R size | P size | forced products | domain sizes |
|---:|---:|---:|---:|---:|---|
| 32 | 8 | 8 | 36 | 198 | [3, 4, 15] |
| 24 | 24 | 24 | 108 | 594 | [3, 4, 15] |
| 8 | 4 | 4 | 18 | 99 | [3, 4, 15] |
| 8 | 5 | 5 | 24 | 126 | [3, 4, 18] |
| 8 | 7 | 7 | 30 | 171 | [3, 4, 12, 15] |
| 8 | 8 | 8 | 36 | 198 | [3, 4, 12, 18] |
| 8 | 12 | 12 | 60 | 306 | [3, 4, 21] |
| 8 | 20 | 20 | 84 | 486 | [3, 4, 13] |
| 6 | 12 | 12 | 54 | 297 | [3, 4, 15] |
| 6 | 15 | 15 | 72 | 378 | [3, 4, 18] |
| 6 | 21 | 21 | 90 | 513 | [3, 4, 12, 15] |
| 6 | 24 | 24 | 108 | 594 | [3, 4, 12, 18] |
| 4 | 9 | 9 | 48 | 234 | [3, 4, 30] |
| 4 | 10 | 10 | 42 | 243 | [3, 4, 13] |
| 4 | 12 | 12 | 60 | 306 | [3, 4, 12, 30] |
| 4 | 19 | 19 | 78 | 459 | [3, 4, 12, 13] |

For every one of the 144 degenerate non-involutive rows, the audit
checks:

```text
forced products have no representative-independence conflicts;
forced partial translations are injective;
lambda_p(D_p)=D_p for every p;
identity-outside L_p are total permutations;
L_{L_p(q)}=L_p L_q L_p^{-1} for every p,q.
```

- degenerate non-involutive rows where `M_L` and `M_R` differ as
  sets of maps: `8`;
- contextual failure count: `0`.

## Consequence

The finite totalization obstruction still does not occur in this
six-point ternary-fibre linear family.  This audit does not check
all-arity orbit separation.  It verifies only the finite rack
completion hypotheses from the identity-extension lemma.
