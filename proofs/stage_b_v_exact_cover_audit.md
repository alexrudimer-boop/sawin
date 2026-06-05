# Stage B V Exact-Cover Audit

Audit the second half of the size 5/6 search pipeline: for a fixed Stage A U-array satisfying multiset factorization, assign V[x,y] by bucket permutations C(u,P)->V(u,P), then enforce V-column singularity, Y2/Y3, and optional non-involutivity.

## Constraints

- V[x,y] lies in the bucket domain V(U[x,y], L_x L_y);
- for every output pair (u,v), exactly one cell has (U,V)=(u,v);
- every V-column x -> V[x,y] is singular;
- Y2 and Y3 hold for all triples;
- optional r^2 != id filter is applied after Y2/Y3;

## Example Rows

### identity_2

- size: `2`;
- source solution YBE: `True`;
- source pair orthogonal: `True`;
- source V-column singular: `True`;
- source Y2/Y3: `True`;
- source noninvolutive: `False`;
- require noninvolutive: `False`;
- actual V recovered: `True`;
- nodes: `6`;
- exact-cover completions: `1`;
- column-singular completions: `1`;
- Y2/Y3 completions: `1`;
- noninvolutive completions: `0`;
- accepted completions: `1`;
- emitted examples: `1`;
- truncated: `False`.

### identity_3

- size: `3`;
- source solution YBE: `True`;
- source pair orthogonal: `True`;
- source V-column singular: `True`;
- source Y2/Y3: `True`;
- source noninvolutive: `False`;
- require noninvolutive: `False`;
- actual V recovered: `True`;
- nodes: `23`;
- exact-cover completions: `1`;
- column-singular completions: `1`;
- Y2/Y3 completions: `1`;
- noninvolutive completions: `0`;
- accepted completions: `1`;
- emitted examples: `1`;
- truncated: `False`.

### size4_affine_type_a

- size: `4`;
- source solution YBE: `True`;
- source pair orthogonal: `True`;
- source V-column singular: `True`;
- source Y2/Y3: `True`;
- source noninvolutive: `True`;
- require noninvolutive: `True`;
- actual V recovered: `True`;
- nodes: `39`;
- exact-cover completions: `2`;
- column-singular completions: `2`;
- Y2/Y3 completions: `2`;
- noninvolutive completions: `1`;
- accepted completions: `1`;
- emitted examples: `1`;
- truncated: `False`.

## Conclusion

The Stage B solver recovers identity completions in sizes 2 and 3, and recovers the known size-4 affine Type A table as the unique non-involutive V-completion of its U among the two bucket-compatible Y2/Y3 completions.  This makes the U-then-V pipeline executable on concrete regression examples.
