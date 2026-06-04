# Size-Four Non-Affine Frontier Audit

This generated audit records a finite correction to the size-four
frontier.  The committed Type B representative is genuinely
non-affine over `F_2^2` under every relabeling, but it is already
closed by the flip-across/product-rack mechanism.

## size4_type_a_affine_f2

- YBE: `True`;
- involutive: `False`;
- left-degenerate: `True`;
- right-degenerate: `True`;
- everywhere left singular: `True`;
- everywhere right singular: `True`;
- affine over `F_2^2` up to relabeling: `True`;
- flip-across decomposition: `False`;
- point-separating proper quotients: `False`;
- mechanism: `all-arity parity/fibre gauge to the two-element cyclic rack`.

Affine witness:

- label: `{'(0, 0)': (0, 0), '(0, 1)': (0, 1), '(1, 0)': (1, 0), '(1, 1)': (1, 1)}`;
- translation: `(0, 0, 1, 1)`;
- linear columns: `((0, 1, 1, 1), (0, 1, 0, 0), (0, 0, 1, 0), (1, 1, 1, 0))`.

## size4_type_b_flip_across_nonaffine

- YBE: `True`;
- involutive: `False`;
- left-degenerate: `True`;
- right-degenerate: `True`;
- everywhere left singular: `False`;
- everywhere right singular: `False`;
- affine over `F_2^2` up to relabeling: `False`;
- flip-across decomposition: `True`;
- point-separating proper quotients: `True`;
- mechanism: `flip-across union of the two-point identity solution and the two-point toggle permutation solution`.

Active-factor certificate:

- proper factor sizes: `(3, 3)`;
- finite conditions hold: `True`;
- injectivity witness: `None`.

## Remaining Gap

The repo now contains an explicit non-affine size-four degenerate non-involutive solution, but it is not a rigid-core candidate: it is a flip-across union with proper active quotient factors.  The remaining size-four question is whether any degenerate non-involutive solution lies outside the Type A affine gauge and Type B flip-across mechanisms.

## Next Prompt

`prompts/gpt55_pro/2026-06-04-observer-factor-rackification_ask_now.md`.
