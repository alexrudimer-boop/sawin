# Finite-Index Contextual Rigidity Boundary

Date: 2026-06-05

This note records the boundary after the bounded-bad-witness audit.  A bounded
bad-witness theorem would prove Sawin through the contextual tower, but it is
not currently justified by the stated residual-rigid hypotheses.

The sharp missing lemma is a finite-index contextual Myhill-Nerode statement:

```text
Orbit-relevant contextual behavior must factor through one finite two-sided
state system.
```

Without that, an infinite sequence of bad pairs can converge to a profinite or
holonomy-type witness that is not a finite active factor.

## Detector Criterion

Let `theta:L_X -> M` be a finite quotient of the positive left structure
monoid, and let

```text
phi:C_M(X) -> Y
```

be a finite rack quotient.  Define

```text
Lambda_n = phi^n Theta_n^M:X^n -> Y^n.
```

If `Lambda_n` separates distinct points inside every braid orbit of `X^n` for
every `n`, then

```text
ker rho_n^Y <= ker rho_n^X
```

for every `n`.

Indeed, if `beta in ker rho_n^Y`, then

```text
Lambda_n(rho_n^X(beta)x)
=
rho_n^Y(beta)Lambda_n(x)
=
Lambda_n(x).
```

The two `X`-points are in the same braid orbit, so orbit-injectivity forces
`rho_n^X(beta)x=x`.

## What A Bounded Witness Theorem Would Prove

A usable bounded theorem would say:

```text
There exists N=N(X) such that for every finite contextual detector (M,phi),
if a bad pair exists in some arity, then there is already a bad
subconfiguration of arity <= N.
```

Here bad means

```text
x != x',
x' in B_n.x,
Lambda_n(x)=Lambda_n(x').
```

If all same-orbit pairs of arity at most `N` are separated, the theorem would
force separation in every arity.

Then one obtains a single finite detector by a product argument.  There are
finitely many same-orbit pairs in arities `1,...,N`.  For each pair choose a
finite quotient `M_i` and finite rack quotient `Y_i` separating it.  Take

```text
M=product_i M_i,
Y=product_i Y_i.
```

The projections induce rack maps `C_M(X)->C_{M_i}(X)`, so `(M,Y)` separates all
pairs of arity at most `N`, hence all pairs.  The detector criterion gives
Sawin domination for `X`.

The problem is that no such bounded theorem follows from the present
hypotheses.

## Why Pointwise Separation Is Not Enough

Let `B_M` be the set of same-orbit bad pairs not separated by state quotient
`M`.  Refinement gives

```text
M' refines M  =>  B_{M'} subset B_M.
```

Pointwise tower separation gives

```text
intersection_M B_M = empty.
```

Uniform separation requires

```text
there exists M with B_M empty.
```

The universe of bad pairs

```text
disjoint union_n X^n x X^n
```

is infinite and discrete in the relevant sense, so empty intersection does not
imply one empty member.  The model is

```text
B_N={m>N} subset N.
```

Thus the missing principle is a noetherian or finite-index principle:

```text
orbit-relevant contextual badness must be controlled by finitely many finite
local patterns.
```

## Right-Separation In The Structure Monoid

The monoid `L_X` is residually finite by length-truncation quotients, but
ordinary residual finiteness is not the relevant property for scattering.

For `p,q in L_X`, define the profinite right equalizer

```text
E(p,q)={ahat in profinite_completion(L_X): ahat p = ahat q}.
```

This closed set is nonempty iff for every finite quotient `theta:L_X->M` there
exists `m in M` such that

```text
m theta(p)=m theta(q).
```

The property that rules scattering out is finite right-separation:

```text
there exists theta:L_X->M finite such that
m theta(p) != m theta(q) for all m in M.
```

Residual finiteness separates elements; finite right-separation separates
right translations uniformly over all states.  These are different.

Stronger properties imply finite right-separation:

```text
right cancellativity of L_X;
embedding of L_X into a residually finite group;
right-nondegeneracy for the displayed fixed-right-output pattern.
```

But YBE origin alone does not eliminate scattering.  For example, constant
action solutions can have relations such as

```text
lambda_0 lambda_0 = lambda_0 lambda_1,
```

so actual right equalizers occur before residual-rigid reduction.

The exact missing monoid lemma is:

```text
For every active pair p != q in L_X, E(p,q)=empty.
```

