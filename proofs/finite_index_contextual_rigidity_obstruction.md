# Finite-Index Contextual Rigidity Obstruction

Date: 2026-06-05

This note records the obstruction identified after asking whether finite-index
contextual rigidity follows from the residual-rigid hypotheses.  The answer was
negative: the missing ingredient is not a computation, but a compactness or
noetherianity principle.

The exact gap is:

```text
pointwise finite separation of each fixed context
does not imply
finite-index contextual behavior over all arities.
```

The strongest valid reduction remains:

```text
finite-index contextual rigidity
=> one finite contextual rack detector
=> Sawin domination for X.
```

But finite-index contextual rigidity is not forced by ordinary YBE hypotheses,
nondegeneracy, residual finiteness of the left structure monoid, or pointwise
stabilizer separability.

## Conditional Detector Theorem

Let `L_X` be the positive left structure monoid and let

```text
theta:L_X -> M
```

be a finite quotient.  Let

```text
phi:C_M(X) -> Y
```

be a finite rack quotient.  If

```text
phi^n Theta_n^M:X^n -> Y^n
```

is injective on every braid orbit in every arity, then

```text
ker rho_n^Y <= ker rho_n^X
```

for every `n`.

Indeed, if `beta in ker rho_n^Y`, then for every word `x in X^n`,

```text
phi^n Theta_n^M(rho_n^X(beta)x)
=
rho_n^Y(beta) phi^n Theta_n^M(x)
=
phi^n Theta_n^M(x).
```

The two `X`-words lie in the same braid orbit, so orbit-injectivity forces
`rho_n^X(beta)x=x`.

Thus the detector theorem is sound.  The problem is producing one finite
detector that works in all arities.

## Pointwise Separation Is Not Uniform Separation

Let `B_M` be the set of same-orbit bad pairs not separated by the contextual
detector at finite state quotient `M`.  Refinement gives a decreasing family:

```text
M' refines M  =>  B_M' subset B_M.
```

Pointwise tower separation gives

```text
intersection_M B_M = empty.
```

Sawin requires

```text
there exists M with B_M empty.
```

These are not equivalent because the universe of bad pairs ranges over all
arities.  The model obstruction is

```text
B_N={m in N : m>N}.
```

The intersection is empty, but no individual `B_N` is empty.  In the
contextual tower, the integer `m` is replaced by required prefix/suffix context
length.

Therefore the missing principle is:

```text
long contextual badness has a bounded active core.
```

Equivalently, orbit-relevant contextual behavior must have finite
Myhill-Nerode index.

## Right-Separation Is Stronger Than Residual Finiteness

For `p,q in L_X`, define the profinite right equalizer

```text
E(p,q)={ahat in profinite_completion(L_X) : ahat p = ahat q}.
```

Then `E(p,q)=empty` iff there exists a finite quotient

```text
theta:L_X -> M
```

such that

```text
m theta(p) != m theta(q)
```

for every state `m in M`.

This is finite right-separation.  It separates the right translations by `p`
and `q` uniformly over all finite states.  Ordinary residual finiteness only
separates `p` and `q` at the identity state.

Several hypotheses do not imply finite right-separation:

```text
ordinary residual finiteness of L_X;
right nondegeneracy of X;
left and right nondegeneracy;
Green/Rees regularity of finite quotients;
residual-rigid core status unless finite right-separation is included.
```

Stronger group-like hypotheses can imply it.  If `L_X` embeds in a residually
finite group and `p != q` in that group, then a finite group quotient
separating `p` and `q` separates `mp` and `mq` for every state `m`, because
left multiplication is cancellative in groups.

Right cancellativity of `L_X` rules out actual equalizers `ap=aq`, but by
itself it does not rule out profinite equalizers.

## Nondegenerate Right-Scattering Example

YBE origin and nondegeneracy do not eliminate right scattering.

Let

```text
X={0,1},
r(i,j)=(j,1-i).
```

This is a constant-action solution `r(x,y)=(alpha(y),beta(x))` with
`alpha=id` and `beta` the flip.  Since `alpha` and `beta` commute, it satisfies
YBE.  It is bijective and nondegenerate: every `L_i` is the identity and every
`R_j` is the flip.

The left structure monoid relations are

```text
lambda_i lambda_j = lambda_j lambda_{1-i}.
```

In particular,

```text
lambda_0 lambda_0 = lambda_0 lambda_1,
```

while homogeneity leaves no length-one relation identifying `lambda_0` and
`lambda_1`.  Thus `lambda_0 != lambda_1`, but `lambda_0` is an actual
right-scattering state for the active pair `lambda_0,lambda_1`.

This example does not refute Sawin.  It shows only that nondegenerate YBE
structure alone cannot justify finite right-separation.

It also illustrates the danger of ordinary quotients.  The one-point quotient
does not dominate this solution: in arity two, the one-point braid action is
trivial, but

```text
sigma_1(0,0)=r(0,0)=(0,1) != (0,0).
```

So `sigma_1` lies in the one-point kernel but not in the kernel of `X`.

## A Special Pattern Ruled Out By Right Nondegeneracy

The earlier two-step fixed-right-output pattern

