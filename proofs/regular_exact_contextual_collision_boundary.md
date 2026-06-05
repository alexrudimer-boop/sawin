# Regular Exact Contextual Collision Boundary

Date: 2026-06-05

This note records the sharpened endpoint after the fixed-`M` finiteness
analysis.  For a fixed finite state quotient `M`, finite rack detection is
purely endpoint-label detection.  Once the finite set of actual endpoint
labels is separated, every remaining fixed-`M` bad pair is an exact equality
of contextual label tuples.

The label-equality side is finite-state, even regular.  The obstruction is
not fixed-`M` factorial endpoint holonomy.  It is the interaction of exact
contextual-label equality with braid reachability, and the possible need for
unbounded state refinement.

The sharp remaining obstruction is:

```text
unbounded exact contextual-label collapse
```

either at one fixed finite `M`, or through finer and finer quotients of
`L_X`.

## Fixed-M Endpoint Reduction

Fix a finite quotient

```text
theta:L_X -> M.
```

For

```text
x=(x_1,...,x_n) in X^n,
```

write

```text
a_i(x)=theta(lambda_{x_1}...lambda_{x_{i-1}}),
b_i(x)=theta(lambda_{x_{i+1}}...lambda_{x_n}),

Theta_n^M(x)_i=d_{a_i(x),x_i,b_i(x)}.
```

Let

```text
Sbar_M={d_{a,x,b}:a,b in M, x in X} subset C_M(X)
```

be the finite set of actual elements of `C_M(X)` represented by contextual
generators.  Different symbols may represent the same rack element, but
`Sbar_M` is finite.

Assume every distinct pair

```text
r != s in Sbar_M
```

is separated by some finite rack quotient

```text
phi_{r,s}:C_M(X) -> Y_{r,s}.
```

Taking the finite product over all such pairs gives one finite rack quotient

```text
phi_M:C_M(X) -> Y_M
```

which is injective on `Sbar_M`.

Therefore, for all `x,x' in X^n`,

```text
phi_M^n Theta_n^M(x)=phi_M^n Theta_n^M(x')
```

if and only if

```text
Theta_n^M(x)=Theta_n^M(x')
```

as elements of `C_M(X)^n`.

Thus, after endpoint separation, a fixed-`M` same-orbit pair is bad exactly
when

```text
x != x',
x' in B_n.x,
Theta_n^M(x)=Theta_n^M(x').
```

This proves that the fixed-`M` endpoint-label problem is finite.

## Hidden Stabilizer Holonomy Is Not Endpoint Data

Let

```text
R=C_M(X),
G=As(R).
```

Suppose a marked strand follows a braid path and has initial contextual label
`r in R`.  Let the escape cocycle be `g in G`.  The endpoint label is

```text
g.r.
```

If endpoint labels are equal, then

```text
g.r=r,
```

so

```text
g in Stab_G(r).
```

This stabilizer element may be diagnostically important, but an endpoint
finite rack detector sees only `r`.  Every rack quotient `phi:R -> Y` has

```text
phi(r)=phi(r).
```

Consequently, after exact `Theta_n^M` equality, fixed-`M` rack quotients have
no further endpoint information.  Hidden path holonomy can motivate an
enriched detector, but it is not additional endpoint-label detection.

To make holonomy finite-detectable one would need extra finite data, such as
a finite quotient of an associated escape groupoid or of `As(C_M(X))`, plus
uniform separation of the relevant transporter families from stabilizers.  If
the relevant transporter family accumulates profinitely at the stabilizer,
holonomy remains diagnostic rather than a finite contextual rack detector.

## Exact Fixed-M Collisions

For fixed `M`, define the exact collision relation

```text
C_M^exact={
  (x,x') in X^n x X^n :
  Theta_n^M(x)=Theta_n^M(x')
}_{n >= 1}.
```

The fixed-`M` bad relation is

```text
B_M^exact=C_M^exact cap {
  (x,x') :
  x != x',
  x' in B_n.x
}.
```

A meaningful bounded fixed-`M` theorem cannot merely say that a nonempty bad
relation has a shortest witness.  The useful statement would be:

