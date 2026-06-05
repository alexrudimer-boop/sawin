# Uniform Reachable Rack Holonomy Boundary

Date: 2026-06-05

This note records the audit of reachable kernel-fiber holonomy.  The conclusion
is sharp:

```text
uniform reachable rack-valued holonomy separation
iff
finite endpoint-change cover
iff
direct finite contextual rack absorption.
```

Thus rack-valued holonomy is a correct Target A language, but it is not a
weaker input.  It is Target A itself, rewritten in terms of actual
kernel-fiber monodromy.

## Reachable Kernel-Fiber Holonomy

Let `X` be a finite bijective set-theoretic YBE solution and let

```text
kappa:X -> P_X
```

be the universal finite rack shadow.  For each `n`, the braid group `B_n` acts
on both `X^n` and `P_X^n`, and `kappa^n` is braid-equivariant.

For `p in P_X^n`, define the fiber

```text
F_p=(kappa^n)^{-1}(p).
```

The subgroup

```text
K_n(P_X)=ker rho_n^{P_X}
```

fixes every point of `P_X^n`, hence acts on each fiber `F_p`.

The reachable kernel-fiber holonomy groupoid has objects

```text
(n,p,a),  p in P_X^n, a in F_p,
```

and an arrow

```text
(n,p,a) -> (n,p,b)
```

is a braid `beta in K_n(P_X)` with

```text
b=beta a.
```

The endomorphism action on `F_p` is the monodromy representation

```text
mu_{n,p}:K_n(P_X) -> Sym(F_p).
```

A kernel-fiber bad pair is exactly a non-identity reachable holonomy arrow:

```text
a --beta--> beta a,
beta in K_n(P_X),
beta a != a.
```

Ambient holonomy not realized by an actual arrow inside some `X^n` fiber is
irrelevant to domination.

## Endpoint Displacement Cocycle

Fix a finite quotient

```text
theta:L_X -> M.
```

Set

```text
S_M=M x X x M.
```

For a word `w=(x_1,...,x_n)`, define the contextual endpoint symbol

```text
epsilon_i^M(w)=(a_i,x_i,b_i),
```

where

```text
a_i=theta(lambda_{x_1}...lambda_{x_{i-1}}),
b_i=theta(lambda_{x_{i+1}}...lambda_{x_n}).
```

For a holonomy arrow

```text
h=(a --beta--> beta a),
```

the `M`-endpoint displacement is

```text
Delta_M(h)=(epsilon^M(a),epsilon^M(beta a)).
```

Coordinatewise:

```text
Delta_{M,i}(h)=
(epsilon_i^M(a),epsilon_i^M(beta a)) in S_M x S_M.
```

This is exactly the endpoint-change data seen by finite contextual rack
detectors.

## Rack-Valued Endpoint Holonomy

For `s in S_M`, write

```text
delta_s=d_s=d_{a,x,b} in C_M(X).
```

A finite rack-valued endpoint detector is a finite rack `Y` and a map

```text
ell:S_M -> Y
```

satisfying the contextual rack crossing rule.  Equivalently, `ell` extends
uniquely to a rack homomorphism

```text
phi:C_M(X) -> Y
```

with

```text
phi(delta_s)=ell(s).
```

Using the right-rack convention `r_Y(s,t)=(t,s triangleright t)`, the
relations are: whenever `r_X(x,y)=(u,v)`,

```text
ell(a,u,lambda_v b)=ell(a lambda_x,y,b),

ell(a lambda_u,v,b)
=
ell(a,x,lambda_y b) triangleright ell(a lambda_x,y,b).
```

Therefore "rack-valued holonomy" in Target A means precisely:

```text
finite endpoint labels satisfying the defining relations of C_M(X).
```

It is not merely path bookkeeping.  It is exactly finite contextual rack
detection.

## Uniform Holonomy Separation Equals Target A

The uniform reachable rack-valued holonomy separation theorem says:

```text
There exist finitely many finite quotients M_j of L_X, finite racks Y_j, and
rack homomorphisms phi_j:C_{M_j}(X)->Y_j such that for every n, every
beta in K_n(P_X), and every a in X^n with beta a != a, there exist j and i
such that

phi_j(delta_{epsilon_i^{M_j}(a)})
!=
phi_j(delta_{epsilon_i^{M_j}(beta a)}).
```

