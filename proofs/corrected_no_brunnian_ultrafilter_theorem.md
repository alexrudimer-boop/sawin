# Corrected No Brunnian Ultrafilter Theorem

Date: 2026-06-05

This note records the quantifier correction to the No Brunnian Harmful
Ultrafilter formulation.

The theorem is exactly Target A only if "one-coordinate endpoint-change
cylinder" means an arity-relative existential coordinate event:

```text
there exists i with 1 <= i <= n(b)
```

inside the bad pair.  It must not mean a fixed absolute coordinate `i`.

## Correct Visibility Sets

Let `B` be the set of witnessed kernel-fiber bad triples

```text
b=(n,a,beta),
a in X^n,
beta in K_n(P_X),
beta a != a.
```

The witnessed version is useful because deletion, support, and Brunnian
arguments depend on the braid `beta`, not only on the endpoint pair
`(a,beta a)`.

For a finite quotient

```text
M of L_X,
```

write

```text
S_M=M x X x M.
```

For a word `w=(x_1,...,x_n)`, define

```text
epsilon_i^M(w)=(a_i,x_i,b_i),
```

where the prefix and suffix products are computed in `M`.

For `s,t in S_M`, write

```text
s equiv_M t
```

if every finite rack quotient of `C_M(X)` identifies `d_s` and `d_t`.

The correct `M`-visible bad-pair set is

```text
D_M={
  (n,a,beta) in B :
  beta a != a and
  exists 1 <= i <= n with
  epsilon_i^M(a) not equiv_M epsilon_i^M(beta a)
}.
```

Its complement is

```text
H_M=B \ D_M.
```

Thus `H_M` consists of bad triples for which every coordinate endpoint
displacement is residual-rack invisible at level `M`:

```text
for all i <= n,
epsilon_i^M(a) equiv_M epsilon_i^M(beta a).
```

## Harmful Ultrafilter

A harmful ultrafilter is an ultrafilter `U` on actual bad triples satisfying

```text
H_M in U
```

for every finite quotient `M` of `L_X`.

Equivalently:

```text
for every finite M,
U-almost every bad triple is M-invisible in all coordinates.
```

The quantifier order is:

```text
for all finite M,
  U-almost every b=(n,a,beta),
    for all i <= n(b),
      epsilon_i^M(a) equiv_M epsilon_i^M(beta a).
```

It is not:

```text
U-almost every b,
  for all finite M,
    for all i <= n(b), ...
```

and it is not a statement about a fixed absolute coordinate.

## Equivalence With Finite Endpoint-Change Cover

The corrected no-harmful-ultrafilter theorem is:

```text
There is no ultrafilter U on B with H_M in U for every finite quotient M.
```

This is equivalent to a finite cover by the `D_M`.

If no finite family of the `D_M` covers `B`, then the complements `H_M` have
the finite intersection property.  By the ultrafilter lemma, they extend to an
ultrafilter `U` with

```text
H_M in U
```

for every finite `M`.

Conversely, if such an ultrafilter exists, no finite family can cover `B`.
Indeed, if

```text
B=D_{M_1} union ... union D_{M_r},
```

then

```text
empty = H_{M_1} cap ... cap H_{M_r}
```

would lie in `U`, impossible.

Therefore:

```text
no harmful ultrafilter
iff
exists finite M_1,...,M_r with
B=D_{M_1} union ... union D_{M_r}.
```

## Product Refinement To One Quotient

Visibility is monotone under context refinement.

If `M' -> M` is a quotient map from a finer finite quotient of `L_X`, then
there is an induced rack homomorphism

```text
C_{M'}(X) -> C_M(X),
d_{(p,x,q)} -> d_{(bar p,x,bar q)}.
```

Thus:

```text
D_M subset D_{M'}.
```

A finite family `M_1,...,M_r` is refined by the product quotient `M_*` of
`L_X` mapping to each `M_j`.  Hence:

```text
D_{M_1} union ... union D_{M_r} subset D_{M_*}.
```

So finite endpoint-change cover is equivalent to:

```text
exists one finite quotient M_* of L_X such that B=D_{M_*}.
```