```text
There exists N=N(M,X) such that every harmful family of fixed-M exact
collisions has a bad core of arity <= N.
```

Equivalently, after all bad pairs of arity at most `N` are separated by finite
refinements, no larger fixed-`M` exact collision remains harmful.

No such theorem follows from the current ingredients.

## Exact Label Equality Is Regular

Although boundedness is not known, the label-equality condition itself is
finite-state.

Define the finite relation

```text
E_M subset (M x X x M)^2
```

by

```text
(a,x,b) E_M (a',x',b')
iff
d_{a,x,b}=d_{a',x',b'} in C_M(X).
```

For words

```text
x=(x_1,...,x_n),
x'=(x'_1,...,x'_n),
```

the equality

```text
Theta_n^M(x)=Theta_n^M(x')
```

is equivalent to the existence of annotations

```text
a_i,a'_i,b_i,b'_i in M
```

satisfying

```text
a_1=a'_1=1,

a_{i+1}=a_i theta(lambda_{x_i}),
a'_{i+1}=a'_i theta(lambda_{x'_i}),

b_n=b'_n=1,

b_i=theta(lambda_{x_{i+1}}) b_{i+1},
b'_i=theta(lambda_{x'_{i+1}}) b'_{i+1},

(a_i,x_i,b_i) E_M (a'_i,x'_i,b'_i) for every i.
```

These are finite local constraints on adjacent annotated positions.  Hence
`C_M^exact` is a regular relation over the alphabet `X x X`.

This finite-state fact is important, but it does not close the proof.

## Braid Reachability Is The Remaining Fixed-M Obstruction

The same-orbit condition is

```text
x' in B_n.x.
```

Equivalently, it is reachability for the length-preserving reversible local
rewrite system

```text
xy <-> uv whenever r_X(x,y)=(u,v).
```

It is also equality in the corresponding homogeneous structure monoid
generated by the local YBE relations.

For special classes of YBE solutions, this reachability relation may have
normal forms, automaticity, or finite-state control.  For a general finite
bijective set-theoretic YBE solution, the current hypotheses do not imply
that the orbit relation is regular, automatic, noetherian, or bounded by
finite semigroup data.

If the orbit relation were regular in a compatible sense, then

```text
B_M^exact =
C_M^exact cap Orbit_X cap inequality
```

would be finite-state controlled.  A nonempty regular language has a shortest
word bounded in terms of the recognizing automaton.

But even that conditional observation would not automatically give one finite
detector for all arities.  Regularity of a bad language is weaker than a
finite-index detector equivalence.  To eliminate all harmful pairs by finite
products, one needs the relevant contextual Myhill-Nerode relation to have
finite index.

Thus the missing theorem is not merely a finite automaton for `Theta^M`; it
is a finite-index theorem for orbit-relevant contextual behavior.

## Deletion And Locality Do Not Bound Witnesses

The braid generator `sigma_i` acts only on coordinates `i,i+1`, but the
contextual label at coordinate `i` depends on all letters to the left and
right:

```text
a_i=theta(lambda_{x_1}...lambda_{x_{i-1}}),
b_i=theta(lambda_{x_{i+1}}...lambda_{x_n}).
```

Deleting an observer strand changes these states.  A contextual equality

```text
d_{a,x,b}=d_{a',x',b'}
```

may therefore disappear after deleting any coordinate.

Similarly, deleting strands from a braid path can destroy the color evolution
of the retained strands: forgotten strands may change colors and context
states before they are forgotten.

Hence braid locality and strand deletion do not prove bounded bad witnesses.

## State-Refinement Escape

Let

```text
K=hat{L_X} x X x hat{L_X}.
```

For each finite quotient `M`, let

```text
q_M:K -> M x X x M
```

be the natural projection.  Let `E_M` be equality of contextual generators in
`C_M(X)` as above.  Define the closed profinite contextual equality relation

```text
E_infty =
intersection_M (q_M x q_M)^(-1)(E_M)
subset K x K.
```

