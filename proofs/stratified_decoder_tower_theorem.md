# Stratified Decoder-Tower Theorem

Date: 2026-06-08

This note records the iterated version of the finite-state and species
transparent decoder mechanisms.  It addresses the case where hidden fibre
transport is not controlled by one quotient layer, but becomes controlled
after peeling a finite tower of braided quotients.

## Statement

Let

```text
X = X^(r) -> X^(r-1) -> ... -> X^(1) -> X^(0)
```

be a tower of finite bijective YBE solutions with braided quotient maps

```text
pi_k:X^(k) -> X^(k-1)        (1 <= k <= r).
```

Assume `X^(0)` is dominated by a finite rack `Y_0`.

For each layer `k=1,...,r`, let

```text
S_k = Sp(X^(k-1))
```

be the strand-species quotient of the lower layer.  For each species
`s in S_k`, let `W_{k,s}` be a finite bijective YBE solution dominated by a
finite rack `Y_{k,s}`.

Assume that for every `k,s,n`, there is a transparent readout

```text
Gamma^{k,s}_n:(X^(k))^n -> (W_{k,s}^0)^n
```

satisfying braid equivariance:

```text
Gamma^{k,s}_n(rho^{X^(k)}_n(beta)(x))
  =
rho^{W_{k,s}^0}_n(beta)(Gamma^{k,s}_n(x))
```

for every braid `beta`, and satisfying species support:

```text
Gamma^{k,s}_n(x)_i = 0
  whenever sigma_k(pi_k(x_i)) != s,
```

where

```text
sigma_k:X^(k-1) -> Sp(X^(k-1))
```

is the lower-layer species quotient.

Finally assume that the layer decoder

```text
D^{(k)}_n:(X^(k))^n
  -> (X^(k-1))^n x product_{s in S_k} (W_{k,s}^0)^n
```

defined by

```text
D^{(k)}_n(x)
  =
(pi_k^n(x), (Gamma^{k,s}_n(x))_{s in S_k})
```

is injective for every `n`.

Then `X=X^(r)` is dominated by the finite rack

```text
Y =
Y_0 x product_{k=1}^r product_{s in S_k} Y_{k,s}^0.
```

Equivalently,

```text
ker rho^Y_n <= ker rho^X_n
```

for every `n`.

## Proof

Proceed by induction on the tower.

Assume `X^(k-1)` is dominated by a finite rack `Y_{<k}`.  Define

```text
Y_{<=k} =
Y_{<k} x product_{s in S_k} Y_{k,s}^0.
```

Let

```text
beta in ker rho^{Y_{<=k}}_n.
```

Then `beta in ker rho^{Y_{<k}}_n`, so by the induction hypothesis

```text
rho^{X^(k-1)}_n(beta)=1.
```

Also

```text
beta in ker rho^{Y_{k,s}^0}_n
```

for every `s`.  Since `Y_{k,s}` dominates `W_{k,s}`, its transparent
extension `Y_{k,s}^0` dominates `W_{k,s}^0`; hence

```text
rho^{W_{k,s}^0}_n(beta)=1
```

for every `s`.

Take any

```text
x in (X^(k))^n
```

and set

```text
x' = rho^{X^(k)}_n(beta)(x).
```

Because `pi_k` is braided,

```text
pi_k^n(x')
  =
rho^{X^(k-1)}_n(beta)(pi_k^n(x))
  =
pi_k^n(x).
```

Because each `Gamma^{k,s}` is braid-equivariant,

```text
Gamma^{k,s}_n(x')
  =
rho^{W_{k,s}^0}_n(beta)(Gamma^{k,s}_n(x))
  =
Gamma^{k,s}_n(x)
```

for every `s`.  Therefore

```text
D^{(k)}_n(x')=D^{(k)}_n(x).
```

By injectivity of `D^{(k)}_n`, `x'=x`.  Thus

```text
beta in ker rho^{X^(k)}_n.
```

So `Y_{<=k}` dominates `X^(k)`.  Starting from `X^(0)`, induction gives
domination of `X=X^(r)`.

