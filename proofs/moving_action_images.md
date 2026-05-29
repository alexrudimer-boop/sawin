# Moving action-image growth

Date: 2026-05-28

This note records the main escape hatch left for a pure-braid law
counterexample.

## Fixed versus moving finite groups

If `w_j` is eventually a law for each fixed finite group, and the same fixed
finite group `H` receives all relevant braid-action generator images, then
`w_j` eventually acts trivially.

In B, however, the braid index grows:

```text
beta_j in B_{q_j},    q_j -> infinity.
```

Even for one fixed finite YBE solution `X`, the action groups

```text
H_j = < rho_{X,q_j}(A_{1,q_j}), ..., rho_{X,q_j}(A_{q_j-1,q_j}) >
```

may grow with `j`.  Eventual laws for each fixed finite group do not
automatically vanish on this moving sequence `H_j`.

## Audit result

`tools/run_moving_image_growth_audit.py` measures `H_j` for small examples and
small braid indices, with explicit tuple-count and subgroup-size caps.  In the
current sample:

- the trivial rack has trivial pure-generator images;
- the one-colour two-point permutation interval has small bounded images;
- the dihedral quandle already has a nonabelian image at braid index `3`,
  which explains why an embedded commutator braid moves it.
- the first size-3 non-rack commutator candidate has the same measured
  `q=2,3` action-image sizes and exponents as the dihedral quandle under the
  current caps: size/exponent `(3,3)` at `q=2` and `(24,12)` at `q=3`.

The dihedral quandle is itself a rack, so this cannot be B.  Its role is only
to demonstrate that law-braid motion is controlled by the generated finite
action image, and that moving image growth is the right quantity to study.
The size-3 candidate is also not B: the measurement stops at `q=3`, and the
commutator longitude is visible to `S3`.

The generated report is `proofs/moving_image_growth_audit.json`.