For fixed `M`, the finite relation `not equiv_M` is represented by one finite
rack quotient of `C_M(X)`: because `S_M` is finite, take the product over all
pairs `s,t` with `s not equiv_M t` of finite rack quotients separating
`d_s,d_t`.

Therefore the corrected no-harmful-ultrafilter theorem is equivalent to direct
finite contextual rack absorption.

## Fixed-Coordinate Trap

For a fixed absolute coordinate `j`, define

```text
C_{M,j}={
  b=(n,a,beta) in B :
  n >= j and
  epsilon_j^M(a) not equiv_M epsilon_j^M(beta a)
}.
```

Then

```text
D_M=union_{j>=1} C_{M,j}.
```

An ultrafilter can contain `D_M` without containing any fixed `C_{M,j}`,
because ultrafilters are closed under finite unions, not countable unions.

Thus a fixed-coordinate formulation is stronger than Target A and can be
defeated by padding or arity escape.  The correct cylinder is the existential
coordinate event `D_M`, or else one must pass to a marked-coordinate bad-pair
space

```text
tilde B={(b,i): b in B_n, 1 <= i <= n}.
```

Without marking, there is no globally distinguished coordinate.

## What Local YBE Gives

Write

```text
r(x,y)=(L_x(y),R_y(x)).
```

The local YBE identities are:

```text
L_{L_x(y)}(L_{R_y(x)}(z))=L_x(L_y(z)),

R_{L_{R_y(x)}(z)}(L_x(y))
=
L_{R_{L_y(z)}(x)}(R_z(y)),

R_z(R_y(x))
=
R_{R_z(y)}(R_{L_y(z)}(x)).
```

Together with bijectivity of `r`, these identities give the braid action on
`X^n`.

They also make the contextual rack relations braid-compatible.  If

```text
r(x,y)=(x',y'),
```

then, with the rack convention `r_Q(u,v)=(u triangleright v,u)`, the local
contextual relations are:

```text
d_{(p,x',y'q)}
=
d_{(p,x,yq)} triangleright d_{(px,y,q)},

d_{(px',y',q)}
=
d_{(p,x,yq)}.
```

The monoid relation `xy=x'y'` in `L_X` ensures total context is preserved:

```text
p x y q = p x' y' q.
```

Thus local YBE proves:

```text
contextual endpoint transport is a well-defined rack-valued braid cocycle.
```

It proves that finite rack quotients of `C_M(X)` are legitimate detectors.
It does not prove that every nontrivial `K_n(P_X)`-monodromy is seen by one.

The missing implication is:

```text
beta in K_n(P_X), beta a != a
implies
exists finite M and i <= n with
epsilon_i^M(a) not equiv_M epsilon_i^M(beta a).
```

The uniform Target A version is:

```text
exists finite M_* such that for every bad triple (n,a,beta),
exists i <= n with
epsilon_i^{M_*}(a) not equiv_{M_*} epsilon_i^{M_*}(beta a).
```

This is a global endpoint-faithfulness principle, not a local YBE identity.

## Deletion, Contraction, And Brunnian Escape

Deleting observer strands is not dynamically neutral.  A retained strand may
cross a deleted strand before deletion.  That crossing can apply a nontrivial
operation to the retained color.  Hence:

```text
delete after acting != act after deleting
```

in general.

Contextual endpoints are a controlled contraction of observer strands:

```text
epsilon_i^M(w)=(finite left context, active letter, finite right context).
```

Harmfulness says that every such finite contraction collapses:

```text
for every finite M,
for U-almost every bad triple,
all coordinates are M-invisible.
```

A bad triple is `M`-Brunnian in the endpoint sense if it is nontrivial but
lies in `H_M`.  A harmful ultrafilter is a coherent profinite tower of such
bad triples at every fixed finite level.

The obstruction is:

```text
nontriviality may live only in the simultaneous presence of all observer
strands.
```

Deleting or finitely contracting observers can destroy the branch data that
made the monodromy nontrivial.

## Minimality And Arity Escape

If a harmful ultrafilter concentrates on a fixed arity `N`, then since `X^N`
is finite, it becomes principal at the level of endpoint pairs after passing
to a finite set.  This would give a single fixed-arity bad pair invisible to
all finite endpoint detectors.

Therefore, if pointwise endpoint detection holds in every fixed arity, any
harmful ultrafilter must satisfy:

