# Harmful Contextual Collapse Dichotomy

Date: 2026-06-05

This note records the correction after the residual right-separation audit.
Finite right-separation for all active pairs in `L_X` is too strong to be a
consequence of residual rigidity.  Right scattering can be harmless.

The correct target is:

```text
Residual rigidity must exclude harmful right scattering,
not all right scattering.
```

The new missing lemma is the harmful contextual collapse dichotomy:

```text
Every orbit-relevant profinite contextual collapse either
  (i) is absorbed by a finite contextual rack detector, or
  (ii) descends to a finite-index, crossing-compatible active factor Z
       satisfying ker rho_n^Z <= ker rho_n^X for every n.
```

If this dichotomy holds, residual rigidity excludes case (ii), while case (i)
gives Sawin domination.

## Right-Separation

For `p,q in L_X`, define

```text
E(p,q)={ahat in profinite_completion(L_X) : ahat p = ahat q}.
```

Then `E(p,q)=empty` iff there is a finite quotient

```text
theta:L_X -> M
```

such that

```text
m theta(p) != m theta(q)
```

for every `m in M`.

This is finite right-separation.  It is stronger than ordinary residual
finiteness of `L_X`.  Residual finiteness separates `p` and `q` at the identity
state; finite right-separation separates the right translations by `p` and `q`
at every finite state.

Group separation is a clean sufficient condition.  If there is a homomorphism

```text
gamma:L_X -> G
```

to a residually finite group with `gamma(p) != gamma(q)`, then a finite group
quotient separating `gamma(p)` and `gamma(q)` right-separates `p` and `q`,
because left multiplication in a group is cancellative.

The following do not imply finite right-separation by themselves:

```text
ordinary residual finiteness of L_X;
YBE origin;
nondegeneracy of X;
finite Green/Rees data of finite quotients;
pointwise stabilizer separability;
ordinary cancellativity, unless strengthened profinitely.
```

Thus the correct additional hypothesis is either finite right-separation for
the relevant active pairs or a harmless-scattering alternative.

## Harmless Scattering Example

Let

```text
X={0,1},
r(i,j)=(j,1-i).
```

This is a constant-action solution with `alpha=id` and `beta` the flip, so
YBE holds because `alpha beta=beta alpha`.  It is bijective and nondegenerate.

The left structure monoid relations are

```text
lambda_i lambda_j = lambda_j lambda_{1-i}.
```

In particular,

```text
lambda_0 lambda_0 = lambda_0 lambda_1,
```

while homogeneity gives no length-one relation identifying `lambda_0` and
`lambda_1`.  Hence `L_X` has actual right scattering:

```text
lambda_0 != lambda_1,
lambda_0 lambda_0 = lambda_0 lambda_1.
```

This scattering is harmless because `X` is itself a rack solution.  Use the
rack convention

```text
r_Y(a,b)=(b,b triangleright a).
```

Define

```text
j triangleright i = 1-i.
```

Then

```text
r_Y(i,j)=(j,j triangleright i)=(j,1-i)=r_X(i,j).
```

The rack maps are bijective and self-distributivity holds since
`t triangleright s=1-s` ignores the acting element.  Therefore taking `Y=X`
gives

```text
ker rho_n^Y = ker rho_n^X
```

for every `n`.

There is also a trivial contextual detector.  Take `M=1`.  Then `C_1(X)` has
generators `d_0,d_1`, and the map

```text
phi:C_1(X) -> X,
phi(d_i)=i
```

is a rack quotient.  Under this quotient,

```text
phi^n Theta_n^1(x_1,...,x_n)=(x_1,...,x_n),
```

so the labels are globally injective.

This example is a guardrail: no residual-rigid theorem should try to forbid
all right scattering unless already-rack-detected solutions have been removed.
The theorem must forbid only harmful scattering.

## What A Genuine Obstruction Would Need

A residual-rigid obstruction based on right scattering would need all of the
following:

```text
1. orbit-relevant active p != q with E(p,q) nonempty;
2. harmful scattering producing same-orbit bad pairs;
3. no fixed finite contextual quotient separating those pairs in all arities;
4. no finite contextual rack detector absorbing the collapse;
5. no proper domination-reducing active factor.
```

The constant-action example has only item 1.  It fails item 2 because the rack
detector absorbs the scattering.

An actual scattering table pattern is:

```text
r(a,y)=(a,z),  z != y.
```

Then the left structure monoid relation gives

```text
lambda_a lambda_y = lambda_a lambda_z.
```

Nondegeneracy does not forbid this pattern in general.  It only forbids the
earlier special two-step fixed-right-output pattern.

## Bounded Bad Witnesses Still Need A New Lemma

The bounded bad-witness theorem remains sufficient:

```text
There exists N=N(X) such that every contextual bad pair has a bad
subconfiguration of arity <= N.
```

If true, one takes the product of finitely many contextual rack detectors for
same-orbit pairs in arities at most `N`, obtaining one detector for all
arities.

But deletion and braid locality do not prove boundedness.  Contextual labels
depend on the full left and right observer states

