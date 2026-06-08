# Context-Signature Quotient Failure Certificate

This generated certificate records a six-point linear skew-over-flip
YBE solution for which the relation

```text
x ~ x' iff (m_x,r_x)=(m_x',r_x')
```

is not a braided congruence.

## Checks

- YBE: `True`;
- nondegenerate: `True`;
- context-signature quotient classes: `5`;
- context-signature braided congruence: `False`;
- context-signature core braided congruence: `True`;
- context-signature core classes: `6`;
- `e_0` and `f_0` have equal context signatures: `True`;
- `e_1` and `e_2` have equal context signatures: `False`;
- `R(e_0,e_1)`: `['e_1', 'e_2']`;
- `R(f_0,e_1)`: `['e_2', 'f_0']`;
- all claimed checks passed: `True`.

## First Congruence Failure

```json
{
  "x": "(0, 0)",
  "x_prime": "(1, 0)",
  "y": "(0, 1)",
  "y_prime": "(0, 1)",
  "R_x_y": [
    "(0, 1)",
    "(0, 2)"
  ],
  "R_x_prime_y_prime": [
    "(0, 2)",
    "(1, 0)"
  ],
  "input_classes": [
    0,
    1
  ],
  "output_classes": [
    1,
    2
  ],
  "output_prime_classes": [
    2,
    0
  ]
}
```

## Consequence

The quotient by equal two-sided context signatures cannot be used as a
universal induction quotient.  This example is nondegenerate, so it is
not a Sawin counterexample, but it kills the proposed canonical
`x -> (m_x,r_x)` quotient route.
