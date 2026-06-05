# Size 5/6 Component Stage B Frontier Audit

bounded execution audit, not an exhaustive size 5 or 6 search

## Bounds

- stage_a_max_nodes: `1000`;
- stage_a_max_examples: `3`;
- max_component_solutions: `10000`;
- max_v_examples: `3`;
- max_bucket_permutations: `120`;

## Size Rows

### size 5

- Stage A nodes: `1000`;
- Stage A MF-valid arrays: `1`;
- Stage A canonical arrays: `1`;
- Stage A emitted examples: `1`;
- Stage A truncated: `True`;

#### U example 0

- relation-GAC product: `24883200000` -> `1`;
- relation-GAC locally consistent: `True`;
- component solver global/noninv/accepted: `0` / `0` / `0`;
- component search exact/noninv/accepted/emitted: `0` / `0` / `0` / `0`;
- component search truncated: `False`;
- rigid first failed filters: `()`;

### size 6

- Stage A nodes: `1000`;
- Stage A MF-valid arrays: `1`;
- Stage A canonical arrays: `1`;
- Stage A emitted examples: `1`;
- Stage A truncated: `True`;

#### U example 0

- maximum bucket permutations: `720`;
- Stage B skipped: `maximum bucket permutation count exceeds bound`;

## Conclusion

This run exercises the production component Stage B search on the first bounded Stage A size-5 and size-6 U-frontiers.  It is a smoke/frontier execution artifact: any surviving V completion is passed immediately into the rigid-core filter row, but a truncated Stage A row does not rule out later U arrays.

## Next Prompt

`prompts/gpt55_pro/2026-06-04-everywhere-singular-rigid-core-theory_ask_now.md`.
