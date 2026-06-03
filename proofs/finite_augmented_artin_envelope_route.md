# Finite augmented Artin-envelope route

Date: 2026-06-03

This note records route (1) for the MathOverflow problem after the
point-pushing correction.  It replaces the false finite-rack heuristic

```text
exp Q_Y(n) <= C(Y)
```

with the actual rack invariant:

```text
Q_Y(n) is a bounded-exponent vertical extension of
a fixed finite group-Hurwitz point-pushing tower.
```

The route is positive if every finite bijective set-theoretic YBE solution has
the same point-pushing structure and if every compatible such structure is
realized by a finite rack tower.

## Rack side

For a finite rack `Y` in the convention `R(a,b)=(a*b,a)`, let

```text
L_y(z)=y*z,        H=Inn(Y)=<L_y>,        C={L_y:y in Y}.
```

The rack identity gives

```text
L_{y*z}=L_y L_z L_y^{-1}.
```

Thus `y |-> L_y` is a morphism from `Y` to the conjugation rack of the finite
group `H`.  Therefore, for each braid index `m`, the map

```text
Y^m -> C^m,        (y_1,...,y_m) |-> (L_{y_1},...,L_{y_m})
```

is equivariant for the group-Hurwitz action on `C^m`.

Let

```text
K_n = ker(P_{n+1}->P_n)
```

be the last-strand Fadell-Neuwirth point-pushing kernel, and set

```text
Q_Y(n)=rho_{Y,n+1}(K_n).
```

Then the rack operator-label map gives an exact sequence

```text
1 -> V_Y(n) -> Q_Y(n) -> Q_{H,C}(n) -> 1,
```

where `Q_{H,C}(n)` is the point-pushing image on `C^{n+1}` under finite
group-Hurwitz moves.  The vertical kernel consists of point-pushing
permutations acting trivially on all operator-label tuples.

For a pure braid `beta in P_m`, the Artin action on the free group has

```text
x_j |-> u_{beta,j} x_j u_{beta,j}^{-1}.
```

For a rack tuple `y=(y_1,...,y_m)`,

```text
(rho_{Y,m}(beta)y)_j =
u_{beta,j}(L_{y_1},...,L_{y_m}) . y_j.
```

Once the operator-label tuple is fixed, every coordinate action is by an
element of `H`.  Hence

```text
V_Y(n) <= product_eta H^{n+1},
```

with `eta` ranging over operator-label fibres, and so

```text
exp V_Y(n) divides exp H
```

uniformly in `n`.

This does not bound the exponent of `Q_Y(n)` itself.  The checked three-point
dihedral rack row already has `exp Inn(Y)=6` and point-pushing image exponent
`36` at arity `3`; the unbounded part belongs to the finite group-Hurwitz
quotient, not to the vertical kernel.

## Domination consequence

If a finite rack `Y` dominates a finite bijective YBE solution `X`, then

```text
ker rho_{Y,n+1}|_{K_n} subset ker rho_{X,n+1}|_{K_n}
```

for all `n`.  Equivalently, each `Q_X(n)` is a marked quotient of `Q_Y(n)`.
Therefore `Q_X(n)` must admit compatible normal subgroups `V_X(n)` such that

```text
exp V_X(n) divides exp Inn(Y)
```

and

```text
Q_X(n)/V_X(n)
```

is a marked quotient of the fixed group-Hurwitz point-pushing tower
`Q_{Inn(Y),C}(n)`.

Thus the rack-dominated point-pushing invariant is:

```text
Q_X(n) is uniformly a bounded-exponent vertical extension
of a fixed finite group-Hurwitz tower.
```

## Missing lemma 1: finite augmented Artin envelope

For every finite bijective set-theoretic YBE solution `X`, prove that there
exist

```text
H_X finite group,        C_X subset H_X conjugation-stable,        e_X < infinity
```

and compatible normal subgroups

```text
V_X(n) normal in Q_X(n)
```

such that

```text
exp V_X(n) divides e_X
```

and

```text
Q_X(n)/V_X(n)
```

is a marked quotient of `Q_{H_X,C_X}(n)` for every `n`.

Equivalently, every finite bijective YBE point-pushing tower has a finite
operator-label model up to uniformly bounded-exponent vertical noise.

If this lemma is true, point-pushing alone gives no obstruction to finite rack
domination, because arbitrary finite bijective YBE towers have the same
structural point-pushing invariant as finite rack towers.

## Missing lemma 2: finite rack realization

The point-pushing lemma does not by itself construct a dominating finite rack.
The next realization lemma would be:

```text
Every compatible finite augmented Artin-envelope tower is a marked quotient
of an actual finite rack tower.
```

Only the combination of the augmented-envelope lemma and this realization
lemma would close the point-pushing route to a full positive answer.

## Obstruction criterion

To refute the augmented-envelope lemma for a candidate finite degenerate
solution `X`, the first meaningful computations are

```text
Q_X(3)=<rho_X(alpha_{1,4}),rho_X(alpha_{2,4}),rho_X(alpha_{3,4})>
```

and

```text
Q_X(4)=<rho_X(alpha_{1,5}),...,rho_X(alpha_{4,5})>.
```

The standard generators are

```text
alpha_{i,n+1}
 =
sigma_n sigma_{n-1} ... sigma_{i+1} sigma_i^2
sigma_{i+1}^{-1} ... sigma_{n-1}^{-1} sigma_n^{-1}.
```

The generated route audit records these words explicitly in the code
convention:

```text
proofs/finite_augmented_artin_envelope_route_audit.md
```

A genuine obstruction must prove that, for every finite pair `(H,C)` and
every exponent bound `e`, the point-pushing groups `Q_X(n)` fail to admit
compatible `V_X(n)` with

```text
exp V_X(n) divides e
```

and

```text
Q_X(n)/V_X(n)
```

a marked quotient of `Q_{H,C}(n)`.

So the route is no longer "find unbounded order."  Finite racks already allow
that.  The pressure test is:

```text
unbounded point-pushing complexity not explainable by
one fixed finite group-Hurwitz base plus bounded-exponent vertical kernel.
```
