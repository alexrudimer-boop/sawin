# Context-Stable Clopen Core Boundary

Date: 2026-06-05

This note records the sharpened formulation of the useful bounded-witness
principle.  The missing theorem is not ordinary regularity of braid orbits,
and it is not weak boundedness under subsequences.  It must be a
context-stable statement on contextual triples.

The current target is:

```text
Every harmful unbounded exact contextual collapse is either finite-rack
absorbed or finite-active-factor extractable.
```

Equivalently, one needs either a bounded family of context-stable clopen cores
that finite detectors separate, or a finite-index crossing-compatible collapse
that produces a proper kernel-reflecting active factor.

## Contextual Alphabet

Let

```text
K=hat{L_X} x X x hat{L_X}.
```

For a word

```text
x=(x_1,...,x_n),
```

define its profinite contextual letter at position `i` by

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

For an increasing index set

```text
I=(i_1<...<i_m),
```

put

```text
Delta_I(omega)=(
  Delta_{i_1}(omega),
  ...,
  Delta_{i_m}(omega)
) in (K^2)^m.
```

The key point is that the retained letters remember their full surrounding
left and right observer contexts.  This is the data that is lost when one
passes to a short standalone subword.

## Context-Stable Cores

A context-stable core of size `m` is a clopen subset

```text
C subset (K^2)^m.
```

A bad pair `omega` contains `C` if

```text
Delta_I(omega) in C
```

for some increasing index set `I` of size `m`.

Let

```text
D=(M,phi)
```

be a finite contextual rack detector.  It induces a continuous label map

```text
ell_D:K -> Y
```

by

```text
ell_D(ahat,x,bhat)=
phi(d_{theta(ahat),x,theta(bhat)}).
```

The detector `D` separates the core `C` if for every tuple

```text
((xi_1,eta_1),..., (xi_m,eta_m)) in C
```

there exists some `j` such that

```text
ell_D(xi_j) != ell_D(eta_j).
```

This is the correct stability notion.  Since `C` is defined using full
contextual triples, if `D` separates `C`, then `D` separates every occurrence
of `C` inside arbitrary surrounding observer words.

## Useful Bounded Core Lemma

The desired bounded theorem should have the following form.

There exist

```text
N=N(X),
C_1,...,C_t with C_j subset (K^2)^{m_j}, m_j <= N,
finite detectors D_1,...,D_t,
```

such that:

```text
1. every harmful bad pair contains some C_j;
2. D_j separates C_j.
```

Then the product detector

```text
D=D_1 x ... x D_t
```

separates every harmful bad pair.  Therefore no harmful ultrafilter exists.

This is stronger than saying that every long bad pair contains a short bad
subsequence.  It is a bounded theorem for contextual triples and finite
detector labels, not for visible subwords alone.

## Why Higman Does Not Prove It

For fixed finite `M`, one can enrich each position by finite contextual data

```text
(a,x,b) in M x X x M.
```

Then Higman's lemma applies to sequences over the finite alphabet

```text
(M x X x M)^2.
```

This does not prove the needed theorem.

First, contextual states are not hereditary under deletion.  If a long pair
contains a short visible subpair, deleting the surrounding observer letters
changes the retained prefix and suffix states:

```text
d_{a,x,b} in the long word
```

may become

```text
d_{a',x,b'}
```

in the standalone subword, with `(a,b) != (a',b')`.  A detector separating the
short standalone pair need not separate the long occurrence.

Second, braid reachability is not hereditary under deletion.  A braid path
from `x` to `x'` may use strands that are later deleted.  Those deleted
strands may alter the colors and contexts of the retained strands before
being forgotten.  Thus a same-orbit long pair need not contain a same-orbit
short subpair.

Third, for state-refinement escape the correct alphabet is the profinite
space

```text
K=hat{L_X} x X x hat{L_X},
```

not one finite alphabet `M x X x M`.  Higman's lemma on finite alphabets does
not yield finite-index clopen behavior on `K`.

Thus:

```text
wqo gives weak subsequence minimality, not context-stable bounded cores.
```

## Braid Orbits Are Not Regular In General

The braid-orbit relation

