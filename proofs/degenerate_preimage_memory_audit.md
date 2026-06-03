# Degenerate preimage memory audit

Date: 2026-06-03

This generated audit records the finite two-strand memory object
for the degenerate derived-Hurwitz preimage gate.  A visible pair
`(a,b)` asks for hidden neighbours `y` with `lambda_b(y)=a`.
The nondegenerate derived rack route is exactly the singleton-fibre
case.  The finite local repair keeps the edge-memory state
`(a,b,y)` for actual pairs `(b,y)`, but this is not yet a tower
proof; triple and quadruple consistency remain to be checked.

## Rows

### nondegenerate_singleton_fibres

- element count: `2`;
- visible pair count: `4`;
- edge-memory state count: `4`;
- singleton fibre count: `4`;
- missing fibre count: `0`;
- multiple same-candidate count: `0`;
- ambiguous candidate count: `0`;
- visible derived operation total: `True`;
- finite edge memory repairs two-strand gate: `True`;
- tower consistency status: `requires_triple_quadruple_check`;
- hidden preimage memory needed: `False`;
- visible compression is safe: `True`;
- records degenerate memory gate: `True`.

### degenerate_identity_memory_gate

- element count: `2`;
- visible pair count: `4`;
- edge-memory state count: `4`;
- singleton fibre count: `0`;
- missing fibre count: `2`;
- multiple same-candidate count: `2`;
- ambiguous candidate count: `0`;
- visible derived operation total: `False`;
- finite edge memory repairs two-strand gate: `True`;
- tower consistency status: `requires_triple_quadruple_check`;
- hidden preimage memory needed: `True`;
- visible compression is safe: `False`;
- records degenerate memory gate: `True`.

Recorded nonsingleton fibres:

- status `multiple_same_candidate`, derived label `0`, original label `0`, preimages `(0, 1)`.
- status `missing`, derived label `0`, original label `1`, preimages `()`.
- status `missing`, derived label `1`, original label `0`, preimages `()`.
- status `multiple_same_candidate`, derived label `1`, original label `1`, preimages `(0, 1)`.

## Meaning

The finite edge-memory object repairs only the local ambiguity.
A proof of the augmented Artin-envelope lemma still needs to
show that these edge memories can be propagated through YBE
triples and through point-forgetting with one fixed finite
operator group and bounded vertical kernel.  A counterexample
should look for failure of exactly that triple/quadruple
compatibility, not for whole-image exponent growth.
