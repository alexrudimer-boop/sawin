# Linear F3 Gap-Corrected Invariant Audit

This generated audit verifies the corrected multi-fibre invariant
for all `32` formal monolith-collision rows in the six-point linear
skew-over-flip family.

## Summary

- source artifact: `proofs\linear_f3_collision_quotient_invariant_audit.json`;
- collision rows: `32`;
- gap-corrected local certificates: `32`;
- local certificate failures: `0`;
- direct invariant arity check: `1..5`;
- direct invariant failures: `0`;
- all claimed checks passed: `True`.

## Checked Identities

For each row, let `alpha` be the visible-label transport in
`zF -> F alpha(z)`, and let `beta` be the visible-label transport in
`Fz -> beta(z)F`.  The audit checks:

```text
beta = alpha^{-1},
S_{alpha^g z} S_{alpha^g w} = S_{alpha^g u} S_{alpha^g v}
  whenever R_Z(z,w)=(u,v),
S_{beta z} T_z = id,
R(F_i,F_j)=(F_i,F_j).
```

It also directly checks the resulting tagged-strand invariant through
arity `5` for positive and negative local
crossings.

## Consequence

The earlier passive-left-list obstruction is repaired by using the
number of collapsed-fibre strands between a visible letter and the
tracked fibre.  If a visible label `z` lies to the left of a tracked
`F`-strand with `g` other `F`-strands between them, the invariant uses
`S_{alpha^g z}` rather than `S_z`.
