# Edge memory tower audit

Date: 2026-06-03

This generated audit checks the first tower gates for the finite
adjacent edge-memory object.  The edge label of a pair `(x,y)` is
`(lambda_x(y),x,y)`.  Adjacent edge labels encode tuples
injectively, so braid-generator updates and point-forgetting maps
are finite maps on the edge-memory state space.  This audit checks
the braid triple and arity-four forgetting prefixes; it does not
yet prove the bounded vertical-kernel part of the augmented
Artin-envelope lemma.

## Rows

### nondegenerate_prefix_witness

- element count: `2`;
- edge label count: `4`;
- arity-3 tuple count: `8`;
- arity-4 tuple count: `16`;
- arity-3 encoding injective: `True`;
- arity-4 encoding injective: `True`;
- braid relation on edge memory: `True`;
- generator updates well-defined: `((0, True), (1, True), (2, True))`;
- point-forgetting maps well-defined: `((0, True), (1, True), (2, True), (3, True))`;
- verifies edge-memory triple/quadruple prefix: `True`.

### degenerate_identity_edge_memory

- element count: `2`;
- edge label count: `4`;
- arity-3 tuple count: `8`;
- arity-4 tuple count: `16`;
- arity-3 encoding injective: `True`;
- arity-4 encoding injective: `True`;
- braid relation on edge memory: `True`;
- generator updates well-defined: `((0, True), (1, True), (2, True))`;
- point-forgetting maps well-defined: `((0, True), (1, True), (2, True), (3, True))`;
- verifies edge-memory triple/quadruple prefix: `True`.

## Meaning

The finite edge-memory object survives the first local tower
checks in these rows.  What remains open is whether its
point-pushing vertical kernel is uniformly bounded-exponent
over a fixed finite group-Hurwitz base, or whether a genuine
degenerate candidate can force unbounded vertical memory.
