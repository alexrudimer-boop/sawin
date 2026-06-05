# Normalized Prefix Profinite Barrier

Date: 2026-06-05

This note records the correction after the profinite stabilizer-separation
audit.  The profinite criterion is correct, but the prefix rack `V_L(X)` is
not a full prefix-arrow rack.  Relation `(VL1)` collapses the label `(p,x)` to
the evaluated label `(1,p(x))`.  The residual branch therefore has two
separate barriers:

```text
normalized-prefix orbit faithfulness;
profinite stabilizer separability in As(W_L(X)).
```

## Profinite Criterion Status

For any finitely generated rack `R`, let

```text
G=As(R)=< e_a, a in R | e_{b triangleright a}=e_b e_a e_b^{-1} >.
```

The group `G` acts on `R` by rack translations.  For `a in R`, let

```text
H_a=Stab_G(a).
```

Define finite-rack residual equivalence by

```text
a ==_fin b
```

if every homomorphism from `R` to a finite rack identifies `a` and `b`.

If `a` and `b` lie in different `G`-orbits, then they are separated by the
finite trivial rack of `G`-orbits.  A finitely generated rack has finitely many
inner orbits, since every element lies in the orbit of one of the finitely many
generators.

If `b=g.a`, then

```text
a ==_fin b
iff
g in closure_prof(H_a)
iff
g in intersection_{N normal finite index in G} H_a N.
```

No residual finiteness of `G` is required.  The converse separation direction
uses the finite augmented rack

```text
Q_N = disjoint union_j G/(H_j N),
```

where `a_j` are orbit representatives and `H_j=Stab_G(a_j)`.

Thus finite-rack residual collapse is exactly a stabilizer-coset separability
question.

## Collapse Through Evaluation

Let

```text
S=S_L^1.
```

The prefix vertex rack `V_L(X)` has generators

```text
a_{p,x}        (p in S, x in X)
```

and relations, for `r_X(x,y)=(u,v)`,

```text
a_{p,u} = a_{pL_x,y},                              (VL1)
a_{pL_u,v} = a_{pL_x,y} triangleright a_{p,x}.     (VL2)
```

Because `u=L_x(y)`, relation `(VL1)` gives

```text
a_{qL_z,x} = a_{q,L_z(x)}
```

for all `q,z,x`.  If

```text
p=L_{z_1}...L_{z_k},
```

then iterating `(VL1)` yields

```text
a_{p,x}=a_{1,p(x)}.
```

Therefore `V_L(X)` is isomorphic to the normalized prefix rack `W_L(X)` with
generators

```text
b_z        (z in X)
```

and relations

```text
b_{pL_u(v)} = b_{p(u)} triangleright b_{p(x)}
```

for every `p in S`, `x,y in X`, and `r_X(x,y)=(u,v)`.

The isomorphism sends

```text
a_{p,x} -> b_{p(x)}.
```

Consequently,

```text
(p,x) ==_fin (q,y) in V_L(X)
iff
p(x) ==_fin q(y) in W_L(X).
```

## Normalized Prefix Map

Define

```text
D_n:X^n -> X^n
```

by

```text
D_n(x_1,...,x_n)
 =
(x_1,
  L_{x_1}(x_2),
  L_{x_1}L_{x_2}(x_3),
  ...,
  L_{x_1}...L_{x_{n-1}}(x_n)).
```

Every prefix vertexization through `V_L(X)` factors through `D_n`.  Thus if
there are distinct words `w,w'` in the same braid orbit with

```text
D_n(w)=D_n(w'),
```

then no finite quotient of `V_L(X)` can separate them, even before any
profinite issue appears.

This is the finite/evaluative obstruction.

## Associated Group Of The Collapsed Rack

Let

```text
G_L(X)=As(W_L(X)).
```

It has finite Wirtinger-type presentation

```text
G_L(X)
= < g_z, z in X
    | g_{pL_u(v)} = g_{p(u)} g_{p(x)} g_{p(u)}^{-1} >,
```

where `p in S` and `r_X(x,y)=(u,v)`.

For `z in X`, let

```text
H_z=Stab_{G_L(X)}(b_z).
```

If two normalized labels `b_z` and `b_{z'}` lie in the same `G_L(X)`-orbit and
`b_{z'}=g.b_z`, then

```text
z ==_fin z'
iff
g in closure_prof(H_z).
```

Thus the profinite obstruction is an orbit-relevant coset

```text
g notin H_z
but
g in closure_prof(H_z).
```

## Correct Residual Branch

