# Clopen Core Compactness Obstruction

Date: 2026-06-05

This note records the negative result for the proposed context-stable clopen
core lemma.  The lemma is a correct target, but it is not a consequence of
compactness, Higman's lemma, Stone duality, profinite semigroup theory, or
ordinary automata theory.

The exact obstruction is:

```text
weak bounded subwords do not imply bounded cores with the same surrounding
contextual states.
```

Compactness gives limiting profinite contextual collapse.  It does not give a
finite quotient, a finite clopen cover, or a finite active factor.

The sharp missing theorem remains a finite extraction dichotomy:

```text
Every orbit-relevant harmful profinite contextual collapse is finite-rack
absorbed or finite-active-factor extractable.
```

## Context-Stable Cores

Let

```text
K=hat{L_X} x X x hat{L_X}.
```

For a word

```text
x=(x_1,...,x_n),
```

define

```text
kappa_i(x)=(
  lambda_{x_1}...lambda_{x_{i-1}},
  x_i,
  lambda_{x_{i+1}}...lambda_{x_n}
) in K.
```

For a pair

```text
omega=(x,x') in X^n x X^n,
```

define

```text
Delta_i(omega)=(kappa_i(x),kappa_i(x')) in K^2.
```

For `I=(i_1<...<i_m)`, put

```text
Delta_I(omega)=(
  Delta_{i_1}(omega),
  ...,
  Delta_{i_m}(omega)
) in (K^2)^m.
```

A context-stable core of size `m` is a clopen subset

```text
C subset (K^2)^m.
```

A bad pair `omega` contains `C` if `Delta_I(omega) in C` for some increasing
index set `I`.

A detector

```text
D=(M,phi)
```

induces a continuous label map

```text
ell_D:K -> Y
```

by

```text
ell_D(ahat,x,bhat)=phi(d_{theta(ahat),x,theta(bhat)}).
```

The detector `D` separates `C` if every tuple

```text
((xi_1,eta_1),..., (xi_m,eta_m)) in C
```

has some coordinate `j` with

```text
ell_D(xi_j) != ell_D(eta_j).
```

This is the right stability notion: the core remembers full left and right
context, so separation of the core separates every occurrence inside arbitrary
surrounding observer words.

Indeed, if `Occ(C)` is the set of bad pairs containing `C`, then

```text
D separates C  =>  Occ(C) cap B_D = empty.
```

If `omega in B_D`, all corresponding contextual pairs have equal `D`-labels,
so no selected subtuple can lie in a core separated by `D`.

## Why The Core Lemma Is Already The Hard Theorem

A harmful ultrafilter `U` satisfies

```text
B_D in U
```

for every finite detector `D`.

If `D` separates a core `C`, then

```text
Occ(C) cap B_D = empty.
```

Therefore

```text
Occ(C) notin U.
```

So a theorem asserting that every harmful ultrafilter contains a
detector-separated core immediately contradicts harmfulness.  It is not a
routine compactness consequence; it is exactly a proof that harmful
ultrafilters do not exist.

Equivalently:

```text
context-stable separated-core lemma
=> one finite contextual rack detector.
```

The lemma remains a valid target, but it is the missing uniformity theorem.

## Stone Duality Does Not Produce The Cover

Let `beta Omega` be the Stone space of ultrafilters on the bad-pair set
`Omega`.  The set of harmful ultrafilters is

```text
H = intersection_D closure(B_D).
```

Products of detectors satisfy

```text
B_{D_1 x D_2}=B_{D_1} cap B_{D_2}.
```

Hence if every detector fails, the family `{B_D}` has the finite intersection
property and `H` is nonempty.

Compactness says that if `H` is covered by open sets, then finitely many open
sets suffice.  But detector-separated cores do not cover `H`.  They are
disjoint from `H`, since a harmful ultrafilter contains every `B_D`.

Therefore Stone duality does not give a finite clopen cover.  To obtain such
a cover one must first prove that every allegedly harmful ultrafilter is
actually non-harmful or active-factor extractable.

