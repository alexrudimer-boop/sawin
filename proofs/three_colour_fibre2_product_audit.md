# Three-colour fibre-2 product audit

Date: 2026-05-28

This generated audit enumerates product-permutation local intervals with
three quotient colours and two-point fibres.  Since every fibre label is
either the identity or the transposition, the product cocycle equations
are solved exactly as homogeneous linear equations over `F_2`; this is
not a timeout or word-length search.

The audit is still finite candidate evidence only.  Its role is to look
for explicit local-minimal rows that route to
`product_genuinely_coloured_bottleneck`, not to prove the arbitrary-fibre
product theorem.

## Totals

- product cocycle rows: `322985`.
- primitive/local-minimal rows: `2472`.
- primitive rows with standard known total tags: `1600`.
- router verdicts: `{'product_finite_g_branch': 2472}`.
- product details: `{'direct_coboundary': 288, 'direct_fibre2_affine': 360, 'swapped_coboundary': 84, 'swapped_fibre2_affine': 720, 'swapped_identity_base_cyclic': 1020}`.

## Swapped branch

- product cocycle rows: `322336`.
- primitive/local-minimal rows: `1824`.
- primitive rows with standard known total tags: `1312`.
- router verdicts: `{'product_finite_g_branch': 1824}`.
- product details: `{'swapped_coboundary': 84, 'swapped_fibre2_affine': 720, 'swapped_identity_base_cyclic': 1020}`.

## Direct branch

- product cocycle rows: `649`.
- primitive/local-minimal rows: `648`.
- primitive rows with standard known total tags: `288`.
- router verdicts: `{'product_finite_g_branch': 648}`.
- product details: `{'direct_coboundary': 288, 'direct_fibre2_affine': 360}`.

## Router outcome

No primitive row in this exact product-label corpus routes to
`product_genuinely_coloured_bottleneck` or
`bi_free_universal_corridor_bottleneck`.

## Interpretation

This extends the product search surface in the complementary direction
from the two-colour/fibre-3 audit: more quotient colours, but the
smallest nontrivial fibres.  The result is consistent with the
fibre-size-two affine/semidirect branch being finite-G measurable,
while keeping the global all-`n` product theorem open for arbitrary
fibre sizes and quotient colour sets.
