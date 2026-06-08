# Four-Point Contextual Completion Audit

This generated audit checks the explicit contextual rack completion for
the four-point degenerate YBE solution on `00,01,10,11`.

## Summary

- source YBE: `True`;
- contextual monoid size: `6`;
- contextual quotient classes: `20`;
- forced product conflicts: `0`;
- rack size: `20`;
- rack YBE: `True`;
- rack-form check: `True`;
- forced partial translations extend to permutations: `True`;
- base separation for equal contexts: `True`;
- one-fibre separation for equal contexts: `True`;
- equivariance checked arities: `[1, 2, 3, 4, 5, 6, 7, 8]`;
- orbit-injectivity checked arities: `[1, 2, 3, 4, 5, 6, 7, 8]`;
- all checks passed: `True`.

## Nontrivial Left Translations

The deterministic class labels are canonical for this script, not the
labels from the theoretical response.  The nontrivial translations are
still only paired transpositions:

```json
{
  "4": [
    [
      4,
      6
    ]
  ],
  "5": [
    [
      5,
      7
    ]
  ],
  "6": [
    [
      4,
      6
    ]
  ],
  "7": [
    [
      5,
      7
    ]
  ],
  "16": [
    [
      16,
      18
    ]
  ],
  "17": [
    [
      17,
      19
    ]
  ],
  "18": [
    [
      16,
      18
    ]
  ],
  "19": [
    [
      17,
      19
    ]
  ]
}
```

## Consequence

The four-point example is positive evidence for the contextual route.  The
finite partial translations close to a 20-element rack in this case, and
the contextual readout is equivariant and orbit-injective in the checked
arities.  The all-arity proof still uses the orbit classification of this
specific example; the audit does not prove the corresponding theorem for
all finite degenerate YBE solutions.
