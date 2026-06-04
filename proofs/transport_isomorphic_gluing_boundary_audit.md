# Transport-Isomorphic Gluing Boundary Audit

This generated audit records a concrete transport-isomorphic
product-like extension whose transport loop monodromy is nontrivial.

Let

```text
X = {0,1} x Z/3
r((a,x),(b,y)) = ((a,y),(b,x+1)).
```

The quotient by the first coordinate is the identity solution on two
colours, and the two colour fibres are crossing-closed.

## Audit

- element count: `6`;
- YBE: `True`;
- branch tags: `[]`;
- colour partition: `[['(0, 0)', '(0, 1)', '(0, 2)'], ['(1, 0)', '(1, 1)', '(1, 2)']]`;
- all mixed transitions product-like: `True`;
- all mixed transitions swapped-product-like: `True`;
- all product-like rows have transport isomorphisms: `True`;
- all rows transport-isomorphic: `True`;
- transport edge count: `6`;
- transport loop group orders: `[3, 3]`;
- all transport loop groups trivial: `False`.

## Consequence

This six-point solution satisfies the local transport-isomorphism
part of the proposed gluing theorem, but the transport groupoid has
loop monodromy of order `3`.  Therefore product-like
transport-isomorphism does not by itself justify replacing every
mixed transport by the identity in one global block gauge.

The example is not being proposed as a Sawin counterexample.  It is
one of the identity-base cyclic product rows already routed to the
cyclic pairwise-linking detector branch in
`proofs/two_colour_fibre3_product_audit.md`.  Its role here is only
to make the flatness obligation in
`proofs/transport_isomorphic_gluing_boundary.md` explicit.
