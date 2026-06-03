# Rack point-pushing operator-label invariant

Date: 2026-06-03

This note replaces the false point-pushing heuristic "finite racks have
bounded point-pushing image exponent" with the usable rack-only structure.
Finite rack point-pushing images may have unbounded exponent as braid index
grows.  The invariant is instead an operator-label Hurwitz quotient with a
uniformly bounded-exponent vertical kernel.

## Rack Operator Labels

Let `Y` be a finite rack in the convention

```text
R(a,b)=(a*b,a).
```

For each `y in Y`, write

```text
L_y(z)=y*z
```

and put

```text
H=Inn(Y)=<L_y:y in Y>,      C={L_y:y in Y} subset H.
```

The rack identity gives

```text
L_{y*z}=L_y L_z L_y^{-1}.
```

Thus `lambda:Y->C`, `lambda(y)=L_y`, is a morphism from `Y` to the
conjugation rack of `H`.  Hence, for every `m`, the map

```text
lambda_m:Y^m -> C^m
```

is `B_m`-equivariant, where `B_m` acts on `C^m` by group Hurwitz moves.

## Point-Pushing Exact Sequence

Let

```text
K_n = ker(P_{n+1}->P_n)
```

be the Fadell-Neuwirth last-strand point-pushing kernel.  Use the standard
generators

```text
alpha_{i,n+1}
 =
sigma_n sigma_{n-1} ... sigma_{i+1} sigma_i^2
sigma_{i+1}^{-1} ... sigma_{n-1}^{-1} sigma_n^{-1}
```

for `1<=i<=n`.  In the code these are `pure_braid_generator(i,n+1)`.

Define

```text
Q_Y(n)=rho_{Y,n+1}(K_n).
```

Equivariance of `lambda_{n+1}` gives a marked quotient

```text
Q_Y(n) -> Q_{H,C}(n),
```

where `Q_{H,C}(n)` is the point-pushing image on `C^{n+1}` under the finite
group-Hurwitz action.  Let `V_Y(n)` be the kernel.  Then

```text
1 -> V_Y(n) -> Q_Y(n) -> Q_{H,C}(n) -> 1.
```

The important bound is

```text
exp V_Y(n) divides exp H
```

uniformly in `n`.

## Vertical Kernel Bound

For a pure braid `beta in P_m`, the Artin action on the free group has

```text
x_j |-> u_{beta,j} x_j u_{beta,j}^{-1}.
```

For a rack tuple `y=(y_1,...,y_m)`, this gives

```text
(rho_{Y,m}(beta)y)_j
 =
u_{beta,j}(L_{y_1},...,L_{y_m}) . y_j.
```

Once the operator-label tuple `(L_{y_1},...,L_{y_m})` is fixed, each
coordinate is acted on by an element of `H`.  Therefore the vertical kernel
embeds in a product of copies of `H^m`, indexed by operator-label fibres:

```text
V_Y(n) <= product_eta H^{n+1}.
```

Consequently every vertical-kernel element has order dividing `exp H`.

## What This Does Not Say

It does not say

```text
exp Q_Y(n) <= C(Y).
```

That statement is false.  For the three-element dihedral rack used in the
repo tests,

```text
Y=F_3,        a*b=2a-b,
```

the inner group has exponent `6`, but the checked arity-`3` point-pushing
image has exponent `36`.  The unbounded part belongs to the finite
group-Hurwitz quotient `Q_{H,C}(n)`, not to the vertical kernel.

The generated audit

```text
proofs/rack_point_pushing_operator_label_audit.md
```

records this finite warning and checks that the vertical-kernel exponent
still divides `exp Inn(Y)` in the tested rows.

## Consequence For Rack Domination

If a finite rack `Y` dominates a finite bijective YBE solution `X`, then for
every `n`,

```text
ker rho_{Y,n+1}|_{K_n} subset ker rho_{X,n+1}|_{K_n}.
```

Equivalently, `Q_X(n)` is a marked quotient of `Q_Y(n)`.  Thus `Q_X(n)` must
admit normal subgroups `V_X(n)` compatible in the point-pushing tower such
that

```text
exp V_X(n) divides exp Inn(Y)
```

and

```text
Q_X(n)/V_X(n)
```

is a marked quotient of the fixed finite group-Hurwitz tower
`Q_{Inn(Y),C}(n)`.

The rack-only point-pushing invariant is therefore:

```text
Q_X(n) is uniformly a bounded-exponent vertical extension
of a fixed finite group-Hurwitz point-pushing tower.
```

## Missing Lemma: Finite Augmented Artin Envelope

The positive point-pushing route is now precise.

For every finite bijective set-theoretic YBE solution `X`, prove that there
exist

```text
H_X finite group,        C_X subset H_X conjugation-stable,        e_X<infty
```

and, for every `n`, normal subgroups

```text
V_X(n) normal in Q_X(n)
```

compatible with the point-pushing tower, such that

```text
exp V_X(n) divides e_X
```

and

```text
Q_X(n)/V_X(n)
```

is a marked quotient of the group-Hurwitz point-pushing image
`Q_{H_X,C_X}(n)` for every `n`.

Equivalently, every finite bijective YBE point-pushing tower has a finite
operator-label model, up to uniformly bounded-exponent vertical noise.

If this lemma is true, point-pushing alone gives no obstruction to finite
rack domination: finite bijective YBE towers satisfy the same structural
point-pushing invariant as finite racks.

To turn that into actual finite rack domination, one still needs a realization
lemma:

```text
Every compatible finite augmented Artin-envelope tower is a marked quotient
of an actual finite rack tower.
```

## Obstruction Criterion

To disprove the missing lemma for a candidate degenerate solution `X`, the
first meaningful computations are at `n=3` and `n=4`:

```text
Q_X(3)=<rho_X(alpha_{1,4}),rho_X(alpha_{2,4}),rho_X(alpha_{3,4})>
```

and

```text
Q_X(4)=<rho_X(alpha_{1,5}),...,rho_X(alpha_{4,5})>.
```

One must then show that for every finite `(H,C)` and every `e`, the sequence
`Q_X(n)` fails to admit compatible normal subgroups `V_X(n)` with

```text
exp V_X(n) divides e
```

and

```text
Q_X(n)/V_X(n)
```

a marked quotient of `Q_{H,C}(n)`.  That is the real point-pushing
obstruction: unbounded complexity not explainable by one fixed finite
group-Hurwitz base plus bounded-exponent vertical kernel.