This is equivalent to finite endpoint-change cover.

If such a finite family exists, then each `S_{M_j} x S_{M_j}` is finite, and
the endpoint pairs separated by `phi_j` give finitely many finite-rack
separable endpoint-change patterns covering all bad pairs.

Conversely, if finitely many finite-rack separable endpoint-change patterns
cover all bad pairs, choose one finite rack quotient separating each pattern.
Those quotients are a finite family of rack-valued reachable holonomy
detectors separating every actual nontrivial holonomy arrow.

Hence:

```text
uniform reachable rack-valued holonomy separation
iff
finite endpoint-change cover
iff
direct finite contextual rack absorption.
```

The holonomy formulation is useful because it keeps attention on actual
monodromy.  But it does not reduce the strength of Target A.

## Pointwise Holonomy Separation

For a fixed bad pair `(a,beta a)`, the following are equivalent:

```text
1. Some finite contextual rack detector separates (a,beta a).

2. There exist M, i, and endpoint symbols s,t in S_M such that
   epsilon_i^M(a)=s, epsilon_i^M(beta a)=t, and (M,s,t) is finite-rack
   separable.

3. There exist M, i, and a finite rack quotient phi:C_M(X)->Y with
   phi(delta_{epsilon_i^M(a)})
   !=
   phi(delta_{epsilon_i^M(beta a)}).
```

This is only pointwise separation.  It does not imply Target A.

Target A requires one finite product detector that separates every bad pair:

```text
exists D, for all bad pairs h, D separates h.
```

Pointwise separation gives only:

```text
for all bad pairs h, exists D_h separating h.
```

The gap is exactly the harmful ultrafilter obstruction.

## Harmful Ultrafilters In Holonomy Language

Let `B` be the set of actual nontrivial holonomy arrows:

```text
B={(n,a,beta): beta in K_n(P_X), beta a != a}.
```

For a finite detector `D`, let `S_D` be the set of arrows separated by `D`,
and let

```text
B_D=B \ S_D
```

be the set not separated by `D`.

Products satisfy

```text
S_{D_1 x D_2}=S_{D_1} union S_{D_2},
B_{D_1 x D_2}=B_{D_1} cap B_{D_2}.
```

If no finite detector separates all bad pairs, then the family `{B_D}` has the
finite intersection property.  Hence there is an ultrafilter `U` on actual
holonomy arrows such that

```text
B_D in U
```

for every finite detector `D`.

Fix `M`.  Let

```text
s equiv_M t
```

mean that every finite rack quotient of `C_M(X)` identifies `delta_s` and
`delta_t`.  Since `S_M` is finite, avoiding every finite-rack separable
endpoint-change cylinder implies that `U`-almost every bad arrow satisfies:

```text
for every coordinate i,
epsilon_i^M(a) equiv_M epsilon_i^M(beta a).
```

Thus a harmful ultrafilter is a profinite accumulation of actual nontrivial
monodromies for which every fixed finite rack-valued endpoint observation sees
all coordinate displacements as residual-rack invisible.

This is stronger than a coordinate drifting: for each fixed `M`, all
coordinates of `U`-typical bad arrows are invisible in `E_M`.

## Principal And Nonprincipal Obstructions

The strongest possible obstruction is principal:

```text
There exists one bad pair a --beta--> beta a such that for every finite M and
every coordinate i,

epsilon_i^M(a) equiv_M epsilon_i^M(beta a).
```

Then no finite contextual rack detector sees that bad pair.

The more flexible obstruction is nonprincipal: every individual bad pair may
be pointwise separable, but a sequence or filter of bad pairs escapes every
finite detector.  This is the actual uniformity failure Target A must exclude.

## Stabilizer Holonomy

There are two stabilizers.

The word stabilizer at `a` is

```text
Stab_X(a)={beta in K_n(P_X): beta a=a}.
```

Elements of `Stab_X(a)` are not bad at `a`; they already act trivially on that
point of `X^n`.

For a detector `D=(M,phi)`, the detector stabilizer is

