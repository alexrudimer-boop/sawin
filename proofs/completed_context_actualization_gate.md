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

## Naive actualization is false

The naive theorem that these local quiver conditions imply one-vertex
actualization is false.  A one-vertex ordinary YBE table must satisfy the YBE
on every triple of letters, including triples whose intermediate adjacent
pairs are unsupported in the quiver row system.  Supported quiver-cube
coherence does not see all of these mixed unsupported constraints.

Here is an explicit one-vertex obstruction with trivial endpoint labels.  Let
the edge set contain distinct symbols

```text
x,y,z,u,v,a,b,c,d,h,k,p,w,t
```

and filler symbols

```text
A_i,B_i       for 1 <= i <= 6.
```

Let the supported pair set consist of the eighteen pairs

```text
p_1=(x,y),     q_1=(u,v),     r_1=(A_1,B_1),
p_2=(y,z),     q_2=(a,b),     r_2=(A_2,B_2),
p_3=(x,a),     q_3=(c,d),     r_3=(A_3,B_3),
p_4=(d,b),     q_4=(h,k),     r_4=(A_4,B_4),
p_5=(u,p),     q_5=(c,h),     r_5=(A_5,B_5),
p_6=(w,t),     q_6=(p,k),     r_6=(A_6,B_6).
```

Define the supported row bijection as the product of six cycles

```text
p_i -> q_i -> r_i -> p_i.
```

The six important rows are

```text
B(x,y)=(u,v),
B(y,z)=(a,b),
B(x,a)=(c,d),
B(d,b)=(h,k),
B(u,p)=(c,h),
B(w,t)=(p,k).
```

Boundary preservation and context-product compatibility are automatic because
the quiver has one vertex.  Global table consistency holds because each edge
is its own colour.  The supported cube checks are vacuous: every supported
length-three path exits the supported pair set before both sides of a braid
cube can be evaluated.

If an ordinary bijective YBE table `r:X^2 -> X^2` realized this system, the
six rows would force

```text
r(x,y)=(u,v),
r(y,z)=(a,b),
r(x,a)=(c,d),
r(d,b)=(h,k),
r(u,p)=(c,h),
r(w,t)=(p,k).
```

Now apply ordinary YBE to `(x,y,z)`.  The right-hand braid word gives

```text
r_23(x,y,z)=(x,a,b),
r_12(x,a,b)=(c,d,b),
r_23(c,d,b)=(c,h,k).
```

For the left-hand word, write `r(v,z)=(P,Q)`.  Then

```text
r_12(x,y,z)=(u,v,z),
r_23(u,v,z)=(u,P,Q).
```

To finish at `(c,h,k)`, one must have

```text
Q=k,       r(u,P)=(c,h).
```

Since `r(u,p)=(c,h)` and `r` is injective, `P=p`.  Hence ordinary YBE forces

```text
r(v,z)=(p,k).
```

But the specified row already has

```text
r(w,t)=(p,k).
```

The input pairs `(v,z)` and `(w,t)` are distinct, contradicting bijectivity of
`r`.  Thus no ordinary finite or infinite one-vertex YBE table realizes this
row system.

The obstruction is a mixed unsupported YBE-forcing collision: ordinary YBE
forces a value on an unsupported pair, and that value is already used by a
different supported input pair.

## Corrected completion gate

A finite quiver row system is a serious negative candidate only if its partial
pair map admits a finite total ordinary YBE completion.  At minimum it must
pass a mixed-cube propagation test.

Start with the partial pair map

```text
r_0: P -> P
```

defined by the supported rows.  For every triple `(x,y,z)`, partially evaluate

```text
r_12 r_23 r_12(x,y,z)
and
r_23 r_12 r_23(x,y,z)
```

using the currently known values of `r_0`.  Whenever one side is fully known
and the other side has exactly one unknown pair value, ordinary YBE forces
that unknown value.  Add it if it is unused; reject if it collides with the
image of a different input pair.  Iterate this closure.

This propagation test is necessary, not sufficient.  The full corrected
candidate condition is:

```text
There exists a finite set X containing the row letters and a bijection
r:X^2 -> X^2 extending the partial row map such that r satisfies ordinary
YBE on X^3.
```

Only after this ordinary YBE-completion gate is passed does it make sense to
ask for finite context transitions `tau_x`, retained germs, endpoint labels,
and preservation of the intended braid-realizable endpoint language.

Even a finite ordinary YBE completion would still not decide the Sawin fork by
itself.  It is only the first collapse a negative candidate must survive.  The
candidate must also occur as an actual completed-context residual interval and
must preserve the actual braid-realizable endpoint language.  The corrected
finite test is therefore:

```text
For every nonidentity endpoint u, is there a finite quotient
phi: Art_I -> Q such that no actual endpoint-u branch has phi-trivial
Artin readout?
```

Equivalently, a negative example must produce one actual interval and one
`u != 1` such that every finite quotient `phi:Art_I -> Q` has an actual
endpoint-`u` branch whose Artin readout is `phi`-trivial.  This condition, for
an already actual interval, is equivalent to the normalized-law no-rack
sequence.  Failure of an earlier ordinary-completion or actualization criterion
is only another gap.

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
context-product compatibility, inverse-row saturation, supported YBE cube
coherence, and ordinary finite YBE-completability, construct a finite set X, a
bijective YBE table r:X^2 -> X^2, a completed-context residual interval I, and
an isomorphism from the row system to I preserving:

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
   becomes relevant only after a finite ordinary YBE-completion and
   one-vertex actualization preserving W_u^br.
```

Thus the current decisive negative target is not merely "find a
nonresidually finite formal row group."  It is "actualize a nonseparable
endpoint-labelled braided-quiver row system into one finite YBE table after
passing the ordinary YBE-completion gate, or produce the nonseparable actual
interval directly."
