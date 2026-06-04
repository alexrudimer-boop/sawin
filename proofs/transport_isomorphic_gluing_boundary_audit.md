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
- naive identity-normalized split model is YBE: `False`;
- first naive split YBE failure: `{'input': '((0, 0), (0, 0), (1, 0))', 'sigma1_sigma2_sigma1': '((0, 0), (0, 1), (1, 1))', 'sigma2_sigma1_sigma2': '((0, 0), (0, 0), (1, 1))'}`;
- local router verdict: `product_finite_g_branch`;
- local router product holonomy details: `('swapped_identity_base_cyclic',)`;
- local router detector group orders: `(3,)`;
- local router detector gaps: `()`;
- closed detector chain complete: `True`;
- assembled detector group orders: `(3,)`;
- assembled final rack size from one-point terminal rack: `18`;
- assembled size formula holds: `True`;
- cyclic rack gauge: `u_i = x_i - i mod 3`;
- cyclic rack gauge verified through degree: `5`;
- cyclic rack gauge check passed: `True`.

## Pro Counter-Audit Examples

The later Pro counter-audit isolates the two proof gaps as separate
finite examples.  Both examples satisfy the stated product-like
transport-isomorphism hypotheses and are rack-dominated by other
routes; their role is to invalidate the proof mechanism.

### Gap 1: Loop Monodromy

Let `X={0,1} x Z/3` and

```text
r((a,i),(b,j))=((b,j+1),(a,i+1)).
```

- YBE: `True`;
- all mixed rows product-like: `True`;
- product-like transports are internal-solution isomorphisms: `True`;
- transport loop group orders: `[3, 3]`;
- `sigma_1^2` witness: `((0, 0), (1, 0)) -> ((0, 2), (1, 2))`.

Thus coherent transport isomorphisms can have nontrivial loop
monodromy; no block gauge can conjugate a 3-cycle transport to the
identity.

### Gap 2: Quotient Colour Routing

Let `Z=Z/3` be the dihedral rack with `a*b=2a-b`, and take the
Cartesian product of `Z` with a two-point identity fibre.  Then

```text
r((a,i),(b,j))=((a*b,i),(a,j)).
```

- total YBE: `True`;
- quotient YBE: `True`;
- all mixed rows product-like: `True`;
- product-like transports are internal-solution isomorphisms: `True`;
- transport loop group orders: `[1, 1, 1]`;
- quotient word and path: `(1, 1, 1)` sends `((0, 1), (2, 0), (1, 2), (0, 1))`;
- returns to base: `True`;
- changes colours before returning: `True`.

So even with trivial fibre transport, a quotient-kernel braid can
move quotient colours during the word and return only at the end.
The fixed-colour substrand-deletion argument is therefore not a
formal consequence of the stated hypotheses.

## Consequence

This six-point solution satisfies the local transport-isomorphism
part of the proposed gluing theorem, but the transport groupoid has
loop monodromy of order `3`.  Therefore product-like
transport-isomorphism does not by itself justify replacing every
mixed transport by the identity in one global block gauge.
For this witness, the naive identity-normalized split model is not
even a YBE solution; the audit records an explicit braid-relation
failure.

The example is not being proposed as a Sawin counterexample.  It is
one of the identity-base cyclic product rows already routed by
`local_master_bottleneck_summary()` to `product_finite_g_branch`
with detector group order `3`; see
`proofs/identity_base_product_branch.md`.  Its role here is only to
make the flatness obligation in
`proofs/transport_isomorphic_gluing_boundary.md` explicit.

The same router row feeds the closed-chain rack assembly.  Starting
from the one-point terminal rack, the single detector group `C_3`
produces the sharp factor size `2*3^2=18`, and the generated audit
checks this size formula directly.

There is also a direct all-arity explanation for this row.  In
one-based positions, the fibre gauge `u_i=x_i-i mod 3` conjugates the
fibre crossing `(x,y)->(y,x+1)` to the cyclic rack crossing
`(u,v)->(v+1,u)`.  The generated audit verifies this generator
identity through degree `5`; the displayed formula is the all-arity
reason.
