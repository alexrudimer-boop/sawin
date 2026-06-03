# Prefix point-forgetting restriction surface

Date: 2026-06-03

The cohomology pressure audit records that a finite Artin envelope must make
vertical cocycles compatible under point-forgetting.  This note isolates the
first concrete marked comparison:

```text
Q_X(4) <= G_X(5)   --->   Q_X(3) <= G_X(4).
```

Use the standard generators `alpha_{i,n+1}` of the point-pushing kernel.
When deleting one of the four stationary strands in `B_5`, the marked
generator `alpha_{i,5}` has the expected image

```text
delete stationary strand j:

alpha_{i,5} |-> identity       if i=j,
alpha_{i,5} |-> alpha_{i,4}    if i<j,
alpha_{i,5} |-> alpha_{i-1,4}  if i>j.
```

This is the abstract braid-level restriction.  The tuple action need not
commute with this deletion strictly, because the deleted strand can leave
monodromy on the remaining labels before it is forgotten.

## Audit

The generated report

```text
proofs/prefix_point_forgetting_restriction_audit.md
```

checks all sixteen rows `(deleted stationary strand, source generator)` for
the first surface `Q_X(4) -> Q_X(3)`.

For the nondegenerate two-point prefix witness, every off-diagonal row
matches the marked restriction exactly.  The four diagonal rows each have
`32` mismatches: after deleting the stationary strand looped around by
`alpha_{i,5}`, the abstract generator restricts to identity, but the tuple
labels still record a vertical monodromy.

For the degenerate identity row, all sixteen rows match.  Thus nonunit prefix
memory and vertical point-forgetting monodromy are distinct phenomena.

## Consequence

This surface is not a counterexample.  Finite racks also have vertical
point-forgetting data, and their operator-label model controls it by bounded
vertical kernels.  The audit instead makes the next obstruction criterion
concrete:

- a positive proof must show that the diagonal restriction cocycles are
  absorbed by one fixed finite operator-label base with uniformly bounded
  vertical exponent;
- a negative proof must find a larger table or local interval where these
  restriction cocycles cannot be made compatible in the tower for any fixed
  finite group-Hurwitz base.

The first place to compute this is exactly the marked `Q_X(4) -> Q_X(3)`
restriction surface.
