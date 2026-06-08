# Binary Skew-Over-Flip Contextual Family Audit

This generated audit enumerates all binary skew-over-flip four-point
solutions

```text
R((a,i),(b,j)) = ((b,I_ab(i,j)), (a,J_ab(i,j)))
```

where each fibre map on `{0,1}^2` is an arbitrary permutation.

## Classification

- tables checked: `331776`;
- YBE solutions: `520`;
- classification counts: `{'degenerate_involutive': 64, 'degenerate_noninvolutive': 72, 'nondegenerate': 384}`;
- all claimed checks passed: `True`.

## Degenerate Non-Involutive Contextual Summary

| cases | M_L size | M_R size | P size | forced products | domain sizes |
|---:|---:|---:|---:|---:|---|
| 36 | 6 | 6 | 20 | 72 | [2, 3, 8] |
| 12 | 5 | 5 | 16 | 60 | [2, 3, 7] |
| 6 | 3 | 3 | 10 | 36 | [2, 3, 8] |
| 6 | 4 | 4 | 14 | 48 | [2, 3, 10] |
| 6 | 5 | 5 | 16 | 60 | [2, 3, 6, 8] |
| 6 | 6 | 6 | 20 | 72 | [2, 3, 6, 10] |

For every degenerate non-involutive row, the audit checks that
`M_L` and `M_R` have the same underlying maps, the contextual quotient
has no forced-product conflicts, every forced partial left translation
is injective, and the identity fill is a rack made from commuting
involutions satisfying `L_{L_p(q)}=L_q`.

- contextual failure count: `0`.

## Consequence

The contextual totalization obstruction does not occur in this full
nearest four-point family.  The remaining search target is either a
larger finite YBE-origin contextual partial rack whose forced
translations cannot be completed by this commuting-involution fill, or
a proof that YBE-origin contextual partial translations always admit a
finite completion of this kind.
