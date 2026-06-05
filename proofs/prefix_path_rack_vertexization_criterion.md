# Prefix-Path Rack Vertexization Criterion

Date: 2026-06-05

This note records the exact finite rack theorem for prefix-path data.  Product
observers alone are not enough; the missing structure is a finite rack
vertexization of the prefix-path groupoid, or else a proper kernel-reflecting
active factor.

## Convention

This note uses the rack convention

```text
r_Y(a,b)=(b,b triangleright a).
```

Equivalently, the second input acts on the first input.  This is just a
notational variant of the right-rack convention used in the product-Hurwitz
note.

## Prefix-path data

Let

```text
S=S_L^1
```

be the left coordinate monoid with identity.  For

```text
x=(x_1,...,x_n)
```

define prefix products

```text
p_0=1,
p_i=L_{x_1}...L_{x_i}.
```

The prefix-path code

```text
P_n^L(x_1,...,x_n)=
    ((p_0,x_1),(p_1,x_2),...,(p_{n-1},x_n))
```

is injective, but it is not automatically a rack coordinate system.  Under a
local rewrite

```text
r_X(x,y)=(u,v),
```

the valid path pair rewrites as

```text
(p,x),(pL_x,y) -> (p,u),(pL_u,v).
```

A rack rewrite must have the form

```text
(A,B) -> (B,B triangleright A).
```

The vertexization criterion is exactly the finite condition that makes these
forms agree after applying a finite rack coordinate map.

## Theorem

Suppose there exist:

```text
1. a finite rack Y;
2. a map psi:S x X -> Y;
3. finite inert observer maps iota_n:X^n -> I_n.
```

For every `p in S` and every `x,y in X`, write

```text
r_X(x,y)=(u,v).
```

Require

```text
psi(p,u) = psi(pL_x,y),                                    (V1)
psi(pL_u,v) = psi(pL_x,y) triangleright psi(p,x).          (V2)
```

Define

```text
Psi_n(x_1,...,x_n)=
    (psi(p_0,x_1), psi(p_1,x_2), ..., psi(p_{n-1},x_n)).
```

If

```text
F_n=(Psi_n,iota_n):X^n -> Y^n x I_n
```

is injective for every `n`, and `iota_n` is `B_n`-invariant, then

```text
ker rho_n^Y <= ker rho_n^X
```

for every `n`.

## Proof

It is enough to check braid generators.  Let `sigma_i` act on adjacent entries

```text
x_i=x,  x_{i+1}=y,
```

with

```text
r_X(x,y)=(u,v).
```

Put `p=p_{i-1}`.  Before the move, the two local rack coordinates are

```text
A=psi(p,x),
B=psi(pL_x,y).
```

After the move, the two local coordinates are

```text
A'=psi(p,u),
B'=psi(pL_u,v).
```

By `(V1)` and `(V2)`,

```text
(A',B')=(B,B triangleright A)=r_Y(A,B).
```

Later prefix states remain valid because the YBE product identity gives

```text
pL_uL_v=pL_xL_y.
```

Thus

```text
Psi_n(sigma_i x)=sigma_i^Y Psi_n(x).
```

Since `iota_n` is inert, `F_n` is equivariant for the product action
`rho_n^Y x id`.

If `beta in ker rho_n^Y`, then

```text
F_n(beta x)=F_n(x)
```

for all `x`.  Injectivity of `F_n` gives `beta x=x` for all `x`, hence

```text
beta in ker rho_n^X.
```

This proves the theorem.

## Why this is the exact missing structure

The raw prefix-path code is injective but not rack-valued.  Two obvious maps
show the gap.

First, taking

```text
psi(p,x)=(p,x)
```

preserves injectivity, but `(V1)` becomes

```text
(p,u)=(pL_x,y),
```

which is false in general.

Second, taking the projected guitar-type map

```text
psi(p,x)=p(x)
```

makes `(V1)` automatic because

```text
p(u)=pL_x(y).
```

But `(V2)` then demands that

```text
pL_{L_x(y)}(R_y(x)) =
    (pL_x(y)) triangleright p(x)
```

define a genuine finite rack operation independent of the choice of `p,x,y`.
Even if this operation is well-defined, `(Psi_n,iota_n)` must still be
injective in every arity.

Therefore the actual structure needed is a finite vertex-face transform

```text
psi:S_L^1 x X -> Y
```

plus inert separators, not merely the endpoint observer `Lambda_n`.

## Active-factor/vertexization dichotomy target

The corrected product-observer branch is:

```text
If a finite solution has unavoidable product observers, then either
  it has a proper kernel-reflecting active factor,
or
  its prefix-path groupoid admits a finite rack vertexization.
```

The first case supports induction or minimality.  The second case gives direct
rack domination by the theorem above.

Product observers alone give neither.

## Minimal-ideal warning

Minimal-ideal local groups do not supply vertexization automatically.  If `e`
is an idempotent in a minimal ideal, YBE gives

```text
eL_uL_ve = eL_xL_ye,
```

but a local-group construction would need

```text
eL_ueL_ve = eL_xeL_ye.
```

The inserted `e` changes the intermediate Rees sandwich entry.  The prefix
state `p` in `psi(p,x)` is precisely the kind of data needed to remember that
intermediate transition, but a finite rack quotient preserving enough of that
data is an additional theorem, not automatic.

