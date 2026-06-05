# Proper Contextual Dichotomy Target

Date: 2026-06-05

This note records the boundary after the residual-endpoint extraction route
has been closed.  The remaining contextual routes are exactly:

```text
direct finite rack absorption
```

or

```text
an independently constructed proper active factor not factoring through E_M.
```

There is no formal extraction of an orbit-injective active factor from the
fixed-`M` residual endpoint systems.  Any such factor would have to use
information not visible to finite rack quotients of `C_M(X)`.

## Residual Endpoint Systems Cannot Give Active Factors

Fix a finite quotient

```text
theta:L_X -> M.
```

Let

```text
S_M=M x X x M
```

and write

```text
delta_{a,x,b}=d_{a,x,b} in C_M(X).
```

Define

```text
s equiv_M t
```

if every finite rack quotient

```text
phi:C_M(X) -> Y
```

identifies `delta_s` and `delta_t`.  Let

```text
E_M=S_M/equiv_M.
```

Since `S_M` is finite, one finite rack quotient

```text
Phi_M:C_M(X) -> Y_M
```

realizes this residual endpoint quotient on endpoint generators:

```text
Phi_M(delta_s)=Phi_M(delta_t)
iff
s equiv_M t.
```

Define

```text
Pi_n^{E_M}:X^n -> E_M^n
```

by

```text
Pi_n^{E_M}(x_1,...,x_n)_i =
[(a_i,x_i,b_i)]_{equiv_M},
```

where the contexts are computed in `M`:

```text
a_i=theta(lambda_{x_1}...lambda_{x_{i-1}}),
b_i=theta(lambda_{x_{i+1}}...lambda_{x_n}).
```

Assume no finite contextual rack detector separates every kernel-fiber bad
pair.  Then the strongest fixed-`M` detector

```text
D_M=(M,Phi_M)
```

also fails.  Therefore there exist

```text
n >= 1,
beta in K_n(P_X),
a in X^n
```

such that

```text
beta a != a
```

but

```text
Phi_M^n Theta_n^M(beta a)=Phi_M^n Theta_n^M(a).
```

By the defining property of `Phi_M`, this is equivalent to

```text
Pi_n^{E_M}(beta a)=Pi_n^{E_M}(a).
```

Thus every finite `M` has an actual bad pair collapsed by `E_M`.

Now let

```text
q:E_M -> Z
```

be any map and define

```text
pi_{a,b}(x)=q([(a,x,b)]_{equiv_M}).
```

Then

```text
Pi_n^Z=q^n Pi_n^{E_M}.
```

The same bad pair satisfies

```text
Pi_n^Z(beta a)=Pi_n^Z(a),
beta a != a,
beta a in B_n.a.
```

So `Pi_n^Z` is not globally orbit-injective.  No quotient of `E_M` can restore
orbit-injectivity.

Totality, cofunctionality, bijectivity, and YBE on unreached triples cannot
repair this, because the coordinate map has already identified a same-orbit
pair.

This proves the residual endpoint extraction principle is false.

## What Active-Factor Routes Remain

A successful active factor cannot factor through `E_M`.  Therefore, for some
finite `M`, a putative active factor

```text
pi_{a,b}:X -> Z
```

must separate endpoint symbols

```text
s=(a,x,b),  t=(a',x',b')
```

with

```text
s equiv_M t
```

but

```text
pi_s != pi_t.
```

Equivalently, it separates finite-rack-invisible endpoint pairs.  Thus it is
not induced by any finite rack quotient of `C_M(X)`.  It is a genuinely
non-rack active structure.

The possible sources of extra information are:

```text
path or holonomy data,
non-endpoint finite state,
inert observers,
a direct construction of pi_{a,b}:X -> Z,
or some finite structure not realized by rack endpoint quotients.
```

Under the harmful hypothesis, such data must fall into one of two useful
cases.

## Holonomy Case Split

One can try to enrich endpoint labels by finite reachable holonomy data, for
example labels of the form

```text
(a,x,b,h),
```

where `h` records a finite path or holonomy state.

This helps only if the holonomy is reachable and orbit-relevant: it must
separate actual pairs

```text
a, beta a
```

with

```text
beta in K_n(P_X),  beta a != a.
```

Ambient holonomy not realized by actual bad pairs is irrelevant.

There are three possibilities.

First, the holonomy labels form a finite rack detector.  If there is a finite
rack `Y` and labels satisfying the contextual rack crossing relations, then
the assignment extends to a finite rack quotient of an enriched contextual
rack.  If it separates every bad pair, this is direct finite rack absorption.

Second, the holonomy labels form a finite active YBE factor.  That requires a
finite set `Z`, a total bijective YBE map

```text
r_Z:Z^2 -> Z^2,
```

contextual crossing compatibility, and induced maps

```text
Pi_n:X^n -> Z^n
```

that are globally orbit-injective.  This can avoid the residual endpoint
obstruction only if it does not factor through `E_M`.

Third, the holonomy labels are neither rack-valued nor YBE-valued.  Then they
do not produce a braid action on a finite target and do not imply any kernel
inclusion.  They may be diagnostic, but they do not solve domination.

Thus hidden holonomy supplies orbit-injectivity only if it becomes either:

```text
a finite rack detector
```

or

```text
a finite non-rack active YBE factor with global orbit-injectivity.
```

There is no third kernel-reflecting mechanism.

## Avoiding E_M

For fixed `M`, a map

```text
pi:S_M -> Z
```

factors through `E_M` if and only if

```text
s equiv_M t  =>  pi(s)=pi(t).
```

