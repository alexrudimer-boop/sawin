# Size-four degenerate non-involutive probe

This note records the current computational evidence for the first genuinely
degenerate non-involutive finite solutions.  It is not yet an exhaustive
classification proof: the 40 size-four tables and the forcing script that found
them still need to be committed before the census can be treated as reproducible
inside this repository.

## Reported forced census

The targeted size-four probe forced a left-degeneracy pattern, for example
`f_0(0)=f_0(1)`, and searched for bijective set-theoretic YBE tables.  In that
branch it found 40 non-involutive degenerate solutions.  All 40 were
bi-degenerate, so they are outside the left-nondegenerate derived-rack branch
and outside the easy involutive branch.

The 40 reported examples split into two observed types.

- Type A: 16 solutions have the same braid kernels as the two-element cyclic
  rack

  ```
  R(a,b)=(1-b,a).
  ```

  The reported braid image orders agree with this rack through the checked
  range.  In particular the rack image orders for `n=2,3,4,5` are
  `4,24,192,1920`; the local audit also records the rack image order
  `23040` at `n=6`.  Exact domination was reported through `n=6`.
  A concrete affine `F_2^2` Type A model and its all-arity fibrewise conjugacy
  to this cyclic rack action are recorded in
  `proofs/affine_f2_cyclic_rack_equivalence.md`.

- Type B: 24 solutions have the same observed braid image orders as the
  three-element rack with left translations

  ```
  L_0=L_1=id,  L_2=(01).
  ```

  The reported image orders for `n=2,3,4,5` are
  `4,48,1536,122880`, and exact domination was reported through `n=4`.  This
  same size-three rack also dominates all 40 reported examples through the
  checked level `n=4`.

All 40 reported examples have crossing order four, so they are not involutive.
The reported Type B description is a twisted union of the trivial solution on
`{0,1}` with the permutation solution `R(a,b)=(b,1-a)` on `{2,3}`.
The general flip-across twisted-union closure theorem is now recorded in
`proofs/flip_twisted_union_domination.md`: if finite racks dominate two
component solutions, then the flip-across disjoint union of those racks
dominates the flip-across disjoint union of the component solutions.

## Local rack-image audit

The script

```
python tools/audit_size4_degenerate_probe.py
```

checks the two small rack image sequences above using the repository's braid
action conventions.  It deliberately does not assert the missing census: it
only verifies the proposed rack-side image orders without constructing a full
finite group multiplication table for the `122880` element size-three image.

This gives a reproducible anchor for the mechanism reported by the probe:
whenever the claimed domination maps have been checked in fixed degree, equality
of image orders forces equality of braid kernels in that degree.

## Status for Sawin's question

The evidence removes the size-three ambiguity.  Degenerate non-involutive
solutions do exist at size four, but the reported examples are not
counterexamples to finite rack domination.  They appear to be braid-equivalent
to small racks, which is stronger than domination.

The next useful theorem target is therefore not another detector for these
tables, but an all-arity structural proof of the observed mechanism:

```
Type A solutions are represented by the affine F_2^2 cyclic-rack-equivalent
model, up to the remaining census equivalence checks.
Type B twisted-union solutions are dominated by the flip-across union of the
component rack detectors; in the observed size-four case this is the rack
L_0=L_1=id, L_2=(01).
```

The Type B proof is now supplied by the flip-across union theorem.  The Type A
affine model is supplied by the cyclic-rack coordinate theorem.  A complete
size-four classification still requires committing the forced-search script and
the 40 tables, or replacing the search by a theoretical classification of the
degenerate non-involutive size-four cases.

The terminal-branch transport audit now distinguishes the two mechanisms
without using braid-image orders.  For the Type B flip-across model, the
subsolution-fibre mixed rows are swapped-product-like and the one-coordinate
mixed transports are isomorphisms of the internal block subsolutions.  For the
Type A affine model, the same mixed rows are swapped-product-like bijections
but not subsolution isomorphisms.  Thus Type A genuinely needs its separate
parity/fibre gauge, while Type B is in the literal flip-across transport
branch.
