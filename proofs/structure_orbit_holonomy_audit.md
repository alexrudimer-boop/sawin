# Structure-orbit holonomy audit

Date: 2026-05-28

This audit refines the structure-orbit reduction.  Degree-`n`
structure classes are exactly braid orbits in `X^n`; the new helper
`structure_orbit_holonomy_summary()` computes the finite braid-action
group on each orbit separately.  The companion helper
`structure_orbit_factorization_summary()` computes the global fixed-degree
image and compares its projections with the orbit-holonomy factors.
This is still fixed-`n` data, not an all-`n` proof.

## Diagnostic rows

### identity_2

- `n=2`: orbits `4`,
  truncated orbits `0`,
  max closed group size `1`.
  Orbit rows `(size, group size, exponent, projection size)`: `[(1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1)]`.
  Global image `(size, exponent, truncated)=(1, 1, False)`; product bound `1`; projection sizes `(1, 1, 1, 1)`; projections match orbit groups `True`.
- `n=3`: orbits `8`,
  truncated orbits `0`,
  max closed group size `1`.
  Orbit rows `(size, group size, exponent, projection size)`: `[(1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1)]`.
  Global image `(size, exponent, truncated)=(1, 1, False)`; product bound `1`; projection sizes `(1, 1, 1, 1, 1, 1, 1, 1)`; projections match orbit groups `True`.
- `n=4`: orbits `16`,
  truncated orbits `0`,
  max closed group size `1`.
  Orbit rows `(size, group size, exponent, projection size)`: `[(1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1)]`.
  Global image `(size, exponent, truncated)=(1, 1, False)`; product bound `1`; projection sizes `(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)`; projections match orbit groups `True`.

### trivial_rack_2

- `n=2`: orbits `3`,
  truncated orbits `0`,
  max closed group size `2`.
  Orbit rows `(size, group size, exponent, projection size)`: `[(1, 1, 1, 1), (1, 1, 1, 1), (2, 2, 2, 2)]`.
  Global image `(size, exponent, truncated)=(2, 2, False)`; product bound `2`; projection sizes `(1, 1, 2)`; projections match orbit groups `True`.
- `n=3`: orbits `4`,
  truncated orbits `0`,
  max closed group size `6`.
  Orbit rows `(size, group size, exponent, projection size)`: `[(1, 1, 1, 1), (1, 1, 1, 1), (3, 6, 6, 6), (3, 6, 6, 6)]`.
  Global image `(size, exponent, truncated)=(6, 6, False)`; product bound `36`; projection sizes `(1, 1, 6, 6)`; projections match orbit groups `True`.
- `n=4`: orbits `5`,
  truncated orbits `0`,
  max closed group size `24`.
  Orbit rows `(size, group size, exponent, projection size)`: `[(1, 1, 1, 1), (1, 1, 1, 1), (4, 24, 12, 24), (4, 24, 12, 24), (6, 24, 12, 24)]`.
  Global image `(size, exponent, truncated)=(24, 12, False)`; product bound `13824`; projection sizes `(1, 1, 24, 24, 24)`; projections match orbit groups `True`.

### dihedral_quandle_3

- `n=2`: orbits `5`,
  truncated orbits `0`,
  max closed group size `3`.
  Orbit rows `(size, group size, exponent, projection size)`: `[(1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (3, 3, 3, 3), (3, 3, 3, 3)]`.
  Global image `(size, exponent, truncated)=(3, 3, False)`; product bound `9`; projection sizes `(1, 1, 1, 3, 3)`; projections match orbit groups `True`.
- `n=3`: orbits `6`,
  truncated orbits `0`,
  max closed group size `24`.
  Orbit rows `(size, group size, exponent, projection size)`: `[(1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (8, 24, 12, 24), (8, 24, 12, 24), (8, 24, 12, 24)]`.
  Global image `(size, exponent, truncated)=(24, 12, False)`; product bound `13824`; projection sizes `(1, 1, 1, 24, 24, 24)`; projections match orbit groups `True`.
- `n=4`: orbits `6`,
  truncated orbits `0`,
  max closed group size `648`.
  Orbit rows `(size, group size, exponent, projection size)`: `[(1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (24, 216, 12, 216), (27, 648, 36, 648), (27, 648, 36, 648)]`.
  Global image `(size, exponent, truncated)=(648, 36, False)`; product bound `90699264`; projection sizes `(1, 1, 1, 216, 648, 648)`; projections match orbit groups `True`.
- `n=5`: orbits `6`,
  truncated orbits `3`,
  max closed group size `1`.
  Orbit rows `(size, group size, exponent, projection size)`: `[(1, 1, 1, None), (1, 1, 1, None), (1, 1, 1, None), (80, None, None, None), (80, None, None, None), (80, None, None, None)]`.
  Global image `(size, exponent, truncated)=(None, None, True)`; product bound `None`; projection sizes `(None, None, None, None, None, None)`; projections match orbit groups `None`.

### size3_commutator_candidate

- `n=2`: orbits `5`,
  truncated orbits `0`,
  max closed group size `3`.
  Orbit rows `(size, group size, exponent, projection size)`: `[(1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (3, 3, 3, 3), (3, 3, 3, 3)]`.
  Global image `(size, exponent, truncated)=(3, 3, False)`; product bound `9`; projection sizes `(1, 1, 1, 3, 3)`; projections match orbit groups `True`.
- `n=3`: orbits `6`,
  truncated orbits `0`,
  max closed group size `24`.
  Orbit rows `(size, group size, exponent, projection size)`: `[(1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (8, 24, 12, 24), (8, 24, 12, 24), (8, 24, 12, 24)]`.
  Global image `(size, exponent, truncated)=(24, 12, False)`; product bound `13824`; projection sizes `(1, 1, 1, 24, 24, 24)`; projections match orbit groups `True`.
- `n=4`: orbits `6`,
  truncated orbits `0`,
  max closed group size `648`.
  Orbit rows `(size, group size, exponent, projection size)`: `[(1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (24, 216, 12, 216), (27, 648, 36, 648), (27, 648, 36, 648)]`.
  Global image `(size, exponent, truncated)=(648, 36, False)`; product bound `90699264`; projection sizes `(1, 1, 1, 216, 648, 648)`; projections match orbit groups `True`.
- `n=5`: orbits `6`,
  truncated orbits `3`,
  max closed group size `1`.
  Orbit rows `(size, group size, exponent, projection size)`: `[(1, 1, 1, None), (1, 1, 1, None), (1, 1, 1, None), (80, None, None, None), (80, None, None, None), (80, None, None, None)]`.
  Global image `(size, exponent, truncated)=(None, None, True)`; product bound `None`; projection sizes `(None, None, None, None, None, None)`; projections match orbit groups `None`.

## Consequence

The size-3 affine commutator diagnostic and the dihedral quandle have
the same orbit-holonomy profile through the audited range.  At
`n=4`, the nontrivial orbit groups have sizes `216`, `648`, and
`648`, with exponents `12`, `36`, and `36`; the global image has
size `648` and exponent `36`, while the product of orbit-holonomy
factor sizes is `90699264`.  Thus the global image is a correlated
subdirect subgroup of the orbit factors, not the whole product.
At `n=5`, the three large orbit closures exceed the configured
group-size cap.  This explains the moving-image warning in
orbit-local terms: a normalized-law B candidate must keep a word
nontrivial in one of these moving structure-orbit holonomy groups
and in the correlated global image while becoming invisible to every
fixed finite-G longitude detector.

No truncated row is used as theorem evidence.  The rows only identify
where the all-`n` proof or a B construction must control internal
structure-orbit holonomy.
