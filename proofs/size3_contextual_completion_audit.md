# Size-3 Contextual Completion Audit

This generated audit enumerates every bijective YBE table on a
three-point set and applies the generic two-sided contextual
completion helper.

## Summary

- YBE solutions: `73`;
- classification counts: `{'degenerate_involutive': 7, 'nondegenerate': 66}`;
- maximum contextual quotient size: `18`;
- identity-extension equivariance checked through arity: `5`;
- contextual profile count: `14`;
- failure count: `0`;
- equivariance failure count: `0`;
- all claimed checks passed: `True`.

The corpus has no degenerate non-involutive rows.  It is therefore not
a hard-case corpus, but it verifies that the generic contextual code
agrees with the expected smallest complete classification and finds no
active-lift or identity-extension obstruction.

## Checked Conditions

For every size-three YBE table the audit checks:

```text
forced products have no representative-independence conflicts;
forced partial translations are injective;
lambda_p(D_p)=D_p for every contextual class p;
identity-outside extensions are total permutations;
L_{L_p(q)}=L_p L_q L_p^{-1} for every p,q;
the full forced graph has no local covariance failures;
J_n rho^X = rho^P J_n in every checked arity.
```

## Profiles

| cases | class | M_L | M_R | P | forced | domains | nontriv L |
|---:|---|---:|---:|---:|---:|---|---:|
| 12 | nondegenerate | 2 | 2 | 6 | 18 | [3] | 6 |
| 9 | nondegenerate | 2 | 2 | 6 | 18 | [3] | 0 |
| 9 | nondegenerate | 2 | 2 | 6 | 18 | [3] | 2 |
| 9 | nondegenerate | 2 | 2 | 6 | 18 | [3] | 4 |
| 9 | nondegenerate | 3 | 3 | 9 | 27 | [3] | 9 |
| 6 | nondegenerate | 1 | 1 | 3 | 9 | [3] | 3 |
| 3 | degenerate_involutive | 3 | 3 | 8 | 18 | [1, 2, 7] | 0 |
| 3 | degenerate_involutive | 4 | 4 | 11 | 23 | [1, 2, 9] | 0 |
| 3 | nondegenerate | 1 | 1 | 3 | 9 | [3] | 1 |
| 3 | nondegenerate | 1 | 1 | 3 | 9 | [3] | 2 |
| 3 | nondegenerate | 6 | 6 | 18 | 54 | [3] | 18 |
| 2 | nondegenerate | 3 | 3 | 9 | 27 | [3] | 0 |
| 1 | degenerate_involutive | 4 | 4 | 12 | 9 | [0, 1] | 0 |
| 1 | nondegenerate | 1 | 1 | 3 | 9 | [3] | 0 |
