# Completed-context actualization gate

Date: 2026-06-04

This note refines the negative side of
`proofs/completed_context_finite_artin_separation.md`.  It records the exact
actuality test that a formal partial-Wirtinger endpoint obstruction must pass
before it can be used against Sawin finite-rack domination.

## Actual row systems

An actual completed-context interval is not an arbitrary partial Artin row
system.  It comes from one finite bijective set-theoretic YBE table

```text
r: X^2 -> X^2.
```

Retained germs have the form

```text
e=(s,x)
```

where `s` is a context state and `x in X`.  A supported row has the form

```text
e=(s,x),        f=(s tau_x,y),
r(x,y)=(u,v),
e'=(s,u),       f'=(s tau_u,v).
```

Thus the row operation on germs is a finite braided-quiver operation on
composable context edges, but one with a one-vertex origin: every row is the
restriction of the same global table `r`.

## Necessary actuality constraints

A formal row system must satisfy at least the following constraints before it
can be considered a candidate actual interval.

1. Boundary preservation.  The outer context endpoints of a length-two path
   are preserved:

```text
s tau_x tau_y = s tau_u tau_v.
```

2. Global table consistency.  If two supported rows use the same input letter
   pair `(x,y)`, their output letter pair is the same `(u,v)`.  Refining
   formal edge colours can avoid collisions, but then the refined colours
   themselves must still come from one finite alphabet and one total table.

3. Inverse-row saturation.  The supported length-two path map is bijective on
   the supported component used by the interval, because the original `r` is a
   bijection.

4. YBE cube coherence.  For every supported length-three path, the two
   three-row composites agree:

```text
B_12 B_23 B_12 = B_23 B_12 B_23.
```

5. Artin-readout coherence.  The induced meridian and longitude row rules

```text
a_{e'} = a_e a_f a_e^-1,     l_{e'} = a_e l_f,
a_{f'} = a_e,                l_{f'} = l_e
```

must be coherent around the same actual cubes.  This is automatic for a true
braid action, but not for a freely wired formal partial-Wirtinger presentation.

These constraints are only necessary.  They do not prove that a finite
braided-quiver row system is the completed-context interval of some finite
one-vertex YBE table.

## Actualization theorem needed for B

The formal partial-Wirtinger construction in
`proofs/completed_context_finite_artin_separation.md` can encode arbitrary
finitely presented relators through cycles in the longitude relations.  That
warning remains valid, but it is not a counterexample unless it is actualized.

The negative route needs the following additional theorem or construction.

```text
Finite endpoint-labelled actualization theorem:

Given a finite inverse braided-quiver row system with endpoint labels,
boundary preservation, global table consistency after finite refinement,
context-product compatibility, inverse-row saturation, and YBE cube
coherence, construct a finite set X, a bijective YBE table r:X^2 -> X^2,
a completed-context residual interval I, and an isomorphism from the row
system to I preserving:

  - the row operation;
  - the endpoint map;
  - the Artin meridian/longitude recursion;
  - the braid-realizable endpoint languages W_u^br.
```

If such an actualization theorem can be applied to a nonseparable
partial-Wirtinger endpoint language, then the failure of profinite separation
is made actual and the diagonal normalized-law no-rack sequence follows.

If actualization fails for a formal row system, that failure alone proves
neither Sawin positive nor Sawin negative.  It only says that the formal
partial-Wirtinger pathology was not an actual finite YBE interval.

## Updated fork

The completed-context endpoint fork is therefore:

```text
A. Prove direct profinite endpoint-language separation for every actual
   interval:

      1 notin closure(W_u^br) in Art_I^T,  for all u != 1.

B. Construct an actual finite YBE interval whose braid-realizable endpoint
   language violates this separation.  A formal nonseparable row language
   becomes relevant only after a one-vertex actualization preserving W_u^br.
```

Thus the current decisive negative target is not merely "find a
nonresidually finite formal row group."  It is "actualize a nonseparable
endpoint-labelled braided-quiver row system into one finite YBE table, or
produce the nonseparable actual interval directly."