The finite-index property needed by the contextual tower is:

```text
There exists M_0 such that, on orbit-relevant contextual letters,
E_infty=(q_{M_0} x q_{M_0})^(-1)(E_{M_0}).
```

Equivalently, the contextual equality relation has finitely many clopen
classes on the orbit-relevant part of `K`.

Compactness does not imply this.  A closed relation on a profinite space need
not be clopen or finite-index.  Equality in a profinite completion is the
standard model: fixed ordinary words are pointwise separated by finite
quotients, but equality is not pulled back from one finite quotient.

Thus state-refinement escape is the exact profinite obstruction:

```text
fixed contexts are pointwise separated, but no finite quotient captures all
orbit-relevant contextual equality.
```

## Possible Harmful Mechanisms

Coarse fixed-`M` collisions are easy and usually harmless.  For instance, a
constant-action solution

```text
r(x,y)=(alpha(y),beta(x))
```

with `alpha,beta` commuting can make `M=1` collapse many labels.  If `alpha`
is transitive, `C_1(X)` identifies all `d_y`, and `Theta^1` is extremely
coarse.  Such examples often have small bad cores, are rack-absorbed, or are
separated by finer contextual states.

A genuine state-refinement obstruction would need more.  It would look like:

```text
observer powers lambda_o^k remain distinguishable in L_X,
but finite quotients see long periods;

active letters p,q collapse at prefix state lambda_o^k;

a braid corridor realizes
o^k p (...)  ->  o^k q (...)
inside one braid orbit;

choosing k=n! defeats every fixed finite quotient along a cofinal tail.
```

No such finite residual-rigid YBE example is currently constructed by the
tower formalism, but the current hypotheses also do not rule it out.

## Active-Factor Extraction Still Needs Extra Conditions

Given a finite contextual collapse with maps

```text
pi_{a,b}:X -> Z,
```

one can try to define a finite active YBE solution by the relation

```text
r_Z(
  pi_{a,lambda_y b}(x),
  pi_{a lambda_x,b}(y)
)
=
(
  pi_{a,lambda_v b}(u),
  pi_{a lambda_u,b}(v)
)
```

whenever `r_X(x,y)=(u,v)`.

This works only if the induced relation on `Z^2` is:

```text
functional,
total,
bijective,
YBE-valid on all of Z^3,
braid-equivariant for the maps Pi_n,
kernel-reflecting: ker rho_n^Z <= ker rho_n^X for all n.
```

Exact contextual collapse alone does not supply these properties.  The rule
may be partial on reachable pairs, nonfunctional because of hidden contexts,
nonbijective, invalid on unreached triples, or non-kernel-reflecting.

For profinite state-refinement collapse, the first obstacle is even earlier:
the relation may not factor through any finite `M`.

## Harmless Product Branches

Product and padding constructions remain guardrails rather than obstructions.

If

```text
X={*} x Z,
```

then `X` is just `Z`.  If

```text
X=E_triv x Z
```

with `E_triv` braid-trivial, then

```text
ker rho_n^X = ker rho_n^Z
```

for every `n`, so projection to `Z` is domination-equivalent.  If `E_triv` is
nontrivial, this is a proper active factor and cannot survive residual-rigid
reduction.

If `X` is already a rack solution, take `Y=X`; the kernel inclusion is equality.

These branches do not create residual-rigid harmful exact contextual collapse.

## Strongest Valid Endpoint

The strongest valid reduction from this stage is:

```text
fixed-M endpoint separation
=> fixed-M badness is exact Theta^M equality.
```

The label equality relation is regular.  The remaining obstruction is the
interaction with braid reachability and unbounded context refinement.

The current ingredients do not prove:

```text
bounded fixed-M harmful witnesses,

finite-index contextual Myhill-Nerode behavior,

active-factor extraction from exact/profinite contextual collapse.
```

The sharp missing lemma is:

```text
Every harmful unbounded exact contextual collapse is either finite-index /
rack-absorbed or finite-active-factor extractable.
```

This lemma is strictly smaller than Sawin and marks the current boundary of
the contextual detector route.
