# Stage B Bucket-CSP Audit

Record the bucket-domain CSP precheck used before full Stage B backtracking: Hall all-different consistency per output u and local support for every Y2/Y3 triple.

## Checks

- domain-size profile for variables W_xy=V[x,y];
- Hall all-different test on cells with fixed U[x,y]=u;
- Y2/Y3 local support test for each triple (x,y,z);
- locally_consistent iff Hall succeeds and no Y2/Y3 triple is unsupported;

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

## Conclusion

The current examples all pass local bucket-CSP consistency.  The profile still distinguishes their domain geometry: identity has three 3-cell buckets, the dihedral rack has nine forced cells, and affine Type A has eight 2-cell buckets.  This is the next precheck layer before full d=5,6 Stage B search.

## Next Prompt

`prompts/gpt55_pro/2026-06-04-stage-b-bucket-csp_ask_now.md`.
