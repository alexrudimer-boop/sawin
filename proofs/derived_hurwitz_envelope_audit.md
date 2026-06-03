# Derived Hurwitz envelope audit

Date: 2026-06-03

This generated audit checks finite rows for the route-(1)
guitar-derived Hurwitz envelope.  It records one nondegenerate
row where the derived rack envelope works and prefix bookkeeping
is visibly needed, and one degenerate row where the derived
operation is not total.

## Rows

### nondegenerate_prefix_witness

- element count: `2`;
- left nondegenerate: `True`;
- right nondegenerate: `True`;
- nondegenerate: `True`;
- derived operation total: `True`;
- derived rack YBE: `True`;
- two-strand guitar conjugacy: `True`;
- three-strand guitar conjugacy: `True`;
- unaugmented interior forgetting matches: `False`;
- prefix left-group order: `2`;
- preimage failure count: `0`;
- proves nondegenerate derived-envelope prefix: `True`;
- detects degenerate derived-operation failure: `False`.

### degenerate_identity_failure

- element count: `2`;
- left nondegenerate: `False`;
- right nondegenerate: `False`;
- nondegenerate: `False`;
- derived operation total: `False`;
- derived rack YBE: `False`;
- two-strand guitar conjugacy: `False`;
- three-strand guitar conjugacy: `False`;
- unaugmented interior forgetting matches: `None`;
- prefix left-group order: `None`;
- preimage failure count: `4`;
- proves nondegenerate derived-envelope prefix: `False`;
- detects degenerate derived-operation failure: `True`.

Recorded preimage failures:

- kind `multiple_preimages_same_candidate`, derived label `0`, original label `0`, preimages `(0, 1)`.
- kind `missing_preimage`, derived label `0`, original label `1`, preimages `()`.
- kind `missing_preimage`, derived label `1`, original label `0`, preimages `()`.
- kind `multiple_preimages_same_candidate`, derived label `1`, original label `1`, preimages `(0, 1)`.

## Meaning

For nondegenerate rows, the route object is not the raw
`lambda/rho` operator label.  It is the guitar-conjugated
derived rack envelope, augmented by the finite left-prefix
group for point-forgetting bookkeeping.  For genuinely
left-degenerate rows, the first finite obstruction is that
the derived operation may not be a total function.
