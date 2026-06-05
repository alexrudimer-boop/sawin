# Product-Hurwitz Separability Branch

Date: 2026-06-05

This note records the corrected status of product observers.  The product
observers `Lambda_n` and `Gamma_n` are genuine broad arity-dependent inert
observers, but their existence alone does not reduce Sawin's problem.  The
usable positive replacement is a suffix-local product-Hurwitz rackification
criterion.

This note uses the right-rack convention

```text
r_Y(a,b)=(b,a triangleright b).
```

## No-go theorem

Product observers alone do not imply rack domination.

Let `Z` be any finite bijective YBE solution.  Let `E` be a finite set with
`|E|>=2` and give `E` the identity solution

```text
r_E(a,b)=(a,b).
```

Then

```text
L_a^E(b)=a,    R_b^E(a)=b,
```

so every coordinate map of `E` is singular.  Form the direct product solution

```text
X = E x Z
```

with

```text
r_X((a,z),(b,w)) =
    ((a,L_z^Z(w)), (b,R_w^Z(z))).
```

This is finite, bijective, and everywhere-singular.  The braid action on

```text
X^n = E^n x Z^n
```

is

```text
rho_n^X = id_{E^n} x rho_n^Z.
```

Therefore

```text
ker rho_n^X = ker rho_n^Z
```

for every `n`.  Hence `X` is rack-dominated if and only if `Z` is
rack-dominated.  The everywhere-singular branch is therefore not a smaller
endpoint by itself.

This also explains why product observers cannot drive induction alone.  The
identity factor supplies nonconstant inert observers, while each observer fiber
can still carry the full hidden braid dynamics of `Z`.

## What the left product observer gives

Let

```text
S_L=<L_x:x in X>
```

and adjoin an identity, writing `S_L^1`.  For

```text
x=(x_1,...,x_n)
```

define suffix products

```text
s_{n+1}=1,
s_i=L_{x_i}s_{i+1}.
```

Then

```text
s_i=L_{x_i}L_{x_{i+1}}...L_{x_n},
s_1=Lambda_n(x).
```

If a braid generator acts at adjacent entries `x,y` and

```text
r(x,y)=(u,v),
```

then for `t=s_{i+2}`,

```text
s_{i+1}=L_y t,      s_i=L_x L_y t,
s'_{i+1}=L_v t,     s'_i=L_u L_v t.
```

The YBE product identity `L_uL_v=L_xL_y` gives `s'_i=s_i`.  Thus
`Lambda_n` records an endpoint of a finite path system in the Cayley graph of
`S_L^1`, but the local move can change intermediate suffix states.  It is a
finite braided path category, not automatically a power of a smaller YBE
solution.

## Product-Hurwitz separability

The following condition is a genuine sufficient theorem for rack domination.
It is stronger than general active-factor observability and weaker than a proof
of Sawin, because it demands explicit suffix-local rack labels.

Assume there are:

```text
1. a finite rack (Y, triangleright);
2. maps c_t:X -> Y for each t in S_L^1;
3. finite inert observer data J_n:X^n -> J_n.
```

For all `x,y in X` and `t in S_L^1`, write

```text
u=L_x(y),    v=R_y(x).
```

Require the product-Hurwitz identities

```text
c_{L_v t}(u) = c_t(y),                                      (LH1)
c_t(v) = c_{L_y t}(x) triangleright c_t(y).                 (LH2)
```

For a word `x=(x_1,...,x_n)`, define suffixes as above and set

```text
C_n(x) =
    ( c_{s_2}(x_1), c_{s_3}(x_2), ..., c_{s_{n+1}}(x_n) )
    in Y^n.
```

Assume finally that

```text
F_n(x) = (C_n(x), Lambda_n(x), J_n(x))
```

is injective for every `n`, with `Lambda_n` and `J_n` treated as inert
observers.

Then

```text
ker rho_n^Y <= ker rho_n^X
```

for every `n`.

Proof: under a local braid move at adjacent entries `x,y`, let
`r(x,y)=(u,v)` and `t=s_{i+2}`.  The old rack labels are

```text
a=c_{L_y t}(x),
b=c_t(y).
```

The new rack labels are

```text
a'=c_{L_v t}(u),
b'=c_t(v).
```

By `(LH1)` and `(LH2)`,

```text
(a',b') = (b, a triangleright b) = r_Y(a,b).
```

Thus `C_n` is `B_n`-equivariant.  If `beta in ker rho_n^Y`, then `C_n`,
`Lambda_n`, and `J_n` all agree on `x` and `beta x`.  Injectivity of `F_n`
forces `beta x=x` for all `x`, proving kernel containment.

## Right product version

There is a dual criterion using

```text
Gamma_n(x_1,...,x_n)=R_{x_n}...R_{x_1}.
```

Let `S_R=<R_x:x in X>` and define prefix products

```text
p_0=1,
p_i=R_{x_i}p_{i-1}.
```

Assume maps

```text
d_p:X -> Y
```

satisfy, for `u=L_x(y)` and `v=R_y(x)`,

```text
d_p(u) = d_{R_x p}(y),                                      (RH1)
d_{R_u p}(v) = d_p(x) triangleright d_{R_x p}(y).           (RH2)
```

Then the corresponding label word

```text
D_n(x)=(d_{p_0}(x_1), d_{p_1}(x_2), ..., d_{p_{n-1}}(x_n))
```

is rack-equivariant.  If `(D_n,Gamma_n,J_n)` is injective for all `n`, the same
kernel containment follows.

## Fiber induction criterion

An inert observer can support induction only with an extra uniform fiber
control hypothesis.  Suppose `q_n:X^n -> O_n` is an inert observer and there is
a finite family of smaller finite YBE solutions

```text
Z_1,...,Z_m
```

such that for every `n` and every observer fiber `F`,

```text
intersection_j ker rho_n^{Z_j} <= ker(rho_n^X restricted to F).
```

If each `Z_j` is rack-dominated by induction, the product of the dominating
racks dominates `X`.  Product observers provide the stable fibers, but they do
not provide this fiber-kernel control.

## Sandwich obstruction

Minimal-ideal local groups do not automatically inherit the YBE product law.
For an idempotent `e` in the minimal ideal, YBE gives

```text
e L_u L_v e = e L_x L_y e,
```

but a naive local group label `ell_x=eL_xe` would need

```text
(eL_ue)(eL_ve) = (eL_xe)(eL_ye).
```

This inserts an extra `e` between the two factors.  In Rees-matrix terms, this
extra insertion changes the sandwich factor.  Product observers avoid this
failure only by staying in the original semigroup where `L_uL_v=L_xL_y` is
true; they do not by themselves repair it into rack labels.

The suffix parameter `t` in the maps `c_t` is precisely the kind of context
needed to carry the missing sandwich data.

## Final reduction

Product observers prove non-rigidity in the broad observer sense, but not rack
domination.  A Sawin-positive branch follows from either:

```text
1. fiber-kernel control by finitely many smaller solutions; or
2. product-Hurwitz separability via suffix-local maps c_t or d_p,
   plus all-arity injectivity with inert observers.
```

The next theoretical target is therefore not observer existence.  It is to
prove that residual rigid cores admit product-Hurwitz separability, or to find
a concrete structural obstruction to such suffix-local rack labels.