## Higman Still Gives Only Weak Boundedness

For fixed finite `M`, one may enrich each letter by contextual state

```text
(a,x,b) in M x X x M.
```

Higman's lemma then applies to sequences over the finite alphabet

```text
(M x X x M)^2.
```

This does not prove context-stable cores.

First, deleting observer strands changes contexts.  A retained visible letter
may have label

```text
d_{a,x,b}
```

inside the long word but label

```text
d_{a',x,b'}
```

as a standalone subword.

Second, braid reachability is not hereditary under deletion.  A braid path
may use deleted strands to alter retained colors or contexts before those
strands are forgotten.

Third, state-refinement escape uses the infinite profinite alphabet `K`, not
one finite alphabet `M x X x M`.

Thus:

```text
Higman gives weak bounded subsequences, not context-stable bounded clopen
cores.
```

## Compact Profinite Factorial Model

A simple model shows why compactness does not force finite clopen cores.

Let

```text
K=hat{Z}
```

and let finite detectors be reductions

```text
q_m:hat{Z} -> Z/mZ.
```

Let

```text
Omega=N,
Delta(n)=(0,n!) in K^2.
```

For each `m`,

```text
q_m(0)=q_m(n!)
```

for all sufficiently large `n`, because `m` divides `n!`.  Therefore the bad
set for `q_m` is cofinite.

A nonprincipal ultrafilter containing all cofinite sets is harmful with
respect to all finite quotients `q_m`.  The limiting relation is `(0,0)`,
which is closed.  Any finite detector-separated clopen core would have to
detect inequality modulo some `m`, but `Delta(n)` is eventually equal modulo
every `m`.

Thus no detector-separated clopen core lies in the ultrafilter.

This is the abstract state-refinement or factorial-prefix obstruction:

```text
every fixed finite quotient is eventually defeated, while the profinite limit
is closed but not finite-index.
```

This model is not yet an orbit-relevant YBE counterexample.  It shows only
that the finite clopen core theorem cannot follow from compactness alone.

## Harmless YBE-Origin Non-Finite-Index Model

There is also a harmless YBE-origin model.

Take the one-point solution

```text
X={*}.
```

Then

```text
L_X=<lambda>.
```

For finite cyclic quotients `M=C_m`, the contextual rack `C_M(X)` is the free
quandle on `m` generators indexed by

```text
a+b mod m.
```

In the profinite limit, contextual equality remembers the profinite sum

```text
ahat + bhat.
```

The relation

```text
ahat+bhat = ahat'+bhat'
```

is closed but not pulled back from any single finite quotient.

This is harmless because `X^n` has one point and

```text
Omega_n=empty
```

for every `n`.  It proves only that YBE contextual structure alone does not
imply global finite-index `E_infty`.  The remaining issue is orbit relevance.

## Fixed-M And State-Refinement Obstructions

After the finite endpoint set `Sbar_M` has been separated, fixed-`M` badness
is exactly

```text
x != x',
x' in B_n.x,
Theta_n^M(x)=Theta_n^M(x').
```

The equality relation is regular, but the braid-orbit relation need not be.
Therefore regularity of exact label equality does not give bounded harmful
witnesses.

A harmful fixed-`M` ultrafilter would be supported on exact `Theta^M`
collisions in unbounded arity and remain bad for every other finite detector.
Current tools neither construct nor rule out such a residual-rigid finite YBE
example.

For state refinement, define

```text
E_infty =
intersection_M (q_M x q_M)^(-1)(E_M)
subset K^2.
```

This is closed.  The missing finite-index theorem would assert that, on
orbit-relevant contexts, `E_infty` is pulled back from one finite quotient
`M_0`.  Compactness gives closedness, not finite index.

The factorial model is the prototype:

```text
for every fixed M, exact Theta^M-collisions occur eventually, but no single M
works for all arities.
```

