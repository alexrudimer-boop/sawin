# Stage B Bucket-CSP Audit

Record the bucket-domain CSP precheck used before full Stage B backtracking: Hall all-different consistency per output u and local support for every Y2/Y3 triple.  Also record the exact generalized arc-consistency propagation over bucket variables.

## Checks

- domain-size profile for variables W_xy=V[x,y];
- Hall all-different test on cells with fixed U[x,y]=u;
- Y2/Y3 local support test for each triple (x,y,z);
- locally_consistent iff Hall succeeds and no Y2/Y3 triple is unsupported;
- exact GAC value deletion using dynamic Y2/Y3 implication supports;
- singleton GAC domains are extracted and directly verified against Y2/Y3;

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

## Conclusion

The current examples all pass local bucket-CSP consistency.  The profile still distinguishes their domain geometry: identity has three 3-cell buckets, the dihedral rack has nine forced cells, and affine Type A has eight 2-cell buckets.  Exact GAC forces the dihedral rack table and preserves all values needed for the known affine Type A completion.  This is the next precheck layer before full d=5,6 Stage B search.

## Next Prompt

`prompts/gpt55_pro/2026-06-04-gac-frontier-next-step_ask_now.md`.
