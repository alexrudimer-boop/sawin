# Minimal-Ideal Escape Rack Construction

Date: 2026-06-05

This note records a conditional rackification obtained from the combined
left/right minimal-ideal transport groupoids.  It does not prove Sawin
domination by itself.  It produces a finite rack and an all-arity equivariant
rack label map, and isolates the exact missing point as orbit-injectivity of
that label map.

## Coordinate identities

Write

```text
r(x,y)=(L_x(y),R_y(x)).
```

For a local crossing, put

```text
u=L_x(y),  v=R_y(x).
```

The left and right product identities are

```text
L_u L_v = L_x L_y,
R_v R_u = R_y R_x.
```

These identities give product-preserving refactorizations of transport arrows.
The middle YBE identity is the remaining three-strand coherence input.

## Combined transport groupoid

Let

```text
S_L=<L_x:x in X>,   S_R=<R_y:y in X>
```

be the nonempty-product left and right transformation semigroups.  Let
`G_L` and `G_R` be the minimal-ideal transport groupoids built from their
minimal-rank images.  The combined two-sided groupoid is

```text
C = G_L x G_R^op.
```

For minimal images `A in Ob(G_L)` and `B in Ob(G_R)`, define the elementary
strand transport

```text
eta(x;A,B) = (L_x|_A, (R_x|_B)^op).
```

As an arrow of `C`,

```text
eta(x;A,B): (A,R_x B) -> (L_x A,B).
```

For the local crossing above and external minimal images `A,B`, define old and
new arrows

```text
a  = eta(x;L_y A,B),
b  = eta(y;A,R_x B),
a' = eta(u;L_v A,B),
b' = eta(v;A,R_u B).
```

The product identities imply that the old and new composites have the same
source and target and satisfy

```text
a' b' = a b
```

with the chosen composition convention.  A rack crossing needs more than this:
it needs the new second strand to become the old first strand, and the new
first strand to become the rack action of the old first strand on the old
second.  That mismatch is the cross-coordinate escape.

## Groupoid action rack

Choose a base object `o in Ob(C)` and connectors

```text
tau_P:o -> P
```

for all objects `P`.  Put

```text
H = Aut_C(o).
```

Every arrow `alpha:P -> Q` has normalized label

```text
nu(alpha)=tau_Q^{-1} alpha tau_P in H.
```

Equivalently, an arrow can be represented as `(Q,g,P)`, meaning source `P`,
target `Q`, and normalized label `g in H`.

Define a rack operation on the finite set

```text
Y_0 = Arr(C)
```

by

```text
(Q,g,P) * (Q',h,P') = (Q', g h g^{-1}, P').
```

The left translations are bijective and the rack identity is conjugation in
`H`.  The connector choice is a gauge; changing it gives an isomorphic
coordinatization.

## Forced escape quotient

Let `~_esc` be the least rack congruence on `Y_0` containing, for every
elementary local crossing and every external boundary pair, the relations

```text
b' ~ a,
a' ~ a*b.
```

The quotient

```text
Y_esc = Y_0 / ~_esc
```

is a finite rack.  It is the maximal quotient of this groupoid action rack in
which every elementary transport refactorization becomes a rack crossing.  Let
`q:Y_0 -> Y_esc` be the quotient map.  Then every local crossing satisfies

```text
q(a') = q(a) * q(b),
q(b') = q(a).
```

## All-arity rack labels

Fix boundary objects

```text
A in O_L,  B in O_R.
```

For a word `w=(x_1,...,x_n)`, propagate left cuts from right to left and right
cuts from left to right:

```text
A_n=A,          A_{i-1}=L_{x_i}(A_i),
B_0=B,          B_i=R_{x_i}(B_{i-1}).
```

The `i`-th strand transport is

```text
eta_i^{A,B}(w)=eta(x_i;A_i,B_{i-1}).
```

Take all boundary pairs at once.  Let

```text
Omega = O_L x O_R,
Y = Y_esc^Omega
```

with componentwise rack operation, and define

```text
Psi_n(w)_i =
    ( q(eta_i^{A,B}(w)) )_{(A,B) in Omega}
    in Y.
```

The local quotient relations imply

```text
Psi_n(sigma_i w) = sigma_i Psi_n(w)
```

for each braid generator.  Thus

```text
Psi_n:X^n -> Y^n
```

is `B_n`-equivariant for every `n`.

## Exact missing lemma

The remaining point is not equivariance.  It is separation inside braid
orbits.

Minimal-ideal strand-separation lemma:

```text
If w' is in the B_n-orbit of w and Psi_n(w')=Psi_n(w), then w'=w.
```

If this holds for a finite solution `X`, then define the inert orbit observer

```text
I_n = X^n / B_n
```

and

```text
Phi_n(w) = (Psi_n(w), [w]) in Y^n x I_n.
```

The map `Phi_n` is `B_n`-equivariant and injective.  Therefore if
`beta in ker rho^Y_n`, then `beta` acts trivially on `Y^n` and on `I_n`, so

```text
Phi_n(beta w)=Phi_n(w)
```

for all `w`.  Injectivity gives `beta w=w` for all `w`, hence

```text
ker rho^Y_n <= ker rho^X_n
```

for every `n`.  Thus `Y` dominates `X`.

## Formal obstruction

The construction also gives the exact obstruction to this route.  If there are
some `n` and distinct words

```text
w != w' in X^n
```

with

```text
w' in B_n w,
Psi_n(w')=Psi_n(w),
```

then no inert observer can repair the collision, because any inert observer is
constant on braid orbits.  Such a collision blocks this particular
minimal-ideal escape-rack detector.

A rigid-core counterexample surviving this route must therefore defeat the
explicit maximal escape-rack detector by producing same-orbit collisions, and
for a genuine Sawin counterexample those failures would have to persist beyond
all finite-rack-prefix repairs in the sharpened asymptotic sense.

