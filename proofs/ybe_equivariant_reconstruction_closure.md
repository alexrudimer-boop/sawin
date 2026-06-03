# YBE equivariant reconstruction closure

Date: 2026-06-03

This note records the sharp safe gluing theorem for known finite-rack
detector branches.

Let `X` be a finite bijective YBE solution, with braid action

```text
rho^X_n:B_n -> Sym(X^n).
```

Suppose that, for each `alpha` in a finite set `A`, there is a finite marked
braid tower

```text
T^alpha_bullet=(T^alpha_n,rho^alpha_n)
```

and `B_n`-equivariant maps

```text
f^alpha_n:X^n -> T^alpha_n
```

for every `n`.  Assume each tower `T^alpha_bullet` is dominated by a finite
rack `Y_alpha`, meaning

```text
ker(B_n acting on Y_alpha^n) <= ker(rho^alpha_n)
```

for every `n`.

Define the visible reconstruction map

```text
F_n:X^n -> prod_alpha T^alpha_n,
F_n(x)=(f^alpha_n(x))_alpha.
```

If `F_n` is injective for every `n`, then the product rack

```text
Y=prod_alpha Y_alpha
```

dominates `X`.

Indeed, the braid action on `Y^n` is the product of the actions on the
`Y_alpha^n`, so

```text
ker(B_n acting on Y^n)
= intersection_alpha ker(B_n acting on Y_alpha^n).
```

If `beta` lies in this kernel, then `beta` acts trivially on every
`T^alpha_n`.  Hence, for every `x in X^n`,

```text
f^alpha_n(rho^X_n(beta)x)
= rho^alpha_n(beta) f^alpha_n(x)
= f^alpha_n(x)
```

for every `alpha`.  Thus

```text
F_n(rho^X_n(beta)x)=F_n(x).
```

By injectivity of `F_n`,

```text
rho^X_n(beta)x=x.
```

Therefore

```text
ker(B_n acting on Y^n) <= ker(B_n acting on X^n)
```

for every `n`.

## Total Quotients

For genuine total YBE quotient maps

```text
pi_j:X -> Z_j
```

the coordinatewise maps

```text
pi_{j,n}:X^n -> Z_j^n
```

are `B_n`-equivariant.  If

```text
pi=(pi_j)_j:X -> prod_j Z_j
```

is injective, then

```text
pi^n:X^n -> prod_j Z_j^n
```

is injective for every `n`.  Consequently, if every `Z_j` is dominated by a
finite rack, then `X` is dominated by the product of those racks.

Thus point-separating total quotient maps are enough, provided they are
genuine YBE quotient maps.

## Partial Data

Partial subquotients and crossing-closed block detectors are usable only
after they are promoted to total marked braid factors.  A partial readout must
come from some finite `B_n`-set `T_n` and a total equivariant map

```text
f_n:X^n -> T_n
```

that records the intended partial data wherever that data is supported.
Equivalently, the relation

```text
x ~_n x'  iff  f_n(x)=f_n(x')
```

must be a `B_n`-congruence.

For a coordinatewise quotient relation `~` on `X`, this means that whenever
`x~x'`, `y~y'`, and

```text
r(x,y)=(u,v),      r(x',y')=(u',v'),
```

then

```text
u~u',      v~v'.
```

For a block decomposition `X=coprod_i B_i`, the block labels define a YBE
quotient only when the output block pair of `r(x,y)` depends only on the
input block pair.  For a partial subquotient `g_i:B_i -> W_i`, every supported
crossing transition must also descend to the `W_i` labels.

## Extension Fibres

Let

```text
pi:X -> Z
```

be a genuine YBE quotient and write `X` as fibres

```text
X = coprod_{z in Z} F_z.
```

If

```text
r_Z(z,z')=(u,v),
```

then the full solution over `Z` includes fibre bijections

```text
phi_{z,z'}:F_z x F_{z'} -> F_u x F_v.
```

The YBE equation for `X` is the YBE equation for `Z` together with the arity-3
fibre cocycle equation.  For a base triple `z=(z_1,z_2,z_3)`, let `Phi_i(z)`
be the fibre map induced by `phi_{z_i,z_{i+1}}` on the `i,i+1` fibre
coordinates.  Then

```text
Phi_1(r_2 r_1 z) Phi_2(r_1 z) Phi_1(z)
=
Phi_2(r_1 r_2 z) Phi_1(r_2 z) Phi_2(z).
```

Detectors that see the quotient and same-block restrictions but not these
off-diagonal maps do not determine the action on `X^n`.

## Exact Criterion

For any finite family of visible marked factors, define

```text
K_vis,n = intersection_alpha ker(rho^alpha_n)
```

and, for `t in prod_alpha T^alpha_n`, define the hidden reconstruction fibre

```text
H_t = F_n^{-1}(t).
```

The visible product detectors dominate `X` if and only if `K_vis,n` acts
trivially on every hidden fibre `H_t`, for every `n`.  Injectivity of `F_n` is
the clean sufficient condition because then each hidden fibre has at most one
element.

Therefore the true closure theorem is not "dominated pieces glue."  It is:

```text
total equivariant marked factors + all-arity injective reconstruction
imply finite rack domination by the product detector.
```

If reconstruction is not injective, one must additionally prove that the
visible-kernel braid action on hidden fibres is trivial.  Point-separating
quotients, separately dominated components, or partial subquotients do not
imply this unless the off-diagonal transition and extension cocycle data are
included.
