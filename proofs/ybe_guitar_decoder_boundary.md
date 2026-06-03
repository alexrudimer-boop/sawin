# YBE guitar decoder boundary

Date: 2026-06-03

This note records the exact interface between the guitar-map theorem and the
finite-state rack-cover criterion.

Write the YBE solution as

```text
r(x,y) = (lambda_x(y), rho_y(x)).
```

For the right-guitar convention, set

```text
R_y(x)=rho_y(x).
```

## One-Sided Nondegenerate Closure

Assume every `R_y` is bijective and `r` is bijective.  Define

```text
J_n:X^n -> X^n
```

by

```text
J_n(x_1,...,x_n) =
(R_{x_n}...R_{x_2}(x_1),
 R_{x_n}...R_{x_3}(x_2),
 ...,
 R_{x_n}(x_{n-1}),
 x_n).
```

This map is triangular from right to left.  Since the maps `R_y` are
bijective, every `J_n` is bijective.

Define the derived operation

```text
a < b = R_a(lambda_{R_b^-1(a)}(b)).
```

Equivalently, if `x=R_b^-1(a)`, so `a=rho_b(x)`, then

```text
a < b = rho_{rho_b(x)}(lambda_x(b)).
```

The guitar-map theorem says that this is a rack operation and that the rack
crossing

```text
S(a,b)=(a < b,a)
```

is conjugate to the original YBE crossing in every arity:

```text
J_n rho_X,n(beta) = rho_Y,n(beta) J_n
```

for every braid `beta in B_n`, where `Y=(X,<)`.

Therefore

```text
ker rho_Y,n = ker rho_X,n
```

for every `n`.  In Sawin's MathOverflow formulation, this is stronger than
domination: the finite rack `Y` has exactly the same braid-action kernels as
`X` in every arity.

This is the right-sided version of the already recorded
left-nondegenerate/guitar branch.  With the opposite rack convention, one uses
invertibility of the `lambda_x` instead.

## Decoder Interpretation

The inverse guitar map is a finite-state decoder.  Let

```text
G_rho=<R_x:x in X> <= Sym(X).
```

Set

```text
Q=G_rho.
```

Reading from right to left, define

```text
d(q,a)=q^-1(a),
tau(q,a)=q R_{q^-1(a)}.
```

Starting from the identity state, these formulas recover `J_n^-1`.  They
satisfy the finite-state decoder equations from
`proofs/ybe_finite_state_rack_cover_criterion.md`.  Thus the finite-state
decoder criterion is not merely a negative abstraction: in the one-sided
nondegenerate case it is exactly the guitar map.

## Degenerate Failure

If some `R_y` is not bijective, the first failure is already visible at
arity `2`:

```text
J_2(x,y)=(R_y(x),y).
```

For fixed `y`, this is bijective in `x` exactly when `R_y` is bijective.
Thus noninvertibility of a right action makes `J_2` nonbijective.

The derived rack formula fails at the same place:

```text
a < b = R_a(lambda_{R_b^-1(a)}(b)).
```

If `R_b` is not surjective, `R_b^-1(a)` may be empty.  If `R_b` is not
injective, it may contain several preimages and the derived operation can
become multivalued unless all choices give the same output.

## Monoid Gate

There is no automatic unbounded-memory obstruction at the level of suffix
transformations.  The transformation monoid

```text
M_rho=<R_x:x in X> <= End(X)
```

is finite.  The problem is that elements of `M_rho` do not have canonical
inverses.  A monoid replacement would need finite deterministic branch data

```text
Q=M_rho,
d(q,a) in q^-1(a),
tau(q,a)=q R_{d(q,a)},
```

defined whenever the decoded state is reachable, satisfying the same
finite-state decoder equations and making the resulting operation a rack.

So the degenerate obstruction is sharper than "needs infinite memory."  The
finite memory state space is available, but coherent deterministic inverse
branches may not exist.  Nondeterministic or relation-valued branches are not
enough for Sawin's kernel-inclusion formulation unless they can be
determinized by finite labels satisfying rack self-distributivity and the
decoder equations.

The generated audit

```text
proofs/ybe_guitar_decoder_boundary_audit.md
```

records this boundary.
