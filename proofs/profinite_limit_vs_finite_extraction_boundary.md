# Profinite Limit Versus Finite Extraction Boundary

Date: 2026-06-05

This note records what the harmful bad-pair ultrafilter actually gives.  It
does produce canonical limiting objects, but they are hyperfinite and profinite,
not standard finite.  The missing step is still finite-index extraction.

The sharp conclusion is:

```text
compactness gives a profinite or hyperfinite collapse,
not a finite-index quotient.
```

To finish the contextual tower route, one needs a YBE-specific theorem ruling
out or finite-factorizing the resulting infinite-index holonomy patterns.

## Hyperfinite Bad Pair

Let finite contextual rack detectors be

```text
D=(M,phi),
Lambda_n^D=phi^n Theta_n^M:X^n -> Y^n.
```

Let

```text
Omega=disjoint_union_n Omega_n,
Omega_n={(x,x') : x != x', x' in B_n.x}.
```

The bad set of `D` is

```text
B_D={(x,x') in Omega : Lambda_n^D(x)=Lambda_n^D(x')}.
```

Uniform failure of all finite detectors gives an ultrafilter `U` on `Omega`
with

```text
B_D in U
```

for every finite detector `D`.  If fixed bad pairs are pointwise separated,
then `U` is nonprincipal and unbounded in arity.

Taking the ultrapower over `U` gives a hyperinteger

```text
N=[n_omega]_U in *N
```

which is infinite, and internal words

```text
x*=[x^omega]_U,
x'*=[x'^omega]_U
```

of length `N` over `X`.  They satisfy

```text
x* != x'*,
x'* in B_N.x*.
```

Choosing braids `beta_omega` with

```text
x'^omega = rho_{n_omega}^X(beta_omega)x^omega
```

gives an internal braid `beta*` on `N` strands with

```text
x'*=rho_N^X(beta*)x*.
```

For every standard finite detector `D`,

```text
Lambda_N^{D,*}(x*) = Lambda_N^{D,*}(x'*),
```

because `B_D in U`.

Thus harmfulness canonically gives:

```text
a nonstandard same-orbit pair of infinite arity invisible to every standard
finite detector.
```

This is a genuine limiting object, but it is not finite.

## Profinite Contextual Collapse

Let

```text
K=hat{L_X} x X x hat{L_X}.
```

For `x=(x_1,...,x_n)`, define the contextual letter

```text
kappa_i(x)=(
  lambda_{x_1}...lambda_{x_{i-1}},
  x_i,
  lambda_{x_{i+1}}...lambda_{x_n}
) in K.
```

The ultrafilter gives a canonical closed relation

```text
R_U subset K x K
```

by

```text
R_U =
intersection_{A in U}
closure({
  (kappa_i(x^omega), kappa_i(x'^omega)) :
  omega in A, 1 <= i <= n_omega
}).
```

Compactness of `K x K` makes `R_U` nonempty and closed.

For a detector `D=(M,phi)`, define the continuous label map

```text
ell_D:K -> Y
```

by

```text
ell_D(ahat,x,bhat)
=
phi(d_{theta(ahat),x,theta(bhat)}).
```

Since `B_D in U`, every pair in `R_U` is identified by `D`:

```text
(xi,eta) in R_U  =>  ell_D(xi)=ell_D(eta).
```

Thus

```text
R_U subset intersection_D ker(ell_D x ell_D).
```

Equivalently, `R_U` lies inside the universal detector-equivalence relation
on `K`.

The quotient

```text
K / equiv_det
```

embeds as a closed subspace of the product of all finite detector label sets.
It is a compact profinite label space, not generally a finite one.

## Partial Pro-YBE Structure

There is a natural partial contextual crossing on `K`.  If

```text
r_X(x,y)=(u,v),
```

then an admissible adjacent pair has the form

```text
(a,x,lambda_y b),
(a lambda_x,y,b).
```

The contextual crossing sends it to

```text
(a,u,lambda_v b),
(a lambda_u,v,b).
```

This defines a partial map

```text
r_K:A subset K^2 -> K^2.
```

The detector-equivalence relation is compatible with this partial crossing on
admissible pairs, because every finite detector is braid-equivariant.

Hence `K/equiv_det` has a well-defined partial pro-YBE operation on reachable
contextual pairs.

This still does not define a finite active factor.  The operation is partial,
may have infinitely many states, need not be bijective on all pairs, and need
not satisfy YBE on unreached triples of any finite quotient.

The canonical limiting object is therefore:

```text
hyperfinite bad pair
+ profinite contextual quotient
+ partial pro-YBE operation
+ possibly profinite holonomy.
```

## Compactness Does Not Give Finite Index

Ultraproducts and compactness produce internally finite or profinite objects.
They do not produce a standard finite quotient.

The obstruction is:

```text
internally finite / profinite / pseudofinite
is not the same as
standard finite.
```

Los transfers first-order properties, but it does not supply a standard finite
bound on the number of contextual states.

A contextual equivalence on `K` factors through one finite quotient

```text
theta:L_X -> M
```

