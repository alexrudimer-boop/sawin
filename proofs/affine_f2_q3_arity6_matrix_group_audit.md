# Affine F2^3 Arity-6 Matrix Group Audit

The arity-6 matrix-group computation passes for rack24: the tetrahedral rack image, the shifted-linear X image, and the joint image all have order 39,813,120.  Thus K_6 is trivial.  This also corrects the provisional unitary-pattern guess 41,057,280.

## Setup

- arity: `6`;
- rack24 vector-space dimension over `F_2`: `12`;
- shifted-linear `X` vector-space dimension over `F_2`: `18`;
- joint permutation degree used by SymPy Schreier-Sims: `266240`.

## Orders

| image | order |
|---|---:|
| rack24 `G_Y(6)` | 39813120 |
| shifted-linear `G_X(6)` | 39813120 |
| joint `G_{Y,X}(6)` | 39813120 |

## Consequence

- all orders equal: `True`;
- joint kernel `K_6` trivial: `True`;
- provisional expected unitary order from the Pro answer: `41057280`;
- actual order: `39,813,120`.

The direct arity-6 obstruction to domination by rack24 is therefore absent.  The remaining all-arity issue is the rack-only finite-to-infinite step: prove a uniform slice-conjugacy/parabolic-kernel-generation theorem, or find a higher-arity kernel word.
