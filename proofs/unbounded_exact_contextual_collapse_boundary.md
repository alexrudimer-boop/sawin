# Unbounded Exact Contextual Collapse Boundary

Date: 2026-06-05

This note records the boundary after formalizing reachable escape holonomy and
fixed-`M` endpoint detection.  For a fixed finite state quotient `M`, finite
rack detection is purely endpoint-label detection.  Hidden path holonomy is
diagnostic, but after endpoint labels are equal it is not seen by the finite
contextual rack detector.

The remaining obstruction is exactly:

```text
fixed-M exact contextual-label collisions in unbounded arity
```

or

```text
state-refinement escape through finer and finer quotients of L_X.
```

Equivalently, the contextual tower is blocked at unbounded exact
contextual-label collisions, not at fixed-`M` endpoint factorial holonomy.

## Reachable Escape Groupoid

Fix a finite quotient

```text
theta:L_X -> M.
```

For a word

```text
x=(x_1,...,x_n) in X^n,
```

define

```text
a_i(x)=theta(lambda_{x_1}...lambda_{x_{i-1}}),
b_i(x)=theta(lambda_{x_{i+1}}...lambda_{x_n}),

kappa_i^M(x)=d_{a_i(x),x_i,b_i(x)} in S_M.
```

The reachable escape groupoid `E_M(X)` has objects

```text
Ob E_M(X)=disjoint_union_n {(x,i): x in X^n, 1 <= i <= n}.
```

The object `(x,i)` is the word `x` with the `i`-th strand marked.  The endpoint
label map is

```text
ell_M(x,i)=kappa_i^M(x) in S_M.
```

Let `sigma_j` act on coordinates `j,j+1`.  If

```text
x_j=x, x_{j+1}=y, r_X(x,y)=(u,v),
```

then

```text
yword=rho_n^X(sigma_j)x
```

is obtained by replacing `(x,y)` with `(u,v)`.  The marked strand index changes
by the transposition `tau_j`.

There is a positive generating morphism

```text
e=(x,i;j,+):(x,i) -> (yword,tau_j(i)).
```

Let

```text
a=theta(lambda_{x_1}...lambda_{x_{j-1}}),
b=theta(lambda_{x_{j+2}}...lambda_{x_n}).
```

The two input labels around the crossing are

```text
P=d_{a,x,lambda_y b},
Q=d_{a lambda_x,y,b}.
```

The output labels are

```text
Q'=d_{a,u,lambda_v b},
P'=d_{a lambda_u,v,b}.
```

The defining relations of `C_M(X)` give

```text
Q'=Q,
P'=Q triangleright P.
```

With the convention that the associated group acts by

```text
g_Q.P = Q triangleright P,
```

define the cocycle on a positive edge by

```text
chi_M(e)=g_Q,  if i=j,
chi_M(e)=1,    if i != j.
```

Thus, when the marked strand is the left strand crossing through the right
strand, its label is acted on by `g_Q`; otherwise the endpoint label is
unchanged.  In every case,

```text
ell_M(target(e))=chi_M(e).ell_M(source(e)).
```

For every positive edge include an inverse edge with inverse cocycle.
Morphisms are finite paths, composition is concatenation, and

```text
chi_M(e_k...e_1)=chi_M(e_k)...chi_M(e_1).
```

This formalizes the difference between ambient holonomy in `As(C_M(X))` and
reachable holonomy from actual braid trajectories.  A transporter is relevant
only if it occurs as `chi_M(gamma)` for a path `gamma` in `E_M(X)`.

## Fixed-M Endpoint Lemma

Let

```text
S_M={d_{a,x,b}:a,b in M, x in X} subset C_M(X).
```

Assume every distinct pair in `S_M` is separated by some finite rack quotient
of `C_M(X)`.  Since `S_M` is finite, the product of those pair-separating
quotients gives one finite rack quotient

```text
phi_M:C_M(X) -> Y_M
```

which is injective on `S_M`.

For the detector

```text
D_M=(M,phi_M),
```

one has, for all `x,x' in X^n`,

```text
Lambda_n^{D_M}(x)=Lambda_n^{D_M}(x')
iff
Theta_n^M(x)=Theta_n^M(x')
```

as tuples in `S_M^n`.

Therefore, after endpoint separation of `S_M`, the fixed-`M` bad set is

