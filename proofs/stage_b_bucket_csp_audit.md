# Stage B Bucket-CSP Audit

Record the bucket-domain CSP precheck used before full Stage B backtracking: Hall all-different consistency per output u and local support for every Y2/Y3 triple.  Also record the exact generalized arc-consistency propagation over bucket variables.

## Checks

- domain-size profile for variables W_xy=V[x,y];
- Hall all-different test on cells with fixed U[x,y]=u;
- Y2/Y3 local support test for each triple (x,y,z);
- locally_consistent iff Hall succeeds and no Y2/Y3 triple is unsupported;
- exact GAC value deletion using dynamic Y2/Y3 implication supports;
- singleton GAC domains are extracted and directly verified against Y2/Y3;
- GAC-assisted Stage B branching for column-singular non-involutive completions;
- early column-singularity feasibility rejection when a column has no possible duplicate value;
- bucket-permutation GAC over whole bijections C(u,P)->B(u,P);
- bucket-permutation branching for column-singular non-involutive completions;
- Aut(U)-aware canonical state rejection for bucket-permutation branches;
- exact bucket-domain column-singularity feasibility before branching;
- exact bucket-domain non-involutivity feasibility before branching;
- remaining bucket-constraint hypergraph and connected components after bucket-GAC;

## Example Rows

### identity_3

- size: `3`;
- source solution YBE: `True`;
- variable count: `9`;
- bucket count: `3`;
- domain size counts: `((3, 9),)`;
- forced variables: `0`;
- maximum domain size: `3`;
- Hall all-different ok: `True`;
- unsupported Y2/Y3 triples: `0`;
- locally consistent: `True`.
- GAC final domain size counts: `((3, 9),)`;
- GAC initial/final domain mass: `27` / `27`;
- GAC deletions, Hall/Y2-Y3: `0` / `0`;
- GAC forced variables: `0`;
- GAC all singleton: `False`;
- GAC singleton Y2/Y3 verified: `None`;
- GAC locally consistent: `True`.
- GAC non-involutive search nodes / accepted: `12` / `0`;
- GAC non-involutive search truncated: `False`.
- bucket-permutation domain product: `216` -> `1`;
- bucket-permutation domain size counts: `((1, 3),)`;
- bucket-permutation singleton/noninvolutive: `True` / `False`;
- bucket-domain column-singularity possible: `True`;
- bucket-domain non-involutivity possible: `False`;
- bucket hypergraph components / largest: `0` / `0`;
- bucket relation patterns YBE/column/noninv: `27` / `3` / `0`;
- bucket hypergraph edge counts YBE/column/involutive: `0` / `0` / `0`;
- bucket hypergraph column/noninv feasible: `True` / `False`;
- bucket-permutation search nodes / accepted: `1` / `0`;
- bucket-permutation Aut(U) / canonical rejections: `6` / `0`;
- bucket-permutation search truncated: `False`.

### dihedral_rack_3

- size: `3`;
- source solution YBE: `True`;
- variable count: `9`;
- bucket count: `9`;
- domain size counts: `((1, 9),)`;
- forced variables: `9`;
- maximum domain size: `1`;
- Hall all-different ok: `True`;
- unsupported Y2/Y3 triples: `0`;
- locally consistent: `True`.
- GAC final domain size counts: `((1, 9),)`;
- GAC initial/final domain mass: `9` / `9`;
- GAC deletions, Hall/Y2-Y3: `0` / `0`;
- GAC forced variables: `9`;
- GAC all singleton: `True`;
- GAC singleton Y2/Y3 verified: `True`;
- GAC locally consistent: `True`.
- GAC non-involutive search nodes / accepted: `1` / `0`;
- GAC non-involutive search truncated: `False`.
- bucket-permutation domain product: `1` -> `1`;
- bucket-permutation domain size counts: `((1, 9),)`;
- bucket-permutation singleton/noninvolutive: `True` / `True`;
- bucket-domain column-singularity possible: `False`;
- bucket-domain non-involutivity possible: `True`;
- bucket hypergraph components / largest: `0` / `0`;
- bucket relation patterns YBE/column/noninv: `27` / `0` / `6`;
- bucket hypergraph edge counts YBE/column/involutive: `0` / `0` / `0`;
- bucket hypergraph column/noninv feasible: `False` / `True`;
- bucket-permutation search nodes / accepted: `1` / `0`;
- bucket-permutation Aut(U) / canonical rejections: `6` / `0`;
- bucket-permutation search truncated: `False`.

### size4_affine_type_a

- size: `4`;
- source solution YBE: `True`;
- variable count: `16`;
- bucket count: `8`;
- domain size counts: `((2, 16),)`;
- forced variables: `0`;
- maximum domain size: `2`;
- Hall all-different ok: `True`;
- unsupported Y2/Y3 triples: `0`;
- locally consistent: `True`.
- GAC final domain size counts: `((2, 16),)`;
- GAC initial/final domain mass: `32` / `32`;
- GAC deletions, Hall/Y2-Y3: `0` / `0`;
- GAC forced variables: `0`;
- GAC all singleton: `False`;
- GAC singleton Y2/Y3 verified: `None`;
- GAC locally consistent: `True`.
- GAC non-involutive search nodes / accepted: `3` / `1`;
- GAC non-involutive search truncated: `False`.
- bucket-permutation domain product: `256` -> `256`;
- bucket-permutation domain size counts: `((2, 8),)`;
- bucket-permutation singleton/noninvolutive: `False` / `None`;
- bucket-domain column-singularity possible: `True`;
- bucket-domain non-involutivity possible: `True`;
- bucket hypergraph components / largest: `1` / `8`;
- bucket relation patterns YBE/column/noninv: `156` / `16` / `24`;
- bucket hypergraph edge counts YBE/column/involutive: `19` / `4` / `4`;
- bucket hypergraph column/noninv feasible: `True` / `True`;
- bucket-permutation search nodes / accepted: `3` / `1`;
- bucket-permutation Aut(U) / canonical rejections: `2` / `0`;
- bucket-permutation search truncated: `False`.

## Conclusion

The current examples all pass local bucket-CSP consistency.  The profile still distinguishes their domain geometry: identity has three 3-cell buckets, the dihedral rack has nine forced cells, and affine Type A has eight 2-cell buckets.  Exact GAC forces the dihedral rack table and preserves all values needed for the known affine Type A completion.  GAC-assisted branching recovers the unique non-involutive affine Type A completion in three search nodes.  The branch search also rejects any non-singleton state where some V-column can no longer become singular.  This is now refined by bucket-permutation GAC, which preserves whole bucket-bijection correlations and forces the identity example without cell-level branching.  The bucket search records Aut(U) and rejects noncanonical branch states under that stabilizer.  It also uses exact bucket-domain column feasibility, which rejects the dihedral rack regression as not column-singular, and exact non-involutivity feasibility, which rejects identity-type states as forced involutive.  The remaining hypergraph audit shows whether unresolved bucket choices decompose into independent components before full d=5,6 Stage B search.

## Next Prompt

`prompts/gpt55_pro/2026-06-04-stabilizer-component-solver-next-step_ask_now.md`.