```text
a_i=theta(lambda_{x_1}...lambda_{x_{i-1}}),
b_i=theta(lambda_{x_{i+1}}...lambda_{x_n}).
```

Deleting an observer can remove the equalizing state.  A long observer word can
be essential to a collapse.  Braid generators act locally on letters but not
on the context states that determine the labels.

Stronger assumptions help only partially:

```text
finite right-separation removes one source of unboundedness;
cancellativity removes actual equalizers but not profinite ones;
group embeddability removes right scattering for pairs separated in the group;
finite Green/Rees data describes finite quotients but gives no uniform bound;
automaticity gives word machinery but not finite contextual behavior;
residual-rigid minimality excludes finite active factors but not profinite
  infinite-index collapses.
```

The useful package is:

```text
finite right-separation
+ finite-index contextual Myhill-Nerode behavior
+ uniform stabilizer separation.
```

None is currently forced by residual rigidity.

## Active-Factor Extraction Conditions

Let `S` be a finite contextual state quotient and suppose there are maps

```text
pi_{a,b}:X -> Z
```

to a finite set `Z`.  For `r_X(x,y)=(u,v)`, define the relation on `Z^2` by

```text
(A,B) R_pi (C,D)
```

if there exist contexts `a,b` and letters `x,y` such that

```text
A=pi_{a,lambda_y b}(x),
B=pi_{a lambda_x,b}(y),
C=pi_{a,lambda_v b}(u),
D=pi_{a lambda_u,b}(v).
```

This produces a finite bijective YBE solution `Z` only if:

```text
1. functionality: output depends only on (A,B);
2. totality: every pair (A,B) in Z^2 occurs as an input;
3. cofunctionality: each output has a unique input;
4. YBE holds on all of Z^3;
5. the induced maps Pi_n are braid-equivariant;
6. Pi_n is injective on every braid orbit.
```

Under these conditions,

```text
ker rho_n^Z <= ker rho_n^X
```

for every `n`: if `beta` is trivial on `Z^n`, equivariance and orbit
injectivity force it to be trivial on `X^n`.

Failure of contextual separation does not automatically force these
conditions.  A profinite collapse may be infinite-index, context-dependent,
nonfunctional, partial on reachable pairs, or non-bijective on `Z^2`.

The missing finite extraction lemma is:

```text
Every harmful profinite contextual collapse has a finite-index quotient
satisfying the active-factor conditions above.
```

## Uniform Stabilizer Separation

Fix a finite state quotient `M` and put

```text
R=C_M(X),
G=As(R).
```

If `r'=g.r` and `H=Stab_G(r)`, finite rack quotients separate `r` from `r'`
only when finite quotients of `G` separate `gH` from `H`.

Pointwise stabilizer separability says `g` is outside the profinite closure of
`H`.  Uniform separation of a family `T subset G\H` requires

```text
closure(T) cap closure(H) = empty
```

inside the profinite completion.

The factorial accumulation model shows the gap:

```text
G=Z,
H={0},
T={n! : n>=1}.
```

Every individual `n!` is separated from `0` by some finite quotient, but no
single finite quotient separates all of `T` from `0`.

The same mechanism can occur in any associated rack group with an element `h`
whose powers act on an orbit-relevant rack label.  The family `h^{n!}` tends to
the identity in every finite quotient.  To rule this out one needs a
YBE-specific uniform transporter theorem or finite orbit control.

## Escape Holonomy

Escape holonomy records transporter or stabilizer-coset data, not merely
finite two-sided context states.  Algebraically, the extra datum has the form

```text
g Stab(r) subset As(C_M(X))
```

or the analogous coset in an escape action groupoid.

Escape holonomy can separate individual witnesses, but to become a finite rack
detector it must satisfy:

```text
finite image of the holonomy cocycle modulo stabilizers;
crossing compatibility of the compressed holonomy data;
uniform stabilizer-coset separation;
a finite rack quotient encoding the labels.
```

If a holonomy loop has infinite order on an orbit-relevant label, the sequence
of factorial powers gives the same uniformity obstruction.  Escape holonomy is
therefore diagnostic but not automatically finite-state.

## Strongest Current Theorems

The contextual detector theorem is valid:

```text
If there exist finite theta:L_X->M and finite phi:C_M(X)->Y such that
phi^n Theta_n^M is injective on every braid orbit in every arity, then
ker rho_n^Y <= ker rho_n^X for all n.
```

Bounded witnesses imply Sawin by the finite product argument.

Finite right-separation plus bounded witnesses plus uniform stabilizer
separation imply Sawin, provided the resulting finite contextual rack label
separations are realized by finite rack quotients.

Tower failure implies a finite active factor only under finite extraction:
the harmful collapse must be finite-index, crossing-compatible, total,
bijective, and orbit-injective.

## Current Missing Lemma

The right target is not:

```text
no right scattering.
```

The right target is:

```text
harmful profinite contextual collapse
=> finite rack absorption or proper finite active factor.
```

Equivalently:

```text
Residual-rigid X
=> finite-index, crossing-compatible, uniformly stabilizer-separable
   harmful behavior.
```

This is strictly smaller than Sawin and is the current exact gap in the
contextual tower route.