```text
O_X={ (x,x') : x' in B_n.x }
```

is not synchronously regular in general.

For the flip solution

```text
X={0,1},
r(x,y)=(y,x),
```

the braid group acts by permuting coordinates.  Hence `x` and `x'` are in the
same orbit if and only if they have the same Parikh vector.

If `O_X` were synchronously regular, intersecting it with the regular
convolution language

```text
(0,1)^*(1,0)^*
```

would give the language

```text
{(0,1)^n(1,0)^n:n>=0},
```

which is not regular.  Contradiction.

This example is harmless because the flip solution is already a rack solution.
Taking `Y=X` gives

```text
ker rho_n^Y = ker rho_n^X
```

for all `n`.  Therefore nonregular orbit behavior is not itself harmful.  It
becomes relevant only when it interacts with contextual label collapse that is
not rack-absorbed.

## Fixed-M Exact Collisions

For fixed finite `M`, exact contextual equality

```text
Theta_n^M(x)=Theta_n^M(x')
```

is regular.  Define

```text
E_M subset (M x X x M)^2
```

by

```text
(a,x,b) E_M (a',x',b')
iff
d_{a,x,b}=d_{a',x',b'} in C_M(X).
```

Then equality of `Theta^M` labels is recognized by finite annotations

```text
a_i,a'_i,b_i,b'_i in M
```

satisfying prefix and suffix transition recurrences and the pointwise
condition `E_M`.

The fixed-`M` bad relation is

```text
B_M={
  x != x',
  x' in B_n.x,
  Theta_n^M(x)=Theta_n^M(x')
}.
```

The label part is regular.  The orbit part need not be.  A harmful fixed-`M`
ultrafilter would be a nonprincipal ultrafilter supported on `B_M`, with
unbounded arity, after the finite endpoint set `Sbar_M` has already been
separated.

Current tools do not construct such an example inside a residual-rigid finite
YBE solution, but they do not rule it out.  The missing fixed-`M` theorem is:

```text
For every finite M, every harmful fixed-M exact collision contains a bounded
context-stable core.
```

## State-Refinement Escape

Let

```text
q_M:K -> M x X x M
```

be the projection induced by a finite quotient of `L_X`.  Define

```text
E_infty =
intersection_M (q_M x q_M)^(-1)(E_M)
subset K^2.
```

This is a closed profinite contextual equality relation.

The needed finite-index theorem is:

```text
There exists M_0 such that, on orbit-relevant contextual letters,
E_infty=(q_{M_0} x q_{M_0})^(-1)(E_{M_0}).
```

Compactness does not imply this.  A closed relation on a profinite space need
not be pulled back from one finite quotient.

There is a harmless YBE-origin model showing global non-finite-index behavior.
For the one-point solution `X={*}`,

```text
L_X=<lambda>.
```

For finite cyclic quotients `M=C_m`, the contextual rack `C_M(X)` is the free
quandle on `m` generators indexed by the sum of left and right context states.
In the profinite limit, the relation remembers a profinite sum

```text
ahat+bhat.
```

Equality of such profinite sums is closed but not pulled back from any single
finite quotient.  This is harmless because `Omega_n` is empty for every `n`.
It nevertheless shows that YBE-origin contextual racks do not force
`E_infty` to be finite-index globally.

The sharp obstruction is:

```text
harmful orbit-relevant E_infty may be closed profinite but not clopen
finite-index.
```

## Observer Corridors

The proposed observer-corridor mechanism is:

```text
lambda_o^k remains distinguishable in L_X;
finite quotients see long periods;
active letters p,q collapse at prefix state lambda_o^k;
a braid corridor realizes o^k p (...) -> o^k q (...);
k=n! defeats every fixed finite quotient.
```

Visible color dynamics alone cannot carry unbounded information if the
corridor is only repeated interaction with a fixed observer color.  Since `X`
is finite, visible active-color evolution is eventually periodic, and often
periodic with bounded period.

But contextual labels contain the prefix monoid state `lambda_o^k`.  The
sequence `lambda_o^k` need not have bounded period in `L_X` or in its
profinite completion.  YBE imposes homogeneous relations

```text
lambda_x lambda_y = lambda_u lambda_v
```

