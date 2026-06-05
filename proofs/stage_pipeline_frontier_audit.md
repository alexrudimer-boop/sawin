# Stage Pipeline Frontier Audit

Connect row-catalogue Stage A enumeration to bucket-CSP, Stage B exact cover, and the existing rigid-pressure filters.  This is a bounded frontier audit, not an exhaustive size 4, 5, or 6 search.

## Stage A Frontiers

### exact_size_3

- size: `3`;
- nodes: `772`;
- MF-valid arrays: `1`;
- canonical arrays: `1`;
- emitted examples: `1`;
- truncated: `False`.

### budget_size_4

- size: `4`;
- nodes: `50000`;
- MF-valid arrays: `1`;
- canonical arrays: `1`;
- emitted examples: `1`;
- truncated: `True`.

## Pipeline Rows

### row_exact_size3_u0

- size: `3`;
- require noninvolutive: `True`;
- bucket count: `3`;
- maximum domain size: `3`;
- locally consistent: `True`;
- GAC domain mass: `27` -> `27`;
- GAC forced variables: `0`;
- GAC locally consistent: `True`;
- bucket-permutation product: `216` -> `1`;
- bucket-permutation locally consistent: `True`;
- relation-GAC product: `216` -> `1`;
- relation-GAC deletions / locally consistent: `15` / `True`;
- bucket hypergraph components / largest: `0` / `0`;
- bucket relation patterns YBE/column/noninv: `27` / `3` / `0`;
- stabilizer branch order/component orbits/child reps: `0` / `0` / `0`;
- component solver global/noninv/accepted: `0` / `0` / `0`;
- component Stage B exact/noninv/accepted/emitted: `0` / `0` / `0` / `0`;
- Stage B accepted completions: `0`;
- Stage B emitted completions: `0`;
- Stage B truncated: `False`;
- GAC Stage B nodes: `12`;
- GAC Stage B accepted completions: `0`;
- GAC Stage B truncated: `False`;
- bucket Stage B nodes: `1`;
- bucket Stage B accepted completions: `0`;
- bucket Stage B Aut(U) / canonical rejections: `6` / `0`;
- bucket Stage B stabilizer branches / child reductions: `0` / `0`;
- bucket Stage B truncated: `False`;
- rigid first failed filters: `()`.

### row_budget_size4_u0

- size: `4`;
- require noninvolutive: `True`;
- bucket count: `4`;
- maximum domain size: `4`;
- locally consistent: `True`;
- GAC domain mass: `64` -> `64`;
- GAC forced variables: `0`;
- GAC locally consistent: `True`;
- bucket-permutation product: `331776` -> `1`;
- bucket-permutation locally consistent: `True`;
- relation-GAC product: `331776` -> `1`;
- relation-GAC deletions / locally consistent: `92` / `True`;
- bucket hypergraph components / largest: `0` / `0`;
- bucket relation patterns YBE/column/noninv: `64` / `4` / `0`;
- stabilizer branch order/component orbits/child reps: `0` / `0` / `0`;
- component solver global/noninv/accepted: `0` / `0` / `0`;
- component Stage B exact/noninv/accepted/emitted: `0` / `0` / `0` / `0`;
- Stage B accepted completions: `0`;
- Stage B emitted completions: `0`;
- Stage B truncated: `False`;
- GAC Stage B nodes: `30`;
- GAC Stage B accepted completions: `0`;
- GAC Stage B truncated: `False`;
- bucket Stage B nodes: `1`;
- bucket Stage B accepted completions: `0`;
- bucket Stage B Aut(U) / canonical rejections: `24` / `0`;
- bucket Stage B stabilizer branches / child reductions: `0` / `0`;
- bucket Stage B truncated: `False`;
- rigid first failed filters: `()`.

### known_affine_type_a

- size: `4`;
- require noninvolutive: `True`;
- bucket count: `8`;
- maximum domain size: `2`;
- locally consistent: `True`;
- GAC domain mass: `32` -> `32`;
- GAC forced variables: `0`;
- GAC locally consistent: `True`;
- bucket-permutation product: `256` -> `256`;
- bucket-permutation locally consistent: `True`;
- relation-GAC product: `256` -> `256`;
- relation-GAC deletions / locally consistent: `0` / `True`;
- bucket hypergraph components / largest: `1` / `8`;
- bucket relation patterns YBE/column/noninv: `156` / `16` / `24`;
- stabilizer branch order/component orbits/child reps: `2` / `1` / `2`;
- component solver global/noninv/accepted: `2` / `1` / `1`;
- component Stage B exact/noninv/accepted/emitted: `2` / `1` / `1` / `1`;
- Stage B accepted completions: `1`;
- Stage B emitted completions: `1`;
- Stage B truncated: `False`;
- GAC Stage B nodes: `3`;
- GAC Stage B accepted completions: `1`;
- GAC Stage B truncated: `False`;
- bucket Stage B nodes: `3`;
- bucket Stage B accepted completions: `1`;
- bucket Stage B Aut(U) / canonical rejections: `2` / `0`;
- bucket Stage B stabilizer branches / child reductions: `1` / `0`;
- bucket Stage B truncated: `False`;
- rigid first failed filters: `('quotient_rigid',)`.

## Conclusion

The exact d=3 row-catalogue frontier has no non-involutive Stage B completion.  The first d=4 budgeted row-catalogue frontier is also identity-type and has no non-involutive completion.  The named affine Type A regression still passes the same pipeline and is rejected by the rigid-core filters at quotient rigidity.