It avoids `E_M` exactly when it separates some pair `s,t` with

```text
s equiv_M t.
```

Such a non-rack active factor must satisfy strong compatibility conditions.

First, contextual crossing compatibility:

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

Second, functionality: equal `Z^2` input labels from hidden contextual
representatives must have equal `Z^2` outputs.

Third, cofunctionality: the same condition must hold backward.

Fourth, totality: every pair in `Z^2` must have an assigned crossing value.

Fifth, YBE must hold on all of `Z^3`, including unreached triples.

Sixth, global orbit-injectivity:

```text
Pi_n(a)=Pi_n(b),  b in B_n.a  =>  a=b.
```

The no-detector hypothesis forces none of these.  It says finite rack
quotients fail; it says nothing positive about non-rack maps `pi:S_M -> Z`.
An active factor avoiding `E_M` is therefore an independent construction.

## Direct Clopen-Core Absorption

The residual endpoint obstruction also clarifies the rack-absorption side.
Finite-rack absorption cannot be obtained by residual endpoint totalization.
The viable rack route is direct finite detector construction.

Let `D` range over finite contextual rack detectors, and let `B_D` be the bad
pairs not separated by `D`.  If no finite detector separates every bad pair,
then the family `{B_D}` has the finite intersection property, so there is a
harmful ultrafilter `U` containing every `B_D`.

If a clopen core `C` is separated by a detector `D`, then

```text
Occ(C) cap B_D = empty.
```

Since `B_D in U`, one has

```text
Occ(C) notin U.
```

Therefore a harmful ultrafilter automatically avoids every clopen core already
separated by a finite detector.  A theorem saying every harmful ultrafilter
contains such a core is a genuinely new YBE-specific bounded-core theorem,
not a compactness consequence.

## Larger Finite Quotients Do Not Evade The Endpoint Obstruction

Could there be a larger finite quotient `M_0` whose residual endpoint system
`E_{M_0}` is orbit-injective?  Under the no-detector hypothesis, no.

For every finite `M`, the strongest detector `D_M=(M,Phi_M)` fails.  Thus for
every finite `M`, there is an actual bad pair

```text
a, beta a
```

with

```text
Pi_n^{E_M}(a)=Pi_n^{E_M}(beta a).
```

Define bad-pair-injectivity for `E_M` by

```text
Pi_n^{E_M}(a)=Pi_n^{E_M}(beta a), beta in K_n(P_X) => beta a=a.
```

Then

```text
E_M is bad-pair-injective
iff
D_M separates every kernel-fiber bad pair.
```

Global orbit-injectivity is stronger.  Hence if some `E_{M_0}` were globally
orbit-injective, a finite detector would already exist.  State refinement
through larger finite `M_0` cannot escape the obstruction while still
factoring through `E_{M_0}`.

## Necessary Active-Factor Conditions

Let finite data be given:

```text
M, Z, pi_{a,b}:X -> Z, r_Z:Z^2 -> Z^2.
```

Define

```text
Pi_n(x_1,...,x_n)_i=pi_{a_i,b_i}(x_i).
```

Sufficient active-factor conditions are:

```text
1. contextual compatibility for every r_X(x,y)=(u,v);
2. r_Z is total, bijective, and YBE on all of Z^3;
3. braid equivariance of Pi_n, which follows from 1 and 2;
4. global orbit-injectivity of Pi_n on braid orbits.
```

Then

```text
ker rho_n^Z <= ker rho_n^X
```

for every `n`.  The exact necessary and sufficient kernel-reflection condition
is weaker than global orbit-injectivity:

```text
for all beta in ker rho_n^Z and all a in X^n,
Pi_n(beta a)=Pi_n(a) => beta a=a.
```

But global orbit-injectivity is the clean structural condition.

None of these active-factor conditions is forced by the no-detector
hypothesis:

```text
functionality,
totality,
cofunctionality,
YBE on unreached triples,
orbit-injectivity,
properness.
```

## Proper Contextual Dichotomy Theorem

The strongest theorem, strictly smaller than Sawin and compatible with the
residual endpoint obstruction, is:

```text
For every finite bijective set-theoretic YBE solution X, at least one of the
following holds.

Branch I: finite rack absorption.
  There exists a finite contextual rack detector D=(M,phi:C_M(X)->Y)
  separating every kernel-fiber bad pair.

Branch II: independent proper active extraction.
  There exists a finite bijective YBE solution Z with |Z|<|X|, a finite
  quotient M of L_X, and maps pi_{a,b}:X -> Z such that the induced Pi_n are
  braid-equivariant and globally orbit-injective.

  Under the no-detector hypothesis, this Z cannot factor through any residual
  endpoint quotient E_M.
```

If this dichotomy were proved, Sawin would follow by induction on `|X|`.
The base case is trivial.  In Branch I, the detector gives a finite rack
directly.  In Branch II, descend to the strictly smaller finite YBE solution
`Z`; by induction, a finite rack `Y` dominates `Z`, and hence dominates `X`
by the kernel inclusions

```text
ker rho_n^Y <= ker rho_n^Z <= ker rho_n^X.
```

This theorem is now the sharp contextual target.  It is not a formal
consequence of the current hypotheses.  The second branch must be proved by a
genuinely new construction, not by quotienting or totalizing `E_M`.

## Final Boundary

The exact remaining route is:

```text
prove direct finite rack absorption,
```

or

```text
construct an independent proper active factor with verified orbit-injectivity.
```

Without one of these two new inputs, the contextual detector route does not
close Sawin's problem.
