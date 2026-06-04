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
- all transport loop groups trivial: `False`;
- local router verdict: `product_finite_g_branch`;
- local router product holonomy details: `('swapped_identity_base_cyclic',)`;
- local router detector group orders: `(3,)`;
- local router detector gaps: `()`.

## Consequence

This six-point solution satisfies the local transport-isomorphism
part of the proposed gluing theorem, but the transport groupoid has
loop monodromy of order `3`.  Therefore product-like
transport-isomorphism does not by itself justify replacing every
mixed transport by the identity in one global block gauge.

The example is not being proposed as a Sawin counterexample.  It is
one of the identity-base cyclic product rows already routed by
`local_master_bottleneck_summary()` to `product_finite_g_branch`
with detector group order `3`; see
`proofs/identity_base_product_branch.md`.  Its role here is only to
make the flatness obligation in
`proofs/transport_isomorphic_gluing_boundary.md` explicit.
