# Edge memory tower prefix

Date: 2026-06-03

This note follows `proofs/degenerate_preimage_memory_gate.md`.  The finite
edge memory

```text
E_X={(a,b,y): lambda_b(y)=a}
```

repairs the two-strand preimage lookup locally.  The next question is whether
this memory behaves coherently under braid triples and point-forgetting.

Use the concrete edge label of an adjacent pair:

```text
e(x,y)=(lambda_x(y), x, y).
```

For a tuple `(x_1,...,x_m)`, record the adjacent edge-memory tuple

```text
(e(x_1,x_2), e(x_2,x_3), ..., e(x_{m-1},x_m)).
```

Because each edge label contains the actual adjacent pair, this encoding is
injective on `X^m`.  It is deliberately not a compression theorem.  It is the
finite local memory object that prevents the derived preimage lookup from
forgetting hidden neighbours.

## Triple gate

For arity `3`, the audit checks that the YBE braid relation remains true
after edge encoding:

```text
edge(R_12 R_23 R_12(x,y,z))
=
edge(R_23 R_12 R_23(x,y,z)).
```

This is the first consistency gate for using edge memory as a label-motion
object.

## Quadruple and forgetting gates

For arity `4`, the audit checks:

- each braid generator update on edge-memory states is well-defined;
- forgetting any one coordinate induces a well-defined map from arity-4 edge
  memory to arity-3 edge memory.

These checks are finite and exact for the supplied table.

## What remains open

The edge-memory prefix does not prove the augmented Artin-envelope lemma.
It only says the canonical finite memory survives the first local tower
checks.  The missing point-pushing theorem must still show one of:

```text
positive: edge-memory point-pushing vertical kernels have uniformly bounded
          exponent over one fixed finite group-Hurwitz base;

negative: some finite degenerate X forces edge-memory vertical kernels that
          escape every fixed exponent/base pair compatibly in n.
```

Thus the next useful computation is a genuine point-pushing image computation
over edge-memory labels, starting with `Q_X(3)` and `Q_X(4)`, rather than a
whole-image order computation.

## Generated audit

The executable helper is

```text
edge_memory_tower_audit(X)
```

and the generated report is

```text
proofs/edge_memory_tower_audit.md
```

The report checks the same nondegenerate prefix witness and degenerate
identity row used in the preimage-memory audit.  Both pass the edge-memory
triple/quadruple prefix, which moves the obstruction target from local
preimage ambiguity to the point-pushing vertical-kernel layer.
