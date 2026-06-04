# Affine F2^3 Dihedral Native Image Audit

This generated audit compares native image groups for the affine
`F_2^3` survivor and the three-element dihedral rack.  It uses
affine transformations over `F_2` for `X` and linear transformations
over `F_3` for `D_3`, avoiding tuple-permutation enumeration.

- max arity: `5`;
- state limit: `1000000`;
- any truncated: `False`;
- all computed orders match: `False`.
- first D3 failure arity: `5`.

| n | D3 image order | X image order | match | truncated |
| ---: | ---: | ---: | --- | --- |
| 2 | 3 | 3 | True | False |
| 3 | 24 | 24 | True | False |
| 4 | 648 | 648 | True | False |
| 5 | 51840 | 77760 | False | False |

## First D3-Kernel Witness

- arity: `5`;
- word length: `25`;
- witness word: `(1, 1, 2, 1, 1, 3, 2, 4, 3, 3, 2, 1, 4, 3, 2, 2, 1, 3, 2, 4, 3, 3, 2, 4, 3)`;
- explored states: `154504`;
- image of the zero tuple under the X action: `((1, 1, 1), (1, 1, 0), (1, 0, 1), (0, 1, 0), (0, 1, 1))`.

## Conclusion

Native linear/affine image generation shows that the three-element dihedral rack repair matches the affine F_2^3 candidate through arity 4 but fails at arity 5: the X image is larger than the D3 image, and a native joint-image search gives an explicit braid word in the D3 kernel that moves X.  This rules out D3 domination of this candidate but does not rule out a larger finite rack detector.