For a residual rigid `X` with no proper domination-reducing active factor, the
current route would need both:

```text
1. normalized-prefix orbit faithfulness:
   if w != w' lie in the same B_n-orbit, then D_n(w) and D_n(w') differ in a
   coordinate that remains distinct in W_L(X);

2. profinite stabilizer separation:
   every orbit-relevant stabilizer H_z <= G_L(X) is profinitely closed on the
   cosets needed to separate those normalized labels.
```

Equivalently, there must be no bad tuple `n,w,beta` with

```text
w' = rho_n^X(beta)w != w
```

such that every coordinate of `D_n(w)` and `D_n(w')` is finite-rack
indistinguishable in `W_L(X)`.

## Finite Closure Is Still Insufficient

Finite closure rules from the rack presentation detect ordinary equality in
`W_L(X)`, corresponding to membership in the actual stabilizer `H_z`.

Finite-rack residual equivalence detects membership in

```text
closure_prof(H_z).
```

The gap

```text
closure_prof(H_z) \ H_z
```

cannot be computed by a finite semigroup closure on `S x X` unless one adds a
profinite separability oracle.

## Active Factors Are Not Automatic

A nonclosed stabilizer coset in `W_L(X)` gives an identification of normalized
prefix labels

```text
p(x) ==_fin q(y).
```

It does not give a coordinate map

```text
pi:X -> Z
```

or a YBE congruence on `X`.  Inside a single braid orbit, inert observers are
constant, so an inert complement cannot repair failure of active-coordinate
separation.

A prefix-dependent collapse can yield a domination-reducing active factor only
if it can be promoted to a coherent finite state-dependent solution quotient,
for example maps

```text
pi_p:X -> Z
```

such that

```text
r_Z(pi_p(x),pi_{pL_x}(y)) = (pi_p(u),pi_{pL_u}(v))
```

for every `p` and `r_X(x,y)=(u,v)`.  This is extra structure and is not forced
by a nonclosed stabilizer coset.

## Rees Sandwich Data

The full prefix path groupoid with arrows

```text
p --x--> pL_x
```

does retain Rees row, column, and sandwich data.  If a minimal ideal has Rees
matrix form

```text
M(G_0;I_0,Lambda;P)
```

and `p=(i,g,lambda)`, then right multiplication by
`L_x=(i_x,g_x,lambda_x)` gives

```text
pL_x=(i, g P_{lambda i_x} g_x, lambda_x),
```

so the arrow remembers the source column `lambda`, the row `i_x`, and the
sandwich entry `P_{lambda i_x}`.

But `V_L(X)` imposes

```text
a_{pL_x,y}=a_{p,L_x(y)},
```

and hence collapses the arrow label to `p(L_x(y))`.  Therefore `V_L(X)` does
not retain the full prefix Rees data.  It retains only the evaluated
normalized label.

There are now two possible losses:

```text
finite/evaluative loss:
    p(x)=q(y) forces a_{p,x}=a_{q,y};

profinite/rackification loss:
    p(x) != q(y), but b_{p(x)} and b_{q(y)} are identified in every finite
    rack quotient because a stabilizer coset is not closed.
```

## Sufficient Criteria

One sufficient theorem is:

```text
If W_L(X) has finite rack quotients separating all distinct generator images
that occur in normalized braid-orbit comparisons, and D_n is orbit-faithful
modulo equality in W_L(X), then X is rack-dominated.
```

Since `X` is finite, one finite product of separating quotients separates all
relevant generator pairs.  With the orbit observer added, the prefix-path
vertexization theorem applies.

A stronger finite certificate is a finite quotient

```text
phi:G_L(X) -> Gbar
```

whose induced finite coset rack separates all needed normalized prefix labels.

An even stronger practical certificate is a finite rack `Y` and a map

```text
varphi:X -> Y
```

such that, for all `p` and `r_X(x,y)=(u,v)`,

```text
varphi(pL_u(v)) = varphi(p(u)) triangleright varphi(p(x)),
```

and the labelled normalized prefix words separate braid-orbit points.

## Current Endpoint

The profinite stabilizer route does not currently finish Sawin.  The residual
branch now requires a theorem proving, for residual rigid cores with no proper
domination-reducing active factor:

```text
normalized-prefix orbit faithfulness
and
profinite stabilizer separability in As(W_L(X)).
```

Or else one must replace `V_L(X)` with a genuine full-arrow detector that
retains prefix holonomy data while still producing a finite rack whose braid
kernel is contained in the braid kernel of `X`.

