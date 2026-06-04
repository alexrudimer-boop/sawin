# Affine Rigid Pressure Core Audit

This generated audit applies the rigid-pressure-core filters to a
structured affine-linear search space.  It is a finite search
frontier, not a proof of Sawin's problem.

## Exact Affine `F_2^2` Search

- exhaustive affine-linear scan: `True`;
- checked affine maps: `1048576`;
- invertible affine maps: `322560`;
- affine YBE tables: `481`;
- terminal survivors: `24`;
- structural survivors: `0`;
- rigid pressure core candidates: `0`;
- first failed filter counts: `{'bidegenerate': 408, 'noninvolutive': 49, 'quotient_rigid': 24}`.

The terminal survivors are exactly the affine size-four rows that
escape bidegeneracy, involutivity, rack-type, and flip-across filters.
They still all fail the next structural test, quotient-rigidity.

Representative terminal survivor records:

- offset `0011`, first failed `quotient_rigid`, congruences `3`, observer blocks `2`.
- offset `1100`, first failed `quotient_rigid`, congruences `3`, observer blocks `2`.
- offset `0010`, first failed `quotient_rigid`, congruences `4`, observer blocks `2`.
- offset `1000`, first failed `quotient_rigid`, congruences `4`, observer blocks `2`.

## Exact Affine Prime-Line Searches

### `F3`

- exhaustive affine-line scan: `True`;
- checked affine maps: `729`;
- invertible affine maps: `432`;
- affine YBE tables: `31`;
- terminal survivors: `0`;
- structural survivors: `0`;
- rigid pressure core candidates: `0`;
- first failed filter counts: `{'bidegenerate': 30, 'noninvolutive': 1}`.

### `F5`

- exhaustive affine-line scan: `True`;
- checked affine maps: `15625`;
- invertible affine maps: `12000`;
- affine YBE tables: `221`;
- terminal survivors: `0`;
- structural survivors: `0`;
- rigid pressure core candidates: `0`;
- first failed filter counts: `{'bidegenerate': 220, 'noninvolutive': 1}`.

## Named `F_2^3` Pressure Row

- bidegenerate: `True`;
- noninvolutive: `True`;
- not rack: `True`;
- observer rigid: `False`;
- subsolution rigid: `False`;
- first failed filter: `quotient_rigid`;
- known closure: `two-state hidden cyclic rack gauge plus inert observer`.

## Conclusion

The exact affine-linear size-four family over F_2^2 has terminal survivors, but no structural rigid-pressure-core survivor: all 24 terminal survivors fail quotient-rigidity.  The exact affine line searches over F_3 and F_5 have no terminal survivors.  The named F_2^3 pressure row remains a useful guardrail but fails observer and subsolution rigidity and is already closed by a finite sequential rack gauge.