only when it is finite-index and clopen in a way controlled by `theta`.  A
closed profinite relation is not enough.

The model remains:

```text
B_N={m in N : m>N}.
```

The intersection is empty, but no single `B_N` is empty.  In the contextual
tower, `m` is observer length or holonomy depth.

Thus the finite-index step requires a new theorem.

## Finite Active Extraction Conditions

Given finite `M`, finite `Z`, and maps

```text
pi_{a,b}:X -> Z,
```

define `Gamma subset Z^2 x Z^2` by

```text
(A,B) Gamma (C,D)
```

if for some `a,b,x,y` with `r_X(x,y)=(u,v)`,

```text
A=pi_{a,lambda_y b}(x),
B=pi_{a lambda_x,b}(y),
C=pi_{a,lambda_v b}(u),
D=pi_{a lambda_u,b}(v).
```

This gives a finite bijective YBE solution only if:

```text
functionality: equal Z-inputs give equal outputs;
totality: every pair in Z^2 occurs as input;
cofunctionality/bijectivity: every output has a unique input;
YBE: the induced bijection satisfies YBE on all of Z^3;
equivariance: the maps Pi_n are braid-equivariant;
kernel reflection: ker rho_n^Z <= ker rho_n^X for all n.
```

A sufficient kernel-reflection condition is orbit-injectivity of `Pi_n` on
every braid orbit.

Harmful non-absorption does not force any of these conditions.  Extraction can
fail through:

```text
infinite-index behavior;
nonfunctional crossing;
partiality;
nonbijectivity;
YBE failure on unreached triples;
loss of orbit-injectivity.
```

## Shift Rack Factorial Obstruction

There is a clean obstruction at the level of racks and associated rack groups.

Let

```text
R=Z
```

with rack operation

```text
i triangleright j = i+1.
```

The shift `h:i -> i+1` generates an action group `Z`, and the stabilizer of
`0` is trivial.

Consider the transporter family

```text
T={h^{n!}:n>=1}.
```

Equivalently, consider pairs `(0,n!)`.  Every fixed pair `(0,n!)` is separated
by some finite rack quotient, for example reduction modulo `m` with
`m` not dividing `n!`.

But no single finite rack quotient separates all pairs `(0,n!)`.  In any
finite quotient, the shift has finite order `m`, and for all sufficiently large
`n`, `n!` is divisible by `m`, so `0` and `n!` coincide.

Thus the family is pointwise separable but not uniformly separable.  In
associated-group language,

```text
h^{n!} -> 1
```

in every finite quotient of the cyclic group generated by `h`, while
`h^{n!}` is never in the original stabilizer.

This is a counterexample to finite extraction in the ambient category of racks
and associated rack groups.  It is not yet a contextual rack `C_M(X)` coming
from a finite YBE solution.

Therefore any Sawin proof through contextual racks needs a YBE-specific reason
to prevent this pattern from being orbit-relevant in `C_M(X)`, or to show that
when it occurs it descends to a proper finite active factor.

## Residual Rigidity Does Not Remove The Limit By Itself

Residual rigidity removes finite active factors satisfying the correct kernel
direction:

```text
ker rho_n^Z <= ker rho_n^X.
```

It does not automatically remove:

```text
infinite-index contextual behavior;
profinite right scattering;
nonfunctional crossing;
partial crossing;
nonbijective induced crossing;
YBE failure on unreached triples;
loss of orbit-injectivity.
```

Only after a valid finite active factor has been extracted can residual
rigidity exclude it.

## Escape Holonomy Ultralimits

Escape holonomy records transporter data in an action groupoid.  A harmful
ultrafilter can determine a profinite holonomy limit:

```text
g_omega H_omega -> ghat Hhat
```

in finite quotients of the associated group or groupoid.

Uniform failure of finite rack separation is exactly the phenomenon that the
profinite transporter lies in the closure of the stabilizer:

```text
ghat in closure(H)
```

or, for families,

```text
closure(T) cap closure(H) != empty.
```

Escape holonomy therefore diagnoses the obstruction.  It compresses to finite
rack labels only when there is a finite quotient separating all relevant
holonomy cosets.  Factorial accumulation prevents such compression.

## Strongest Current Theorems

The valid endpoint remains conditional.

```text
Finite contextual detector with empty bad set => Sawin domination for X.
```

Bounded harmful witnesses imply a finite detector by a finite product over
bounded arities.

Finite-index contextual behavior plus uniform stabilizer separation implies a
finite detector.

Finite active extraction implies residual-rigid Sawin:

```text
Every harmful bad-pair ultrafilter produces a finite active factor Z with
ker rho_n^Z <= ker rho_n^X.
```

The sharp missing lemma is:

```text
Every harmful profinite contextual/holonomy collapse is finite-index and
active-factor extractable, or finite-rack absorbed.
```

Equivalently, one must rule out realization of the shift-rack/factorial
holonomy pattern inside orbit-relevant YBE contextual racks, or prove that such
realization gives a proper finite active factor with the correct kernel
direction.
