# Size-3 candidate details

Date: 2026-05-28

The bounded size-3 scan found non-rack bijective YBE tables moved by the
embedded commutator law braid in `B_3`.

This is not a counterexample B:

- the commutator word `[x,y]` is only a law for abelian finite groups, not for
  all finite groups;
- the search is bounded to a deterministic prefix of size-3 bijective tables;
- the candidate YBE tables are given by explicit finite tables, not by a
  symbolic family with `q_j -> infinity`.

However, these candidates are useful because they show that non-rack finite
YBE actions can see non-power pure-braid law embeddings.  The remaining
question is whether there exists a fixed finite non-rack YBE solution and a
sequence of genuine finite-group laws whose pure-braid embeddings remain
nontrivial in the moving action images.

The generated report is `proofs/size3_candidate_detail.json`.

First returned candidate, in the row order
`(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)`, has table

```text
(0,0) -> (0,0)
(0,1) -> (1,0)
(0,2) -> (2,0)
(1,0) -> (2,2)
(1,1) -> (0,2)
(1,2) -> (1,2)
(2,0) -> (1,1)
(2,1) -> (2,1)
(2,2) -> (0,1)
```

The embedded commutator braid is
`(2,1,1,-2,2,2,2,-1,-1,-2,-2,-2)` in `B_3`; it sends
`(0,0,1)` to `(1,1,2)`.  Its action on all `3^3` tuples has support 24 and
order 4.

The same commutator longitude is invisible on the abelian test groups
`C2`, `C3`, and `C5`, but visible on `S3`.  Thus it proves only that the
pure-braid law embedding can expose non-rack motion; it does not begin to meet
the normalized obstruction requirement for defeating every finite group `G`.

The candidate is also not a new structural branch.  The audit detects it as
affine over `Z/3`:

```text
R(x,y) = (2x + y, 2x) mod 3 = (y - x, -x) mod 3.
```

The other returned size-3 commutator candidates are affine over the same
cyclic set as well.  This places the bounded examples inside the already
bookkept affine branch rather than inside the arbitrary-fibre master gap.
