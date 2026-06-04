# Rigid Pressure Core Audit

This generated audit records the first falsifiable negative-search
target after the active-factor boundary.  It is not a proof of
Sawin's problem.

## Definition

A rigid pressure core is a nonterminal, quotient-rigid, subsolution-rigid, observer-rigid, transport-split-rigid finite YBE table with actual small-rack prefix pressure.

## Exhaustive Size 3 Corpus

- exhaustive: `True`;
- YBE solution count: `73`;
- terminal survivor count: `0`;
- structural survivor count: `0`;
- rigid pressure core candidates: `0`;
- first failed filter counts: `{'bidegenerate': 66, 'noninvolutive': 7}`.

## Named Representatives

### size4_affine_type_a

- size: `4`;
- tags: `()`;
- bidegenerate: `True`;
- noninvolutive: `True`;
- not rack: `True`;
- not flip-across: `True`;
- quotient rigid: `False`;
- subsolution rigid: `False`;
- observer rigid: `False`;
- no transport-isomorphic split: `True`;
- rack-prefix pressure attempted: `False`;
- rack-prefix pressure found: `None`;
- first failed filter: `quotient_rigid`;
- rigid pressure core candidate: `False`.

### size4_type_b_flip_across

- size: `4`;
- tags: `()`;
- bidegenerate: `True`;
- noninvolutive: `True`;
- not rack: `True`;
- not flip-across: `False`;
- quotient rigid: `False`;
- subsolution rigid: `False`;
- observer rigid: `True`;
- no transport-isomorphic split: `False`;
- rack-prefix pressure attempted: `False`;
- rack-prefix pressure found: `None`;
- first failed filter: `not_flip_across`;
- rigid pressure core candidate: `False`.

### affine_f2_hidden_cyclic_pressure_row

- size: `8`;
- tags: `()`;
- bidegenerate: `True`;
- noninvolutive: `True`;
- not rack: `True`;
- not flip-across: `True`;
- quotient rigid: `None`;
- subsolution rigid: `False`;
- observer rigid: `False`;
- no transport-isomorphic split: `None`;
- rack-prefix pressure attempted: `False`;
- rack-prefix pressure found: `None`;
- first failed filter: `quotient_rigid`;
- rigid pressure core candidate: `False`.

## Conclusion

- representative candidate count: `0`;

No rigid pressure core appears in the exhaustive size-three corpus or in the current named pressure representatives.  The next falsifiable search target is a larger table, preferably size five or a structured affine-linear family, that survives all finite rigidity filters and then exhibits N_{m,n}(X)!=1 for a small rack prefix.