```text
B_{D_M}={
  (x,x') in Omega_n :
  Theta_n^M(x)=Theta_n^M(x')
}.
```

Hidden stabilizer holonomy may exist along a braid path, but if endpoints are
identical then every finite contextual rack quotient of `C_M(X)` sees the same
endpoint labels.  The detector records endpoint elements, not the path or
stabilizer element.

Thus:

```text
For fixed M, hidden stabilizer holonomy is invisible to finite contextual rack
labels once endpoints are identical.
```

## Escape Mode I: Fixed-M Exact Collisions

After endpoint separation, fixed-`M` failure means:

```text
exists x != x' in X^n, x' in B_n.x,
Theta_n^M(x)=Theta_n^M(x').
```

Unbounded fixed-`M` failure means this happens in arbitrarily large arity.

Coarse examples are easy.  For a constant-action solution

```text
r(x,y)=(alpha(y),beta(x))
```

with commuting permutations, the quotient `M=1` can be so coarse that
relations identify many or all labels.  If `alpha` is transitive, then
`C_1(X)` identifies all `d_y`, so `Theta^1` is extremely coarse and exact
collisions can occur in arbitrarily large arity by padding.

This is not harmful by itself.  A finer `M` or another rack detector may still
separate the pairs.

Deletion and braid locality do not prove boundedness.  The label at coordinate
`i` is

```text
d_{a_i,x_i,b_i},
```

where the context states `a_i,b_i` depend on all letters to the left and right.
Deleting an observer changes these states, so an equality may disappear after
deletion.  A braid generator acts locally on letters, but the contextual labels
of those letters depend globally on the word.

The missing bounded statement would be:

```text
For fixed M, if exact Theta^M-collisions occur in some arity, then one occurs
in arity <= N(M,X).
```

No such theorem follows from the current ingredients.

## Escape Mode II: State-Refinement Escape

For each finite quotient `M`, define

```text
E_M subset (M x X x M)^2
```

by

```text
(a,x,b) E_M (a',x',b')
iff
d_{a,x,b}=d_{a',x',b'}
in C_M(X).
```

Let

```text
K=hat{L_X} x X x hat{L_X},
q_M:K -> M x X x M.
```

Define the profinite exact-context relation

```text
E_infty =
intersection_M (q_M x q_M)^(-1)(E_M)
subset K x K.
```

This is closed.  A harmful state-refinement ultrafilter produces limiting
contextual letter pairs lying in `E_infty`.

Pointwise separation says that any fixed concrete pair of contexts not truly
equal is separated by some finite quotient.  It does not imply `E_infty` is
determined by one finite quotient.

The finite-index condition needed is:

```text
exists M0 such that, on orbit-relevant contextual letters,
E_infty =
(q_M0 x q_M0)^(-1)(E_M0).
```

Equivalently, the contextual Myhill-Nerode relation has finite index.

Without this, compactness gives a closed profinite relation but no finite
detector.

## Harmful Constructions Still Missing

A genuine harmful construction would need one of two forms.

Type A: fixed-`M` exact collisions.

```text
There is one finite M such that exact Theta^M-collisions occur for same-orbit
distinct pairs in unbounded arity, and no finite rack quotient or refined
contextual detector separates the resulting ultrafilter.
```

Type B: state-refinement escape.

```text
For every finite M there are same-orbit pairs with exact Theta^M-collisions,
but the required separating quotient of L_X grows with the witness.
```

The current tower formalism does not rule out either type.  A construction
inside a finite YBE solution would be a serious obstruction to the route.

The mechanisms that could rule them out are:

```text
bounded harmful witnesses;
finite-index contextual Myhill-Nerode behavior;
uniform reachable holonomy separation;
active-factor extraction from unbounded contextual collapse.
```

## Active-Factor Extraction

Suppose one tries to extract a finite active factor from contextual collapse.
Let `M` be finite, `Z` finite, and let

```text
pi_{a,b}:X -> Z
```

be maps.  For `r_X(x,y)=(u,v)`, define `Gamma subset Z^2 x Z^2` by

```text
A=pi_{a,lambda_y b}(x),
B=pi_{a lambda_x,b}(y),
C=pi_{a,lambda_v b}(u),
D=pi_{a lambda_u,b}(v),
```