## Hidden Holonomy Remains Diagnostic Without Uniform Separation

Fix `M`, put

```text
R=C_M(X),  G=As(R).
```

If a marked strand has escape cocycle `g` and endpoint label `r`, then the
final endpoint is `g.r`.  If endpoint labels are equal, then

```text
g in H_r=Stab_G(r).
```

A finite contextual rack detector sees only `r`; it does not distinguish
different elements of `H_r`.

To make holonomy a finite detector, one needs finite path data, for instance a
finite quotient of the reachable escape groupoid separating orbit-relevant
holonomy data.  A sufficient condition is uniform separability:

```text
closure(T) cap closure(H) = empty
```

for every relevant transporter family `T` and stabilizer `H`.  If the
closures meet, holonomy remains profinite diagnostic data.  It does not
automatically yield a finite rack detector or a finite active factor.

## Active-Factor Extraction Is An Additional Theorem

Suppose a finite-index contextual collapse is represented by finite data

```text
theta:L_X -> M,
Z,
pi_{a,b}:X -> Z.
```

For `r_X(x,y)=(u,v)`, define `Gamma subset Z^2 x Z^2` by

```text
A=pi_{a,lambda_y b}(x),
B=pi_{a lambda_x,b}(y),
C=pi_{a,lambda_v b}(u),
D=pi_{a lambda_u,b}(v).
```

This gives a finite active YBE factor exactly if:

```text
Gamma is functional;
every pair in Z^2 occurs as an input;
the induced r_Z:Z^2 -> Z^2 is bijective;
r_Z satisfies YBE on all of Z^3;
the maps Pi_n are braid-equivariant;
ker rho_n^Z <= ker rho_n^X for all n.
```

Orbit-injectivity of `Pi_n` on braid orbits is a sufficient condition for the
kernel inclusion.

A harmful ultrafilter does not force these properties.  It gives a limiting
nonseparation phenomenon, which may be infinite-index, nonfunctional, partial,
nonbijective, YBE-valid only on reachable triples, or not kernel-reflecting.

Thus finite active extraction is an independent theorem.

## Finite Extraction Dichotomy

The clean theorem that would close the route is:

```text
Finite extraction dichotomy.

Let X be finite bijective.  Suppose every unbounded bad-pair ultrafilter U
satisfies one of:

Alternative A: finite rack absorption.
  There exists a finite detector D with Omega \ B_D in U.
  A sufficient mechanism is a bounded context-stable clopen core separated by D.

Alternative B: finite active-factor extraction.
  The profinite contextual collapse associated to U factors through finite
  data (M,Z,pi_{a,b}) such that Gamma is functional, total, bijective,
  satisfies YBE on all of Z^3, gives braid-equivariant Pi_n, and satisfies
  ker rho_n^Z <= ker rho_n^X for all n.
```

If no finite detector works, choose a harmful ultrafilter `U` with

```text
B_D in U
```

for all `D`.  Alternative A is impossible for such `U`, because it gives
`Omega \ B_D in U` for some `D`.  Alternative B gives a proper active factor,
contradicting residual rigidity.  Therefore no harmful ultrafilter exists and
some finite detector works.

## Final Boundary

The context-stable clopen core lemma is correct but is not obtained from
compactness or WQO arguments.  A harmful ultrafilter, by definition, avoids
every detector-separated core.

The exact obstruction is:

```text
a closed profinite contextual collapse may be orbit-relevant but not clopen
finite-index.
```

Such a collapse may come from factorial prefix/state-refinement behavior or
profinite reachable holonomy.  It is harmless if it is ambient only, as in the
one-point/free-quandle model, or if a rack branch absorbs it.  It becomes
dangerous only when realized by actual same-orbit bad pairs and surviving all
finite detectors.

The sharp missing lemma, strictly smaller than Sawin, is:

```text
Every orbit-relevant harmful profinite contextual collapse is finite-rack
absorbed or finite-active-factor extractable.
```