## Finite Local Certificate For A Layer

Fix a layer `k`.  The theorem is checkable when `Gamma^{k,s}` is built from
finite context over the lower layer `X^(k-1)`.

Let `L_k,R_k` be finite monoids, and let

```text
lambda_k:X^(k-1) -> L_k,
rho_k:X^(k-1) -> R_k
```

satisfy, for every

```text
R_{X^(k-1)}(a,b)=(c,d),
```

the context preservation identities

```text
lambda_k(a) lambda_k(b)=lambda_k(c) lambda_k(d),
rho_k(b) rho_k(a)=rho_k(d) rho_k(c).
```

For each species `s in S_k`, choose

```text
gamma_{k,s}:L_k x X^(k) x R_k -> W_{k,s}^0
```

with support condition

```text
gamma_{k,s}(A,x,B)=0
  unless sigma_k(pi_k(x))=s.
```

Given

```text
x=(x_1,...,x_n) in (X^(k))^n,
```

write

```text
a_i = pi_k(x_i) in X^(k-1).
```

Define lower-layer contexts

```text
A_1=1,
A_{i+1}=A_i lambda_k(a_i),
B_n=1,
B_i=B_{i+1} rho_k(a_{i+1}).
```

Set

```text
Gamma^{k,s}_n(x)_i =
gamma_{k,s}(A_i,x_i,B_i).
```

Then `Gamma^{k,s}` is braid-equivariant if the finite local identity holds:
whenever

```text
R_{X^(k)}(x,y)=(u,v),
```

with

```text
a=pi_k(x),  b=pi_k(y),
c=pi_k(u),  d=pi_k(v),
```

then for every `A in L_k`, `B in R_k`,

```text
R_{W_{k,s}^0}(
  gamma_{k,s}(A,x,B rho_k(b)),
  gamma_{k,s}(A lambda_k(a),y,B)
)
 =
(
  gamma_{k,s}(A,u,B rho_k(d)),
  gamma_{k,s}(A lambda_k(c),v,B)
).
```

As in the finite-state decoder theorem, checking positive generators is
enough because all involved generator actions are bijections.  These local
identities are finite sufficient certificates; they are literally necessary
only on reachable context pairs.

## Automatic Layer Injectivity By Fibrewise Gauges

The injectivity of `D^{(k)}_n` is automatic if each local readout separates
fibres of `pi_k` at fixed lower context.

Specifically, suppose that for every

```text
A in L_k, B in R_k, a in X^(k-1),
```

the map

```text
x in pi_k^{-1}(a)
  ->
(gamma_{k,s}(A,x,B))_{s in S_k}
```

is injective.

Then `D^{(k)}_n` is injective for every `n`.

Indeed, if two words `x,x' in (X^(k))^n` have the same `D^{(k)}_n`, then

```text
pi_k(x_i)=pi_k(x_i')=a_i
```

for every coordinate.  The lower word `(a_i)` is the same, so the lower
contexts `A_i,B_i` are the same.  Equality of all `Gamma^{k,s}` gives

```text
(gamma_{k,s}(A_i,x_i,B_i))_s
  =
(gamma_{k,s}(A_i,x_i',B_i))_s.
```

Fibrewise injectivity gives `x_i=x_i'` for every `i`.  Hence `x=x'`.

## Use

This theorem handles hidden data that becomes quotient-controlled only after
introducing additional lower layers.  It includes:

- quotient/product closures;
- one-fibre passive gauges;
- gap gauges;
- active internal-fibre gauges;
- finite iterated versions of those mechanisms.

It does not prove Sawin's statement by itself.  It turns the next obstruction
into a sharper finite target: a minimal counterexample must evade every
finite stratified decoder tower.  Concretely, it must be braided-simple
degenerate non-involutive, or nonsimple with no proper quotient admitting a
dominated transparent species decoder layer, or must have hidden monodromy
that remains genuinely self-referential inside one strand species at every
finite quotient depth.