and `(A,B) Gamma (C,D)`.

This gives a finite active YBE solution only if:

```text
1. functionality: each input has at most one output;
2. totality: every pair in Z^2 occurs as input;
3. cofunctionality/bijectivity: r_Z is bijective;
4. YBE: r_Z satisfies YBE on all triples in Z^3;
5. braid equivariance: Pi_n(rho^X(beta)x)=rho^Z(beta)Pi_n(x);
6. kernel reflection: ker rho_n^Z <= ker rho_n^X for all n.
```

Fixed-`M` exact collisions do not automatically yield such a `Z`.  The naive
quotient of `S_M` may be partial on `Z^2`, may fail functionality, and may fail
YBE on unreached triples.

State-refinement escape gives a profinite active pre-factor unless the
relation factors through one finite quotient.

Hidden path holonomy lives in stabilizer cosets.  To turn it into finite
`Z`-data, the holonomy cocycle must have finite image modulo stabilizers.  If
it has factorial/profinite accumulation, finite `Z` sees only finite-period
shadows and loses the holonomy.

## Product And Padding

If

```text
X={*} x Z,
```

then `X` is isomorphic to `Z`; one-point free-quandle holonomy adds no active
component.

If

```text
X=E_triv x Z
```

and `E_triv` has trivial braid action, then

```text
rho_n^X = id x rho_n^Z,
ker rho_n^X = ker rho_n^Z.
```

Thus projection to `Z` is domination-equivalent.  If `E_triv` is nontrivial,
then `Z` is a proper domination-equivalent active factor, so such padding does
not survive residual-rigid reduction.

If both product factors are rack-dominated, their rack product dominates the
product solution.  Product padding does not create a residual-rigid harmful
obstruction once the factors are solved.

## Escape Holonomy After Endpoint Reduction

The escape groupoid separates:

```text
ambient holonomy in As(C_M(X))
```

from

```text
reachable holonomy from actual braid trajectories.
```

For fixed `M`, endpoint labels lie in finite `S_M`.  Any reachable transporter
family from `r in S_M` has endpoints in `S_M`; on an ultrafilter-large subset
the endpoint is constant.

If the endpoint `s` differs from `r` and `r,s` are finite-rack separated, one
finite quotient separates all such transporters from acting like stabilizers.
If `s=r`, the family is stabilizer holonomy and is invisible to endpoint
labels.

Thus fixed-`M` escape holonomy is harmful only if it supports exact endpoint
label collisions.  It is not an additional endpoint obstruction after `S_M` is
separated.

The unresolved case is profinite holonomy coupled with exact contextual-label
collisions or state-refinement escape.

## Strongest Valid Theorems

Endpoint reduction:

```text
If S_M is separated by one finite rack quotient, then a fixed-M same-orbit pair
is bad iff it has identical Theta_n^M label tuple.
```

Bounded fixed-`M` exact witnesses imply a finite detector by taking products
over all witnesses up to the bound.

Finite-index contextual Myhill-Nerode behavior implies a finite detector once
the relevant finite `S_M` is endpoint-separated and `Theta^M` is orbit-faithful.

Finite active extraction from harmful escape implies residual-rigid Sawin: if
every harmful ultrafilter arising from fixed-`M` exact collisions,
state-refinement escape, or hidden reachable holonomy is either finite-rack
absorbed or yields a proper finite active factor with

```text
ker rho_n^Z <= ker rho_n^X,
```

then residual rigidity excludes the active-factor branch and a finite detector
must exist.

## Current Missing Lemma

The fixed-`M` endpoint problem is settled:

```text
finite S_M + pointwise rack separation
=> one rack quotient injective on S_M.
```

After that, fixed-`M` badness is exact equality of `Theta_n^M` tuples.  Hidden
stabilizer holonomy gives no additional finite rack detection power at fixed
`M`.

The sharp missing lemma is:

```text
Every harmful unbounded exact contextual collapse is either finite-index /
rack-absorbed or finite-active-factor extractable.
```

Equivalently, one must prove one of:

```text
bounded harmful witnesses;
finite-index contextual Myhill-Nerode behavior;
uniform reachable escape-holonomy separation;
active-factor extraction from profinite contextual collapse.
```

Without one of these, the contextual tower remains blocked precisely at
unbounded exact contextual-label collisions.