```text
{b in B : n(b)>N} in U
```

for every standard `N`.

The same applies to any bounded active-support notion.  Minimal-support
arguments work only if one has an extraction theorem:

```text
nontrivial bad pair
implies
nontrivial smaller bad pair after deleting or contracting passive strands.
```

That extraction is not formal for general bijective YBE solutions.  Observer
strands can carry branch-choice data, so harmfulness may evade all finite
minimality arguments by arity escape.

## Profinite Limit View

The profinite context space is

```text
hat S=hat{L_X} x X x hat{L_X}.
```

Each finite `M` gives a clopen relation `R_M` on `hat S`:

```text
(s,t) in R_M
iff
s_M equiv_M t_M.
```

The limiting invisibility relation is

```text
R_infty=intersection_M R_M.
```

This relation is closed, but need not be clopen.  It is clopen only if some
finite quotient `M_0` already determines all later residual rack
identifications:

```text
R_infty=R_{M_0}.
```

Compactness does not produce such finite-index stabilization.  The bad-pair
space is a disjoint union over unbounded arities and carries braid witnesses;
it is not a compact finite-dimensional profinite space on which an ordinary
finite-subcover argument applies.

A harmful ultrafilter is exactly a drifting profinite limit: the detector
level required to see the monodromy can escape with arity, support, or braid
complexity.

## Special Branches

In rack solutions, take `Y=X`; there are no bad pairs relative to the rack
shadow `P_X=X`.

In involutive/symmetric solutions, the braid action factors through the
symmetric group, so pure braid monodromy vanishes.  This proves the
domination statement in that branch but does not address genuine braid
monodromy.

In left-nondegenerate branches, derived-rack or guitar-map machinery gives
enough branch recoverability to compare the YBE action with rack action.  This
is a special positive mechanism and does not extend to arbitrary bijective
solutions, because global bijectivity of `r:X^2->X^2` need not make the
individual maps `L_x` and `R_y` bijective.

In constant-action or permutation branches, the braid action reduces to finite
permutation/exponent data, so Brunnian branch choice collapses to finite state.

Product and padding branches are harmless only when an independent
active-factor or componentwise domination argument removes the padding.  They
also illustrate why fixed-coordinate formulations are wrong: visible changes
can be shifted to arbitrarily large coordinates.

## Sharp Valid Theorem

Let `X` be a finite bijective set-theoretic YBE solution and let `B` be the
set of actual kernel-fiber bad triples.  For each finite quotient `M` of
`L_X`, define `D_M` as above.

Then the following are equivalent:

```text
1. finite endpoint-change cover;
2. direct finite contextual rack absorption;
3. uniform reachable rack-valued holonomy separation;
4. there is no ultrafilter U with B\D_M in U for every finite M;
5. there exists one finite quotient M_* of L_X with B=D_{M_*}.
```

For fixed `M`, visibility by `not equiv_M` is represented by one finite rack
quotient of `C_M(X)`.

The theorem follows from:

```text
- the ultrafilter finite-cover duality for (1) and (4);
- product refinement of finite quotients for (1) and (5);
- finiteness of S_M for representing not equiv_M by one finite rack quotient;
- the previous coordinatewise equivalence of endpoint-change cover,
  contextual rack absorption, and rack-valued holonomy separation.
```

## Current Boundary

Local YBE identities prove that contextual endpoint detectors are legitimate.
They do not prove that nontrivial shadow-fiber monodromy is endpoint-visible.

The missing global principle is:

```text
Nontrivial K_n(P_X)-monodromy on X^n forces a finite-rack-separable
contextual endpoint change.
```

Uniformly over all arities, this is the corrected No Brunnian Harmful
Ultrafilter Theorem.

Any strategy that deletes or contracts observers until a smaller active bad
pair remains requires an independent active-extraction theorem.  That belongs
to Target B and cannot be assumed without constructing finite coordinatewise
YBE data with orbit-injectivity.

Thus:

```text
Target A is exactly the corrected No Brunnian Harmful Ultrafilter Theorem.
```

It is not currently forced by local YBE or residual endpoint machinery.  The
precise missing input is the global exclusion of profinitely
endpoint-invisible Brunnian shadow-fiber monodromy.
