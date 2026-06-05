# Braid Reachability Context-Stable Boundary

Date: 2026-06-05

This note records the boundary after separating endpoint label equality from
braid-orbit reachability.  There are three different relations in play:

```text
Theta_n^M(x)=Theta_n^M(x')              fixed-M endpoint-label equality,
x' in B_n.x                             braid-orbit reachability,
one finite detector works for all n      uniformity over arities and states.
```

For fixed finite `M`, endpoint equality is finite-state and regular.  The
difficult relation is braid reachability, and the real obstruction to one
finite detector is a uniformity condition over all arities and all finite
state quotients.

The next missing theorem is not ordinary regularity of braid orbits.  That is
false in general.

## Braid-Orbit Reachability Is Not Regular In General

Let

```text
O_X={(x,x'): x' in B_n.x for some n}.
```

This is the reachability relation for the reversible length-preserving local
rewrite system

```text
xy <-> uv whenever r_X(x,y)=(u,v).
```

For each fixed `n`, the relation on `X^n x X^n` is decidable by finite graph
search.  But as `n` varies, `O_X` need not be synchronously regular.

The simplest counterexample is the flip solution

```text
r(x,y)=(y,x)
```

on `X={0,1}`.  This solution is finite, bijective, involutive,
nondegenerate, and is the rack solution of the trivial rack.

Here `B_n` acts by permuting coordinates.  Hence

```text
x' in B_n.x
```

if and only if `x` and `x'` have the same number of `0`s and the same number
of `1`s.

If `O_X` were synchronously regular, intersecting it with the regular
convolution language

```text
(0,1)^*(1,0)^*
```

would still be regular.  A word in this convolution language has the form

```text
conv(0^a 1^b, 1^a 0^b).
```

The two words have the same Parikh vector if and only if `a=b`.  Thus the
intersection is

```text
{(0,1)^n(1,0)^n : n >= 0},
```

which is not regular.  Contradiction.

Therefore the braid-orbit relation is not regular even in a completely solved
positive branch.  A proof of Sawin cannot rely on general regularity or
automaticity of `O_X`.

## What YBE Supplies

Let `r_i` act on coordinates `i,i+1`.  The Yang-Baxter equation gives

```text
r_i r_{i+1} r_i = r_{i+1} r_i r_{i+1},
```

and distant generators commute:

```text
r_i r_j = r_j r_i,  |i-j| >= 2.
```

Thus the local rewrites define a braid group action.

This is not confluence.  The rewrite system is symmetric and length
preserving, so there is no natural terminating orientation.  YBE gives
consistency of braid moves, not a finite normal form for arbitrary orbits.

Extra hypotheses can help in special classes.  If `r^2=id`, the action
factors through the symmetric group, but the flip rack shows that the orbit
relation can still be nonregular.  If the structure monoid is cancellative,
Garside, or embeds in a good structure group, one may get word-problem
algorithms or normal forms.  This still does not imply finite-state orbit
reachability over all arities, and it does not give a uniform contextual
detector.

Thus:

```text
YBE gives braid consistency, not finite-state orbit reachability.
```

## Fixed-M Exact Label Equality Is Regular

Fix finite `M`.  Define

```text
E_M subset (M x X x M)^2
```

by

```text
(a,x,b) E_M (a',x',b')
iff
d_{a,x,b}=d_{a',x',b'} in C_M(X).
```

For

```text
x=(x_1,...,x_n),
x'=(x'_1,...,x'_n),
```

the equality

```text
Theta_n^M(x)=Theta_n^M(x')
```

is equivalent to the existence of finite annotations

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

