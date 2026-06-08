# F3 Deterministic Context Quotient And Harmless Collapse

This note records the computation of the deterministic actual-transition
quotient `P_det` for the three-point affine solution

```text
X=F_3,        R_X(x,y)=(-y, x-y).
```

It also records why the collapsed pure Brunnian transition in this example is
harmless for finite-rack residual complexity.

## The Solution

All arithmetic is modulo `3`.  The inverse is

```text
R_X^{-1}(u,v)=(v-u, -u),
```

so `R_X` is bijective.  The braid-form YBE holds because both sides send

```text
(x,y,z) -> (z, z-y, x-y-z).
```

The context maps are translations.  Put `e_i(z)=z-i`.  Then

```text
r_y=e_y,        m_u=e_u,
```

and

```text
M_L=M_R={e_0,e_1,e_2}.
```

Write a raw contextual state as

```text
(i,a,j) in F_3^3,
```

meaning `(e_i,a,e_j)`.

## Adjacent Crossing Formula

For `A=e_i`, `B=e_j`, and incoming colors `x,y`, with

```text
R_X(x,y)=(-y, x-y),
```

the actual adjacent contextual states are

```text
ell     = (i,   x,   j+y),
rr      = (i+x, y,   j),
bar_rr  = (i,   -y,  j+x-y),
bar_ell = (i-y, x-y, j).
```

The deterministic quotient is the least equivalence relation containing all
stationary equalities

```text
rr ~ bar_rr
```

and closed under output determinism:

```text
ell_c ~ ell_d and rr_c ~ rr_d  =>  bar_ell_c ~ bar_ell_d.
```

## Stationary Quotient

The stationary relation preserves

```text
s=i+a+j in F_3
```

and whether `a` is zero.  Thus the stationary quotient has six classes

```text
Z_s={(i,0,j): i+j=s},
N_s={(i,a,j): a!=0, i+a+j=s},
```

for `s in F_3`.

## Deterministic Closure

Every actual crossing preserves the total

```text
s=i+a+j.
```

Indeed `ell`, `rr`, and `bar_ell` above all have the same total
`i+j+x+y`.

Within a fixed `s`, the stationary quotient has an ambiguous input pair

```text
(N_s,N_s).
```

If `x=y!=0`, then `x-y=0`, so the left output lies in `Z_s`.  If
`x,y!=0` and `x!=y`, then `x-y!=0`, so the left output lies in `N_s`.
Determinism therefore forces

```text
Z_s ~ N_s
```

for each `s`.  Since `s` is preserved by all actual crossings, there are no
further merges.  Hence

```text
P_det={C_0,C_1,C_2},
```

where

```text
C_s={(i,a,j): i+a+j=s}.
```

The induced actual partial operation is diagonal:

```text
C_s ▷ C_s = C_s.
```

No actual adjacent crossing produces an input pair `(C_s,C_t)` with `s!=t`.

## The Collapsed Brunnian Transition

Let

```text
p =(0,1,2),
p'=(2,0,1).
```

Both have total `0`, so

```text
p,p' in C_0.
```

Thus the deterministic quotient collapses the transition.

The transition is genuinely realized by the pure Brunnian braid

```text
beta=[sigma_2^2, sigma_1^2] in B_3.
```

Starting from `(0,1,2)`, the trajectory is

```text
(0,1,2) --sigma_2^2-->  (0,1,2)
        --sigma_1^2-->  (1,0,2)
        --sigma_2^-2--> (1,1,1)
        --sigma_1^-2--> (2,0,1).
```

Since `beta` is pure, the middle physical strand returns to the middle
coordinate.  Its initial context is `(0,1,2)=p`, and its final context is
`(2,0,1)=p'`.

## Rack Conjugacy

The collapse is harmless because the whole `X` braid action is conjugate to a
three-element rack action.

Let `Y=F_3` with rack operation

```text
s ▷ t = -s-t.
```

This is the three-element dihedral quandle: right translations are bijections
and

```text
(s ▷ t) ▷ u = s+t-u
```

equals

```text
(s ▷ u) ▷ (t ▷ u).
```

Define

```text
J_n(x_1,...,x_n)=(x_1,-x_2,x_3,-x_4,...,(-1)^{j-1}x_j,...).
```

For generator `sigma_i`, put `s=(-1)^{i-1}`.  The two `Y` colors before the
crossing are

```text
a=sx,        b=-sy.
```

The `X` crossing sends `(x,y)` to `(-y,x-y)`.  Applying `J_n` gives

```text
b,        -sx+sy.
```

But

```text
a ▷ b = -a-b = -sx+sy.
```

Therefore

```text
J_n rho^X_n(sigma_i) = rho^Y_n(sigma_i) J_n
```

for every generator and hence every braid.

Consequently, every `X`-visible braid is detected by the three-element rack
`Y`.  In particular every pure color-changing contextual witness in this
example satisfies

```text
r(beta) <= 3.
```

Thus the collapsed transition is a failure of the deterministic one-strand
contextual detector, not an unbounded residual-complexity obstruction.

## Consequence

The example shows that `P_det` can collapse genuine pure Brunnian
color-changing transitions.  Such a collapse must not be treated as a
counterexample without an unbounded residual-complexity sequence.  In this
case no such sequence exists, because the entire solution is already dominated
by the three-element dihedral rack.
