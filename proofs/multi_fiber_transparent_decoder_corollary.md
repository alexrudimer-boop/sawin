# Multi-Fibre Transparent Decoder Corollary

Date: 2026-06-08

This note records the multi-fibre transparent decoder as a corollary of
`proofs/finite_state_dominated_decoder_theorem.md`.  It is the natural
version to use when several quotient fibres are nonsingleton and each fibre
has its own transparent finite readout.

## Statement

Let `X` be a finite bijective YBE solution.  Suppose there is a braided
quotient

```text
pi:X -> Z,
```

and suppose `Z` is dominated by a finite rack `Y_Z`:

```text
ker rho^{Y_Z}_n <= ker rho^Z_n
```

for every `n`.

For each quotient color `a in Z`, let `W_a` be a finite bijective YBE solution
dominated by a finite rack `Y_a`:

```text
ker rho^{Y_a}_n <= ker rho^{W_a}_n
```

for every `n`.

Let `W_a^0` denote the transparent YBE extension of `W_a`, obtained by adding
a color `0` with

```text
R(0,w)=(w,0),
R(w,0)=(0,w),
R(0,0)=(0,0).
```

Assume that for every `a in Z` and every arity `n`, there is a readout

```text
Gamma^a_n:X^n -> (W_a^0)^n
```

satisfying braid equivariance:

```text
Gamma^a_n(rho^X_n(beta)(x))
  =
rho^{W_a^0}_n(beta)(Gamma^a_n(x))
```

for all `beta in B_n` and `x in X^n`, and satisfying support transparency:

```text
Gamma^a_n(x)_i = 0 whenever pi(x_i) != a.
```

Finally assume the combined decoder

```text
D_n:X^n -> Z^n x product_{a in Z} (W_a^0)^n
```

given by

```text
D_n(x) = (pi^n(x), (Gamma^a_n(x))_{a in Z})
```

is injective for every `n`.

Then `X` is dominated by the finite rack

```text
Y = Y_Z x product_{a in Z} Y_a^0.
```

That is,

```text
ker rho^Y_n <= ker rho^X_n
```

for every `n`.

## Proof

For each `a`, the rack transparent extension `Y_a^0` dominates the YBE
transparent extension `W_a^0`.  Indeed, if a braid is trivial on
`(Y_a^0)^n`, then for every subset of nontransparent strands the induced
deleted braid is trivial on the corresponding `Y_a` subword.  Since `Y_a`
dominates `W_a`, the deleted braid is trivial on the corresponding `W_a`
subword.  Hence the original braid is trivial on `(W_a^0)^n`.

Equivalently, the product

```text
U = product_{a in Z} W_a^0
```

is dominated by

```text
Y_U = product_{a in Z} Y_a^0.
```

Define

```text
Gamma_n:X^n -> U^n
```

coordinatewise by

```text
Gamma_n(x)_i = (Gamma^a_n(x)_i)_{a in Z}.
```

Since each `Gamma^a_n` is braid-equivariant, `Gamma_n` is braid-equivariant
for the product solution `U`.  The assumed combined decoder is exactly

```text
(pi^n, Gamma_n):X^n -> Z^n x U^n.
```

It is injective by hypothesis.  The finite-state dominated-decoder theorem
therefore gives

```text
ker rho^{Y_Z x Y_U}_n <= ker rho^X_n
```

for every `n`, which is the claimed domination by
`Y_Z x product_a Y_a^0`.

## Local Certificate

The corollary is often certified by one shared finite context system.  Let
`L,R` be finite monoids, with updates

```text
lambda:X -> L,
rho:X -> R.
```

For `R_X(x,y)=(u,v)`, assume

```text
lambda(x) lambda(y)=lambda(u) lambda(v),
rho(y) rho(x)=rho(v) rho(u).
```

For each `a in Z`, let

```text
gamma_a:L x X x R -> W_a^0
```

be a finite local readout with

```text
gamma_a(A,x,B)=0 whenever pi(x) != a.
```

Define contexts

```text
A_1=1_L,
A_{i+1}=A_i lambda(x_i),
B_n=1_R,
B_i=B_{i+1} rho(x_{i+1}),
```

and

```text
Gamma^a_n(x)_i = gamma_a(A_i,x_i,B_i).
```

The following local identity for all `A in L`, `B in R`, and `x,y in X`
with `R_X(x,y)=(u,v)` is a finite sufficient certificate for equivariance:

```text
R_{W_a^0}(
  gamma_a(A,x,B rho(y)),
  gamma_a(A lambda(x),y,B)
)
 =
(
  gamma_a(A,u,B rho(v)),
  gamma_a(A lambda(u),v,B)
).
```

It is an exact necessary condition on all reachable context pairs; requiring
it for every `A,B` is the convenient finite global certificate.

## Finite Injectivity Test

With the shared local context data above, all-arity injectivity of `D_n` is a
finite graph test.

Build a finite directed graph with vertices

```text
(A,A',B,B',x,x') in L^2 x R^2 x X^2
```

satisfying

```text
pi(x)=pi(x')
```

and

```text
gamma_a(A,x,B)=gamma_a(A',x',B')       for every a in Z.
```

There is an edge

```text
(A,A',B,B',x,x') -> (bar A,bar A',bar B,bar B',y,y')
```

iff

```text
bar A  = A  lambda(x),
bar A' = A' lambda(x'),
B  = bar B  rho(y),
B' = bar B' rho(y').
```

Initial vertices have `A=A'=1_L`; terminal vertices have `B=B'=1_R`.
Then `D_n` fails to be injective for some `n` if and only if this graph has
an initial-to-terminal path containing at least one coordinate mismatch
`x_i != x_i'`.  If a collision exists, one exists with

```text
n <= 2 |L|^2 |R|^2 |X|^2.
```

## Use

This corollary packages multi-fibre hidden data into transparent dominated
channels.  It strictly generalizes the one-fibre gap-gauge mechanism when a
solution has several nonsingleton quotient fibres, provided each fibre has a
dominated transparent readout and the product of those readouts jointly
decodes `X^n` with the quotient.

The remaining positive target is to construct such quotient and transparent
decoder data for arbitrary finite degenerate `X`, or to find a fixed finite
`X` for which every such finite decoder family fails and convert that failure
into cofinal Brunnian rack-prefix witnesses.