```text
ahat lambda_s = ahat lambda_x = ahat lambda_u,
r(s,y)=(x,y),
r(x,y)=(u,y),
u != x
```

is impossible when `R_y` is injective.  The first two equations imply
`R_y(s)=R_y(x)=y`, hence `s=x`, and then `u=x`, a contradiction.

This only rules out that special pattern.  General right scattering
`ahat p=ahat q` can still occur in nondegenerate examples.

## Why Bounded Bad Witnesses Do Not Follow From Locality

A bounded bad-witness theorem would say that every contextual bad pair contains
a bad subconfiguration of arity at most `N(X)`.  Such a theorem would convert
pointwise separation into one finite detector by a finite product over all
same-orbit pairs in arities at most `N(X)`.

The obstruction is that badness is not hereditary under deleting observer
strands.  The contextual label at position `i` depends on the full left and
right states

```text
a_i=theta(lambda_{x_1}...lambda_{x_{i-1}}),
b_i=theta(lambda_{x_{i+1}}...lambda_{x_n}).
```

Deleting an observer changes these states, so a collapse such as
`a_i p=a_i q` may disappear after any deletion.  Long observer words can be
essential to place a crossing at the equalizing state.

Braid locality does not repair this: the generator acts on adjacent letters,
but the contextual states of those letters depend on all letters to the left
and right.  Fadell-Neuwirth-style forgetting and product observers do not give
the needed hereditary property either.

## Active-Factor Extraction Obstruction

An infinite sequence of bad pairs can yield context-dependent equivalence
relations on `X`, indexed by profinite contexts:

```text
E_{ahat,bhat}.
```

To extract a finite domination-reducing active factor, the collapse must factor
through finitely many states and define a finite YBE solution.  Concretely, one
would need a finite set `Z`, finite context states, and maps

```text
pi_{a,b}:X -> Z
```

such that, for `r_X(x,y)=(u,v)`,

```text
r_Z(pi_{a,lambda_y b}(x), pi_{a lambda_x,b}(y))
=
(pi_{a,lambda_v b}(u), pi_{a lambda_u,b}(v)).
```

This formula must be well-defined on the two `Z` inputs, not on hidden choices
of `a,b,x,y`.  It must also extend to a total bijective YBE solution on all of
`Z^2`, not merely on reachable contextual pairs.

A profinite contextual collapse need not be finite-index, crossing-compatible,
or total.  Therefore tower failure does not automatically produce a proper
domination-reducing active factor.

## Infinite Myhill-Nerode Index

Finite automaton contextual detectors replace monoid states by finite left and
right state systems.  The relevant Myhill-Nerode relation identifies contexts
that no orbit-relevant continuation and braid test can distinguish.

A finite detector exists exactly when this behavioral relation has finite
index and is stable under context transitions.  Residual finiteness of `L_X`
does not imply finite index.  It separates fixed pairs of contexts, but it does
not imply that one finite automaton recognizes all orbit-relevant behavior.

Automaticity or finite normal forms would also be insufficient unless the
orbit-relevant contextual behavior itself has finite index.

## Uniform Stabilizer Separation

For a fixed `M`, let

```text
R=C_M(X),
G=As(R).
```

If `r'=g.r` and `H=Stab_G(r)`, finite rack quotients separate `r` and `r'`
only when finite quotients of `G` separate `g` from `H`.

Pointwise separability says each individual `g` is outside the profinite
closure of `H`.  Uniform separation of an infinite transporter family
`T subset G\H` requires one finite quotient separating all of `T` from `H`,
equivalently

```text
closure(T) cap closure(H) = empty
```

inside the profinite completion.

Pointwise separability does not imply this.  The model is

```text
G=Z,
H={0},
T={n! : n>=1}.
```

Every individual `n!` is separated from `0` by some finite quotient, but no
single finite quotient separates all of `T` from `0`.

Thus stabilizer separability must be strengthened to uniform transporter-family
separation unless bounded bad witnesses reduce the relevant transporter set to
a finite set.

## Green/Rees And Escape Holonomy

Green/Rees theory describes finite monoid quotients but does not force finite
right-separation.  Minimal ideals and recurrent classes can create equalizing
states rather than eliminate them.

Escape holonomy retains more data than two-sided context states: it records a
transporter or stabilizer coset in an action groupoid.  To convert that into a
finite rack detector one needs:

```text
finite holonomy states;
rack crossing compatibility;
uniform stabilizer-coset separation;
a finite rack quotient encoding the labels.
```

Without those, escape holonomy remains groupoid/profinite observer data rather
than a finite rack-determined detector.

## Current Missing Lemma

The current sharp target is:

```text
Residual-rigid X
=> finite-index, crossing-compatible, uniformly stabilizer-separable
   contextual behavior.
```

Equivalently, the residual branch must prove one of the following:

```text
bounded bad witnesses;
finite-index contextual Myhill-Nerode behavior;
no active profinite right-scattering plus uniform stabilizer separation;
tower failure implies a finite domination-reducing active factor.
```

None of these follows from the hypotheses currently recorded.  This is a
strictly smaller target than Sawin, but it remains the exact obstruction for
the contextual tower route.
