# Quotient-Controlled Species-Gauge Theorem

Date: 2026-06-08

This note records the quotient-controlled injective-gauge subcase of the
species-indexed transparent decoder theorem.  In this subcase the all-arity
injectivity graph is unnecessary: once a detector-kernel braid fixes the
quotient word, the quotient-controlled contexts are fixed, and fibrewise
injective gauges recover each hidden coordinate directly.

## Statement

Let

```text
pi:X -> Z
```

be a braided quotient of finite bijective YBE solutions.  Let

```text
sigma:Z -> S=Sp(Z)
```

be the strand-species quotient, so if

```text
R_Z(z,w)=(u,v),
```

then

```text
sigma(u)=sigma(w),
sigma(v)=sigma(z).
```

Assume `Z` is dominated by a finite rack `Y_Z`.

For every species `s in S`, let `W_s` be a finite bijective YBE solution
dominated by a finite rack `Y_s`.

For each `z in Z`, write

```text
X_z = pi^{-1}(z).
```

Assume there are finite monoids `L,R`, quotient-context updates

```text
lambda:Z -> L,
rho:Z -> R,
```

and, for each species `s`, each `z in Z` with `sigma(z)=s`, and each
`A in L`, `B in R`, an injective gauge map

```text
G^s_{A,z,B}:X_z -> W_s.
```

For `x in X_z`, define

```text
gamma_s(A,x,B) =
  G^s_{A,z,B}(x)  if sigma(z)=s,
  0               if sigma(z)!=s,
```

where `0` is the transparent colour in `W_s^0`.

Assume quotient-context preservation: for every quotient crossing

```text
R_Z(z,w)=(u,v),
```

one has

```text
lambda(z) lambda(w)=lambda(u) lambda(v),
rho(w) rho(z)=rho(v) rho(u).
```

Assume the finite local crossing identities hold: for every

```text
R_X(x,y)=(x',y'),
```

with

```text
z=pi(x),   w=pi(y),
u=pi(x'),  v=pi(y'),
```

and for every `A in L`, `B in R`, and `s in S`,

```text
R_{W_s^0}(
  gamma_s(A,x,B rho(w)),
  gamma_s(A lambda(z),y,B)
)
 =
(
  gamma_s(A,x',B rho(v)),
  gamma_s(A lambda(u),y',B)
).
```

Then

```text
Y_Z x product_{s in S} Y_s^0
```

dominates `X`:

```text
ker rho^{Y_Z x product_s Y_s^0}_n <= ker rho^X_n
```

for every `n`.

## Proof

For a word

```text
x=(x_1,...,x_n) in X^n,
```

write

```text
z_i = pi(x_i).
```

Define quotient-controlled contexts

```text
A_1=1_L,
A_{i+1}=A_i lambda(z_i),
B_n=1_R,
B_i=B_{i+1} rho(z_{i+1}).
```

For each species `s`, define

```text
Gamma^s_n(x)_i = gamma_s(A_i,x_i,B_i) in W_s^0.
```

The local crossing identity proves, generator by generator, that

```text
Gamma^s_n(rho^X_n(beta)(x))
  =
rho^{W_s^0}_n(beta)(Gamma^s_n(x))
```

for every braid `beta`.  It is enough to check positive braid generators:
the `X` and `W_s^0` generator actions are bijections, so inverse-generator
equivariance follows by applying the positive-generator identity to the
preimage and rearranging.  The context identities are quotient-level
identities, so all contexts outside a crossing block are preserved by a
generator.  The support condition is compatible with transparent crossings
because the species quotient gives

```text
sigma(u)=sigma(w),
sigma(v)=sigma(z)
```

for every quotient crossing `R_Z(z,w)=(u,v)`.

Now let

```text
beta in ker rho^{Y_Z x product_s Y_s^0}_n.
```

Since `Y_Z` dominates `Z`,

```text
rho^Z_n(beta)=1.
```

Since each `Y_s` dominates `W_s`, the transparent extension `Y_s^0` dominates
`W_s^0`, so

```text
rho^{W_s^0}_n(beta)=1
```

for every `s`.

Fix `x in X^n`, and put

```text
x' = rho^X_n(beta)(x).
```

Because `pi` is braided and `rho^Z_n(beta)=1`,

```text
pi^n(x') = pi^n(x).
```

Therefore every coordinate has the same quotient colour:

```text
pi(x_i') = pi(x_i) = z_i.
```

Since the quotient word is unchanged, all quotient-controlled contexts are
unchanged:

```text
A_i'=A_i,
B_i'=B_i.
```

For every species `s`,

```text
Gamma^s_n(x')
  =
rho^{W_s^0}_n(beta)(Gamma^s_n(x))
  =
Gamma^s_n(x).
```

Take a coordinate `i`, and let

```text
s = sigma(z_i).
```

Then

```text
G^s_{A_i,z_i,B_i}(x_i')
  =
Gamma^s_n(x')_i
  =
Gamma^s_n(x)_i
  =
G^s_{A_i,z_i,B_i}(x_i).
```

Both `x_i` and `x_i'` lie in `X_{z_i}`, and the gauge
`G^s_{A_i,z_i,B_i}:X_{z_i}->W_s` is injective.  Hence

```text
x_i'=x_i.
```

This holds for every coordinate, so `rho^X_n(beta)(x)=x`.  Since `x` was
arbitrary,

```text
beta in ker rho^X_n.
```

Thus the desired kernel inclusion holds in every arity.

## Use

This theorem removes the finite all-arity injectivity graph in the important
quotient-controlled case.  The stronger finite hypothesis is simply:

```text
each gauge G^s_{A,z,B}:X_z -> W_s is injective.
```

Because the contexts are computed from the quotient word alone, a braid that
is invisible to the quotient detector uses the same gauge before and after
the braid.  Fibrewise injectivity then recovers the hidden coordinate.

The theorem captures the mechanism behind the six-point `F_3` closures:

```text
quotient motion
  +
quotient-controlled fibre gauge
  +
internal dominated fibre detector
  =>
domination of X.
```

The remaining obstruction class is narrower: a finite degenerate solution
whose useful quotients have hidden fibre transport depending essentially on
hidden fibre context, not quotient context alone.  Equivalently, a
counterexample must evade quotient-controlled injective gauges and force
genuinely self-referential hidden monodromy inside a strand species.