Equivalently, every active pair admits finite right-separation.

## Active Factor Extraction Obstruction

An infinite bad sequence can produce a family of context-dependent equivalence
relations on `X`,

```text
E_{ahat,bhat},
```

indexed by profinite two-sided contexts.  To obtain a finite
domination-reducing active factor, this family must factor through finitely
many states and satisfy a crossing-compatibility condition.

For a finite two-sided state system and maps

```text
pi_{a,b}:X -> Z,
```

the local rule must satisfy

```text
r_Z(pi_{a,lambda_y b}(x), pi_{a lambda_x,b}(y))
=
(pi_{a,lambda_v b}(u), pi_{a lambda_u,b}(v)).
```

This defines a finite YBE factor only if the right-hand side depends solely on
the two `Z` inputs and extends to a bijective YBE map on all of `Z^2`.

An infinite bad sequence may converge to a profinite active object whose
contextual equivalences vary on arbitrarily fine profinite neighborhoods.  In
that case there is no finite `Z`.  The active-factor extraction obstruction is
exactly failure of finite-index, crossing-compatible contextual behavior.

## Uniform Stabilizer Separation

For fixed `M`, let

```text
R=C_M(X),
G=As(R),
H=Stab_G(r_0).
```

If `r_1=g.r_0`, finite rack quotients separate `r_0` from `r_1` exactly when
`g` is separated from `H` in finite quotients of `G`.

Pointwise separability of every transporter is not enough.  For an infinite
family `T subset G\H`, uniform separation asks for one finite quotient

```text
q:G -> F
```

such that

```text
q(T) cap q(H)=empty.
```

Equivalently,

```text
closure(T) cap closure(H)=empty
```

inside the profinite completion.

Even closed stabilizers do not guarantee uniform separation.  In `G=Z`,
`H={0}` is closed, and each `n!` is individually separated from `0`, but no
single finite quotient separates all of

```text
T={n!: n>=1}
```

from `0`.

Thus bounded bad witnesses, or another finite-index theorem, are needed to
reduce the relevant transporter set to finitely many cases.

## Contextual Myhill-Nerode Formulation

For finite automaton contextual detectors, the right object is a
Myhill-Nerode relation on contexts.  Two contexts are equivalent if no
orbit-relevant finite continuation and braid test distinguishes their
contextual behavior.

A finite automaton detector exists exactly when this relation has finite index
and is stable under context transitions

```text
(a,b) -> (a lambda_x,b),
(a,b) -> (a,lambda_x b).
```

Pointwise residual separation does not imply finite index.  One may have
infinitely many context states distinguishable only by tests of increasing
length, as in nonregular language theory.

Thus a Myhill-Nerode argument proves Sawin only if one proves:

```text
the orbit-relevant contextual behavior relation has finite index.
```

This is the finite-index contextual rigidity lemma.

## Escape Holonomy

Escape-holonomy separation may record more than finite two-sided context
states.  It can include transporter/stabilizer cosets in an action groupoid,
for example elements or cosets in `As(C_M(X))`.

To become a finite rack detector, escape holonomy must factor through finite
data satisfying:

```text
1. a finite holonomy quotient;
2. compatibility with the rack crossing law;
3. uniform separation of all orbit-relevant nontrivial holonomies from
   stabilizers.
```

Residual rigidity does not currently imply these facts.

## Strongest Valid Conditional Theorem

The strongest usable theorem is:

```text
If the residual-rigid reduction has finite-index orbit-relevant contextual
behavior, and the finitely many resulting stabilizer cosets are uniformly
profinitely separated, then one finite rack detector exists and Sawin follows
for X.
```

Equivalently, prove one of:

```text
bounded bad witnesses;
finite-index contextual Nerode relation;
no profinite scattering plus uniform stabilizer separation plus finite
holonomy;
tower failure gives a finite crossing-compatible active factor.
```

The current data prove none of these.  The exact obstruction is:

```text
pointwise residual separation does not imply finite-index contextual behavior.
```

## Current Missing Lemma

Finite-index contextual rigidity lemma:

```text
For residual-rigid X, every orbit-relevant profinite contextual collapse
factors through one finite quotient of L_X, and the resulting finite contextual
collapse is crossing-compatible and finite-rack separable.
```

This lemma is strictly smaller than Sawin and targets exactly the current
obstruction.

