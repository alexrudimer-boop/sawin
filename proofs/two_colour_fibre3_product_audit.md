# Two-colour fibre-3 product audit

Date: 2026-05-28

This audit enumerates the swapped and direct product-permutation
branches with two quotient colours and three fibre points over each
colour.  It is an exact candidate-discovery audit for this structured
branch, not a finite-search proof of the master theorem.

The enumerated swapped local maps have the form

```text
T_{a,b}(x,y) = (L_{a,b}(y), R_{a,b}(x))
```

and the direct maps have the form

```text
T_{a,b}(x,y) = (L_{a,b}(x), R_{a,b}(y)).
```

All `L` and `R` labels lie in `S_3`, over each of the five two-point
bijective YBE quotient colour tables.

## Swapped Totals

- valid left-label assignments: `1800`;
- right-label assignments checked: `2332800`;
- swapped product cocycle solutions: `18612`;
- primitive/local-minimal product rows: `2064`;
- known-branch primitive rows: `1740`;
- identity-base cyclic rows: `324`;
- unknown primitive rows: `0`.
- router verdicts: `{'product_finite_g_branch': 2064}`.
- product details: `{'swapped_genuinely_coloured_known_total': 576, 'swapped_identity_base_cyclic': 1488}`.

## Direct Totals

- valid left-label assignments: `25`;
- right-label assignments checked: `32400`;
- direct product cocycle solutions: `85`;
- primitive/local-minimal product rows: `24`;
- known-branch primitive rows: `24`;
- unknown primitive rows: `0`.
- router verdicts: `{'product_finite_g_branch': 24}`.
- product details: `{'direct_genuinely_coloured_known_total': 24}`.

## By Base

### base 0

- base tags: `involutive+identity_table+affine_cyclic`;
- identity base: `True`;
- swapped cocycle solutions: `1764`;
- swapped primitive rows: `1488`;
- swapped unknown primitive rows: `0`;
- swapped router verdicts: `{'product_finite_g_branch': 1488}`;
- direct cocycle solutions: `1`;
- direct primitive rows: `0`;
- direct unknown primitive rows: `0`.
- direct router verdicts: `{}`.

### base 1

- base tags: `rack_type+involutive+permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate+affine_cyclic`;
- identity base: `False`;
- swapped cocycle solutions: `15876`;
- swapped primitive rows: `0`;
- swapped unknown primitive rows: `0`;
- swapped router verdicts: `{}`;
- direct cocycle solutions: `36`;
- direct primitive rows: `12`;
- direct unknown primitive rows: `0`.
- direct router verdicts: `{'product_finite_g_branch': 12}`.

### base 2

- base tags: `permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate+affine_cyclic`;
- identity base: `False`;
- swapped cocycle solutions: `108`;
- swapped primitive rows: `48`;
- swapped unknown primitive rows: `0`;
- swapped router verdicts: `{'product_finite_g_branch': 48}`;
- direct cocycle solutions: `6`;
- direct primitive rows: `0`;
- direct unknown primitive rows: `0`.
- direct router verdicts: `{}`.

### base 3

- base tags: `rack_type+permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate+affine_cyclic`;
- identity base: `False`;
- swapped cocycle solutions: `108`;
- swapped primitive rows: `48`;
- swapped unknown primitive rows: `0`;
- swapped router verdicts: `{'product_finite_g_branch': 48}`;
- direct cocycle solutions: `6`;
- direct primitive rows: `0`;
- direct unknown primitive rows: `0`.
- direct router verdicts: `{}`.

### base 4

- base tags: `involutive+permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate+affine_cyclic`;
- identity base: `False`;
- swapped cocycle solutions: `756`;
- swapped primitive rows: `480`;
- swapped unknown primitive rows: `0`;
- swapped router verdicts: `{'product_finite_g_branch': 480}`;
- direct cocycle solutions: `36`;
- direct primitive rows: `12`;
- direct unknown primitive rows: `0`.
- direct router verdicts: `{'product_finite_g_branch': 12}`.

## Consequence

Within this exact two-colour/fibre-3 swapped product search, the only
primitive row outside the standard branch tags is the identity-base
cyclic case.  That case is covered by the symbolic identity-base
product lemma and the cyclic pairwise-linking detector.  The
non-identity two-colour bases contribute primitive rows only in
known finite-G-measurable tags such as nondegenerate, rack-type,
permutation-form, or involutive.

The direct search has nontrivial direct product holonomy in the full
cocycle space, so direct holonomy is not automatically coboundary.
However, every primitive direct row in this exact search is
involutive and hence already belongs to a known finite-G-measurable
branch.

This does not prove the arbitrary-colour product theorem.  It does
remove the smallest genuinely coloured product search space as a
source of B-style obstruction candidates.

The central local router agrees with this split: every primitive
row in this corpus routes to `product_finite_g_branch`; no row
routes to `product_genuinely_coloured_bottleneck` or to the
bi-free corridor target.