(a_i,x_i,b_i) E_M (a'_i,x'_i,b'_i) for all i.
```

Since `M` and `X` are finite, these are finite automaton constraints.  Hence
the relation

```text
C_M={ (x,x') : Theta_n^M(x)=Theta_n^M(x') }
```

is regular over the alphabet `X x X`.

The fixed-`M` bad relation is

```text
B_M=C_M cap O_X cap {x != x'}.
```

The label part is regular.  The orbit part need not be.  Therefore regularity
of `C_M` does not prove bounded bad witnesses.

## Weak Boundedness Versus Useful Boundedness

There is a weak boundedness statement that is formally true but useless here.
Since `X x X` is finite, Higman's lemma implies that every subset of
`(X x X)^*` has finitely many minimal elements under the subsequence order.
Thus, for fixed `M`, the bad set `B_M` has finitely many subsequence-minimal
elements.

This does not produce a finite detector.

The problem is contextual dependence.  If a long bad pair contains a short bad
subsequence `(y,y')`, a detector separating `(y,y')` in its own arity need not
separate the original long pair, because the selected letters occur with
different left and right context states:

```text
a_i=theta(lambda_{x_1}...lambda_{x_{i-1}}),
b_i=theta(lambda_{x_{i+1}}...lambda_{x_n}).
```

Deleting observer strands changes these states.  Therefore separation of a
short standalone pair does not lift to separation of the long pair.

There are two notions:

```text
weak boundedness:
  every bad pair contains a bounded bad subsequence;

useful boundedness:
  every long harmful pair contains a bounded core whose separation is stable
  under arbitrary surrounding contexts.
```

Only useful boundedness proves a finite detector.  The missing theorem is a
context-stable bounded core theorem, not a Higman finite-basis statement.

## Fixed-M Unbounded Exact Collisions

For fixed `M`, after endpoint separation of

```text
Sbar_M={d_{a,x,b}:a,b in M, x in X},
```

a same-orbit pair is bad exactly when

```text
Theta_n^M(x)=Theta_n^M(x').
```

Unbounded exact collisions can occur for coarse `M`.  For example, with
`M=1`, the contextual rack relations may identify many generators `d_x`, so
distinct same-orbit words can have identical `Theta^1` labels in arbitrarily
large arity.

This is not automatically harmful.  A finer state quotient `M'`, or a
different finite rack detector, may separate the pair.  A genuinely harmful
fixed-`M` obstruction would require unbounded exact collisions that survive
every finite detector on an ultrafilter-large subsequence.

Current tools do not construct such a finite residual-rigid YBE example, but
they also do not rule it out.  The precise obstruction to proving boundedness
is:

```text
deleting observer strands changes the contextual states that caused the
equality.
```

Thus braid locality does not give a bounded bad core.

## State-Refinement Escape

Let

```text
K=hat{L_X} x X x hat{L_X}.
```

For each finite quotient `q_M:L_X -> M`, define

```text
q_M:K -> M x X x M
```

by projecting both profinite context coordinates.

Let `E_M` be exact equality of contextual generators in `C_M(X)`.  Define

```text
E_infty =
intersection_M (q_M x q_M)^(-1)(E_M).
```

This is a closed relation on the profinite space `K`.

The required finite-index theorem is:

```text
There exists M_0 such that, on orbit-relevant contextual letters,
E_infty=(q_{M_0} x q_{M_0})^(-1)(E_{M_0}).
```

This says that orbit-relevant contextual equality is clopen and finite-index.

Compactness does not imply this.  Equality on a profinite completion is the
basic model: every distinct pair of ordinary points is separated by some
finite quotient, but equality itself is not determined by one finite quotient.

Thus `E_infty` can fail to be finite-index in principle.  The Sawin-relevant
question is whether this failure can occur on orbit-relevant contextual
letters of a finite residual-rigid YBE solution.  Current hypotheses do not
decide it.

The sharp profinite obstruction is:

```text
a harmful ultrafilter converges to a closed contextual equality relation that
is not clopen finite-index.
```

## Observer-Corridor Mechanism

The proposed state-refinement mechanism is:

```text
lambda_o^k remains distinguishable in L_X;
finite quotients see only long periods;
active letters p,q collapse at prefix state lambda_o^k;
a braid corridor realizes o^k p (...) -> o^k q (...);
k=n! defeats every fixed finite quotient.
```

A simple corridor controlled only by iterating a visible color permutation is
finite-state.  If moving an active color through `o^k` is governed by a fixed
permutation `T_o:X -> X`, then `T_o^k` has period at most `|X|!`.

But this does not rule out the general mechanism.  The observer word may carry
context through the monoid element `lambda_o^k` even when visible colors are
periodic.  The equality

```text
d_{lambda_o^k,p,b}=d_{lambda_o^k,q,b}
```

is contextual equality, not merely color equality.

The YBE identity guarantees that braid decompositions are consistent.  It
does not force the sequence `lambda_o^k` to have bounded period in `L_X`, nor
does it force all prefix-dependent contextual equalities to be finite-index.

To rule out observer corridors one needs one of:

```text
finite-index contextual Myhill-Nerode,
context-stable bounded harmful witnesses,
uniform reachable holonomy separation,
active-factor extraction.
```

## Hidden Holonomy After Endpoint Equality

Fix `M`, put

```text
R=C_M(X),
G=As(R).
```

Let a marked strand follow a braid trajectory with reachable escape cocycle
`g in G`.  If its endpoint contextual label is again `r`, then

```text
g.r=r,
```

so

```text
g in H_r=Stab_G(r).
```

A finite contextual rack detector sees only the endpoint element `r`; it does
not see which element of `H_r` occurred.  Stabilizer/path holonomy therefore
cannot separate exact `Theta^M` collisions at fixed `M`.

Escape holonomy can still be diagnostic.  It becomes a finite detector only
after enriching endpoint labels by finite holonomy data.  That requires an
additional finite quotient of a holonomy groupoid and a uniform separation
condition.  If the holonomy remains profinite, it need not define a finite
active factor.

## Active-Factor Extraction Conditions

Let `M` be finite, `Z` finite, and suppose maps

```text
pi_{a,b}:X -> Z
```

are given.  For `r_X(x,y)=(u,v)`, define

```text
(A,B) Gamma (C,D)
```

if

```text
A=pi_{a,lambda_y b}(x),
B=pi_{a lambda_x,b}(y),
C=pi_{a,lambda_v b}(u),
D=pi_{a lambda_u,b}(v).
```

This data gives a finite active YBE factor exactly when:

```text
1. Gamma is functional;
2. every pair in Z^2 occurs as an input;
3. the induced map r_Z:Z^2 -> Z^2 is bijective;
4. r_Z satisfies YBE on all of Z^3;
5. the maps Pi_n are braid-equivariant;
6. ker rho_n^Z <= ker rho_n^X for all n.
```

Orbit-injectivity of `Pi_n` on braid orbits is a clean sufficient condition
for the kernel inclusion.

Exact contextual collapse alone does not force any of these properties.  It
may be infinite-index, nonfunctional, partial, nonbijective, invalid on
unreached triples, or non-kernel-reflecting.  Ordinary quotients or contextual
equivalence classes cannot be used as active factors unless the kernel
direction is proved.

## Strongest Valid Theorems

The current valid endpoints are:

```text
Theorem A: Fixed-M endpoint reduction.
If Sbar_M is separated by one finite rack quotient, then badness for that
detector is exactly Theta_n^M(x)=Theta_n^M(x') inside a braid orbit.

Theorem B: Regular label equality.
For fixed M, exact contextual label equality is regular, but braid-orbit
reachability need not be regular.  Therefore regular label equality does not
imply bounded harmful witnesses.

Theorem C: Context-stable bounded witnesses imply a finite detector.
If every harmful exact contextual collapse contains a bounded bad core whose
separation is stable under arbitrary surrounding observers, then finite
products of pointwise detectors give one finite detector.

Theorem D: Finite-index contextual Myhill-Nerode implies a finite detector.
If orbit-relevant E_infty is pulled back from one finite quotient M_0, and
the resulting labels are rack-separated and orbit-injective, then a finite
contextual rack detector exists.

Theorem E: Active extraction implies residual-rigid Sawin.
If every harmful exact/profinite contextual collapse is finite-rack absorbed
or yields a proper finite active factor Z with ker rho_n^Z <= ker rho_n^X
for all n, then residual rigidity closes the branch.
```

## Final Boundary

The next missing theorem is not ordinary regularity of braid orbits.  The
flip rack already shows that this is false.

The possible missing inputs are, in increasing strength:

```text
context-stable bounded harmful witnesses,

finite-index contextual Myhill-Nerode behavior,

active-factor extraction from unbounded exact contextual collapse.
```

The sharpest formulation is:

```text
Every harmful unbounded exact contextual collapse is either detected by a
finite contextual rack quotient, or factors through finitely many context
states in a crossing-compatible and kernel-reflecting way.
```

This lemma is strictly smaller than Sawin and isolates the unresolved part of
the contextual detector route.
