# Product-Like Transport Boundary Audit

This generated audit records the finite boundary between two
subsolution-fibre mechanisms in the first size-four degenerate
non-involutive examples.

It is not a proof of Sawin's conjecture.  It proves only that finite
YBE locality does not force product-like mixed transports to be
isomorphisms of the internal block subsolutions.

## type_a_affine_f2

- element count: `4`;
- YBE: `True`;
- involutive: `False`;
- proper congruences: `2`;
- congruence block-size profiles: `[[4], [2, 2], [1, 1, 1, 1]]`;
- proper subsolution-fibre congruences: `1`;
- flip-across decomposition: `False`;
- nontrivial one-state observer: `True`.

| partition | product-like | transport isomorphism |
| --- | --- | --- |
| `[['(0, 0)', '(1, 1)'], ['(0, 1)', '(1, 0)']]` | `True` | `False` |

## type_b_flip_across

- element count: `4`;
- YBE: `True`;
- involutive: `False`;
- proper congruences: `4`;
- congruence block-size profiles: `[[4], [2, 2], [1, 1, 2], [1, 1, 2], [1, 1, 1, 1]]`;
- proper subsolution-fibre congruences: `2`;
- flip-across decomposition: `True`;
- nontrivial one-state observer: `False`.

| partition | product-like | transport isomorphism |
| --- | --- | --- |
| `[["('P', 0)", "('P', 1)"], ["('T', 0)", "('T', 1)"]]` | `True` | `True` |
| `[["('T', 0)"], ["('T', 1)"], ["('P', 0)", "('P', 1)"]]` | `True` | `True` |

## Consequence

The Type A affine model has exactly one proper subsolution-fibre
congruence, with block sizes `[2,2]`.  Its mixed rows are
product-like, but the resulting one-coordinate transport maps are
not isomorphisms of the two internal block subsolutions.  The only
subsolution-fibre refinement that removes this obstruction is the
equality congruence, which is not a proper compression.

Thus Question B from the queued Pro prompt has a negative finite
answer in this sense: product-like mixed transport is a real weaker
condition than product-like transport by subsolution isomorphisms.
The Type B flip-across model lies on the positive transport branch,
while Type A requires the separate parity/fibre gauge.