when `r_X(x,y)=(u,v)`, but does not force `lambda_o` to have finite order.
Nor does it imply confluence, bounded derivations, finite normal forms, or
finite-index contextual equality.

Thus visible color periodicity does not rule out unbounded prefix-context
information.  To exclude observer corridors one needs one of the global
missing principles:

```text
context-stable bounded witnesses,
finite-index contextual Myhill-Nerode,
uniform reachable holonomy separation,
active-factor extraction.
```

## Hidden Holonomy After Endpoint Equality

Fix `M`, put

```text
R=C_M(X),
G=As(R).
```

A marked strand following a braid trajectory has escape cocycle `g in G`.
If its initial endpoint label is `r`, the final endpoint label is `g.r`.  If
endpoint labels are equal, then

```text
g.r=r,
```

so

```text
g in H_r=Stab_G(r).
```

Finite contextual rack detectors see only `r`; they cannot distinguish
different elements of `H_r`.  Thus stabilizer holonomy cannot separate exact
`Theta^M` collisions at fixed `M`.

To convert holonomy into a finite detector, one must enlarge the detector to
remember finite path data.  The needed condition is uniform separability in
the reachable escape groupoid:

```text
for every orbit-relevant transporter family T and stabilizer H,
closure(T) cap closure(H) = empty
```

inside the appropriate profinite completion.  If the closures meet, holonomy
remains profinite diagnostic data and does not automatically produce a finite
active factor.

## Active-Factor Extraction

Suppose finite `M`, finite `Z`, and maps

```text
pi_{a,b}:X -> Z
```

are given.  For `r_X(x,y)=(u,v)`, define

```text
(A,B) Gamma (C,D)
```

if there exist `a,b,x,y` such that

```text
A=pi_{a,lambda_y b}(x),
B=pi_{a lambda_x,b}(y),
C=pi_{a,lambda_v b}(u),
D=pi_{a lambda_u,b}(v).
```

This data defines a finite active YBE factor exactly if:

```text
1. Gamma is functional;
2. every pair in Z^2 occurs as an input;
3. the induced map r_Z:Z^2 -> Z^2 is bijective;
4. r_Z satisfies YBE on all triples in Z^3;
5. the maps Pi_n are braid-equivariant;
6. ker rho_n^Z <= ker rho_n^X for all n.
```

Orbit-injectivity of `Pi_n` on braid orbits is a sufficient condition for the
kernel inclusion.

Exact contextual collapse alone does not force these conditions.  It can be
infinite-index, nonfunctional, partial, nonbijective, YBE-valid only on
reachable triples, or non-kernel-reflecting.

## Strongest Valid Schema

The precise combined theorem schema is:

```text
Context-stable finite extraction.

Let X be finite bijective.  Suppose every harmful ultrafilter of exact
contextual collapses satisfies one of:

Alternative A: finite rack absorption.
  There are finitely many context-stable clopen cores C_1,...,C_t of bounded
  size, and finite detectors D_1,...,D_t, such that the cores cover the
  harmful ultrafilter and D_j separates C_j.  The product detector absorbs
  the ultrafilter.

Alternative B: finite active-factor extraction.
  The harmful collapse factors through a finite quotient L_X -> M and finite
  maps pi_{a,b}:X -> Z such that the induced crossing is functional, total,
  bijective, YBE-valid on all triples, braid-equivariant, and
  kernel-reflecting.
```

For residual-rigid `X`, Alternative B is excluded if `Z` is proper, while
Alternative A gives a finite rack detector.  Hence this schema would close the
residual-rigid branch.

## Final Boundary

The next theorem should not be ordinary regularity of braid orbits; that is
false.  It should not be weak Higman boundedness; that is not stable under
observer contexts.

The sharp missing lemma is:

```text
Every harmful unbounded exact contextual collapse has a bounded
context-stable clopen core,
```

or, failing that,

```text
it is finite-index and active-factor extractable.
```

Equivalently:

```text
harmful profinite contextual collapse
=> finite rack absorption or proper kernel-reflecting active factor.
```

This lemma is strictly smaller than Sawin and is the exact remaining gap in
the contextual detector route.