```text
Stab_D(a)={
  beta in K_n(P_X):
  phi^n Theta_n^M(beta a)=phi^n Theta_n^M(a)
}.
```

A harmful bad pair lies in

```text
Stab_D(a) \ Stab_X(a)
```

for every detector in the harmful family.

If endpoint labels are equal under every finite rack-valued endpoint detector,
then endpoint rack detection cannot see the path holonomy.  Enriched path
labels help only if they become word-defined coordinate labels satisfying
rack relations.  If they remain path-dependent, they detect ambient holonomy
but do not separate endpoint words and do not imply kernel domination.

## Brunnian Towers

A Brunnian harmful tower consists of bad arrows

```text
a_m --beta_m--> beta_m a_m,
a_m in X^{n_m},
n_m -> infinity,
beta_m in K_{n_m}(P_X),
beta_m a_m != a_m,
```

such that:

```text
1. for every fixed finite M, eventually all coordinate endpoint changes are
   residual-rack invisible;
2. deleting any observer strand kills the monodromy or makes it
   detector-invisible;
3. the nontriviality depends on all n_m strands.
```

Local YBE identities enforce braid consistency on triples, but they do not
imply a deletion theorem saying that every nontrivial `K_n(P_X)`-monodromy has
a nontrivial bounded-substrand restriction.

The exact Target A theorem is therefore:

```text
No Brunnian harmful ultrafilter theorem.
There is no ultrafilter on actual kernel-fiber bad pairs such that, for every
finite quotient M of L_X, U-almost every pair satisfies

for all i,
epsilon_i^M(a) equiv_M epsilon_i^M(beta a).
```

Equivalently, every harmful ultrafilter contains a finite-rack separable
one-coordinate endpoint-change cylinder.

## Bounded-Support Generation

Since `P_X` is finite, `K_n(P_X)` has finite index in `B_n` for each fixed
`n`.  This does not give uniform finite generation over all arities.

A bounded-support route would need a theorem like:

```text
There exists N=N(X) and finitely many primitive kernel moves
gamma_j in K_{m_j}(P_X), m_j<=N, such that every actual nontrivial holonomy
arrow factors, after inserting observer strands and context-stable
conjugation, into primitive moves, and at least one primitive factor already
produces a finite-rack separable endpoint change.
```

Pure-braid and Brunnian complexity obstruct this route.  Even when abstract
generators are bounded in a braid group family, conjugating through observer
strands changes the contextual states

```text
a_i=lambda_{x_1}...lambda_{x_{i-1}},
b_i=lambda_{x_{i+1}}...lambda_{x_n}.
```

Thus bounded abstract generation does not automatically give bounded
contextual detector-visible generation.

## Target B Does Not Follow From Failure

If uniform rack-valued holonomy separation fails, the failure data is a
harmful ultrafilter of actual monodromies invisible to every finite
rack-valued endpoint detector.

This data is profinite and nonuniform.  It does not automatically produce
finite active data

```text
M, Z, r_Z:Z^2 -> Z^2, pi_{a,b}:X -> Z
```

with:

```text
|Z|<|X|,
r_Z total bijective YBE,
contextual compatibility,
braid equivariance,
global orbit-injectivity.
```

Therefore Target B still requires an independent construction.  Failure of
Target A can remain purely profinite and non-coordinatewise.

## Current Boundary

The strongest valid theorem is:

```text
For X, the following are equivalent:

1. one finite contextual rack detector separates every kernel-fiber bad pair;
2. finitely many finite-rack separable endpoint-change patterns cover all bad
   pairs;
3. finitely many rack-valued reachable holonomy detectors separate every
   actual nontrivial K_n(P_X)-holonomy arrow.
```

When these hold, the product detector gives a finite rack `P_X x Y` satisfying

```text
ker rho_n^{P_X x Y} <= ker rho_n^X
```

for every `n`.

The next theorem is not pointwise holonomy separation.  It is:

```text
No Brunnian Harmful Ultrafilter Theorem.
```

The obstruction is exact:

```text
actual nontrivial kernel-fiber holonomy may escape every fixed finite
rack-valued endpoint detector through Brunnian/profinite accumulation.
```

Ruling out that escape is precisely the remaining Target A problem.
