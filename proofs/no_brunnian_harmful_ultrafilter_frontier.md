# No Brunnian Harmful Ultrafilter Frontier

Date: 2026-06-05

This note records the sharpened Target A frontier after auditing the finite
endpoint-change cover theorem.  The one-coordinate endpoint-change formulation
is not merely a simplification: it is equivalent to direct finite contextual
rack absorption.

The next exact theorem is:

```text
No Brunnian harmful ultrafilter theorem.
Every harmful ultrafilter on actual kernel-fiber bad pairs contains some
finite-rack separable one-coordinate endpoint-change cylinder.
```

Equivalently, there is no harmful ultrafilter that makes every finite
coordinate endpoint change finite-rack invisible.

## Endpoint-Change Cover Equivalence

Let `B` be the set of kernel-fiber bad pairs

```text
(a,beta a),  a in X^n, beta in K_n(P_X), beta a != a.
```

For a finite quotient

```text
M of L_X,
```

define

```text
S_M=M x X x M.
```

For `s=(a,x,b) in S_M`, write

```text
delta_s=d_{a,x,b} in C_M(X).
```

For a word `w=(x_1,...,x_n)`, define

```text
epsilon_i^M(w)=(a_i,x_i,b_i),
```

where the contexts are computed in `M`:

```text
a_i=theta(lambda_{x_1}...lambda_{x_{i-1}}),
b_i=theta(lambda_{x_{i+1}}...lambda_{x_n}).
```

For an endpoint-change pattern `(M,s,t)`, define its bad-pair cylinder:

```text
C(M,s,t)={
  (a,beta a) in B :
  exists i, epsilon_i^M(a)=s, epsilon_i^M(beta a)=t
}.
```

The pattern is finite-rack separable if some finite rack quotient

```text
phi:C_M(X) -> Y
```

satisfies

```text
phi(delta_s) != phi(delta_t).
```

Then the following are equivalent:

```text
1. There exists one finite contextual rack detector separating every bad pair.

2. There exist finitely many finite-rack separable endpoint-change patterns
   (M_j,s_j,t_j) whose cylinders cover B.
```

If a detector

```text
D=(M,phi:C_M(X)->Y)
```

separates every bad pair, the finite set

```text
P_D={(M,s,t): s,t in S_M, phi(delta_s) != phi(delta_t)}
```

covers `B`: for every bad pair,

```text
Lambda_n^D(a) != Lambda_n^D(beta a)
```

means that some coordinate has distinct `Y`-labels.

Conversely, given a finite cover by patterns `(M_j,s_j,t_j)`, choose finite
rack quotients

```text
phi_j:C_{M_j}(X) -> Y_j
```

separating each `delta_{s_j}` from `delta_{t_j}`.  Let

```text
M=M_1 x ... x M_k.
```

Each projection `M -> M_j` induces a rack homomorphism

```text
C_M(X) -> C_{M_j}(X),
d_{a,x,b} -> d_{pr_j(a),x,pr_j(b)}.
```

The product of the pulled-back quotients separates every bad pair.

Thus:

```text
finite endpoint-change cover
iff
direct finite contextual rack absorption.
```

## No Multi-Coordinate Loophole

There is no case where a finite contextual rack detector separates a pair only
globally without a coordinate endpoint change.  It has the form

```text
Lambda_n^D=phi^n Theta_n^M:X^n -> Y^n.
```

Equality in `Y^n` is coordinatewise.  Therefore

```text
Lambda_n^D(a) != Lambda_n^D(b)
```

always gives some `i` with

```text
phi(delta_{epsilon_i^M(a)})
!=
phi(delta_{epsilon_i^M(b)}).
```

Multi-coordinate primitive cores are unnecessary for Target A.

## Harmful Ultrafilter Negation

The negation of the finite endpoint-change cover theorem is:

```text
For every finite family of finite-rack separable endpoint-change patterns,
there is a bad pair avoiding all of them.
```

Equivalently, there is an ultrafilter `U` on `B` such that

```text
C(M,s,t) notin U
```

for every finite-rack separable endpoint-change pattern `(M,s,t)`.

Fix finite `M`.  Since `S_M` is finite, there are finitely many endpoint pairs
`(s,t)`.  Let

```text
s equiv_M t
```

mean that every finite rack quotient of `C_M(X)` identifies `delta_s` and
`delta_t`.  Then `(M,s,t)` is finite-rack separable exactly when

```text
s not equiv_M t.
```

Since `U` avoids every separable cylinder, `U`-almost every bad pair satisfies

```text
for every coordinate i,
epsilon_i^M(a) equiv_M epsilon_i^M(beta a).
```

Equivalently,

```text
Pi_n^{E_M}(a)=Pi_n^{E_M}(beta a)
```

for `U`-almost every bad pair.

Thus a harmful ultrafilter says:

```text
for every finite context quotient M, all coordinate endpoint changes are
finite-rack invisible on an ultrafilter-large set of actual bad pairs.
```

The ultrafilter need not select one coordinate.  The arity may grow and the
changed coordinate may drift.  The statement is stronger in another direction:
for each fixed `M`, all coordinates of typical bad pairs are invisible in
`E_M`.

## Brunnian / Observer-Strand Obstruction

A natural obstruction to finite endpoint-change cover is a tower of bad pairs

```text
(a_n,beta_n a_n),  a_n in X^{m_n}, m_n -> infinity,
beta_n in K_{m_n}(P_X), beta_n a_n != a_n,
```

such that:

```text
1. for every fixed finite M, all coordinate endpoint changes are eventually
   equiv_M-invisible;
2. deleting any observer strand kills the monodromy or makes it finite-rack
   invisible;
3. the nontriviality depends essentially on all m_n strands.
```

This is a Brunnian harmful tower.

Local YBE identities do not formally rule it out.  Writing

```text
r_X(x,y)=(L_x(y),R_y(x)),
```

YBE gives triple identities such as

```text
L_{L_x(y)} L_{R_y(x)}(z)=L_x L_y(z),

R_{L_{R_y(x)}(z)}(L_x(y))
=
L_{R_{L_y(z)}(x)}(R_z(y)),

R_z R_y(x)=R_{R_z(y)} R_{L_y(z)}(x).
```

These ensure braid consistency on triples.  They do not give a global deletion
theorem for `K_n(P_X)`-monodromy, nor do they imply that every nontrivial
kernel action has a bounded-support subaction.

The exact missing theorem is:

```text
No Brunnian harmful ultrafilter theorem.
There is no ultrafilter on actual kernel-fiber bad pairs such that, for every
finite M, all coordinate endpoint changes are equiv_M-invisible on an
ultrafilter-large set.
```

Equivalently:

```text
Every harmful ultrafilter contains some finite-rack separable endpoint-change
cylinder.
```

## Bounded Arity And Braid Length

Bounded arity would assert that every bad pair has a finite-rack separable bad
core involving at most `N=N(X)` strands, with separation of the core forcing
separation of the original bad pair.

This is powerful but not justified.  `K_n(P_X)`-monodromy may use observer
strands, and deleting a strand can destroy the kernel condition or trivialize
the lift.

Bounded braid complexity would assert that every bad pair `(a,beta a)` admits
a detector-equivalent bad representative `(a,gamma a)` with

```text
gamma in K_n(P_X), |gamma| <= L(X).
```

This is also not justified.  For fixed `n`, finite images exist, but no
uniform Cayley-diameter bound is known over all `n`.  Pure braids, full
twists, Brunnian commutators, and observer-threading mechanisms can force
length growth.

Both bounded arity and bounded braid length are possible sufficient
mechanisms, but they are likely too strong as primary targets.

## Contextual Myhill-Nerode And Clopen Cores

A finite-index contextual Myhill-Nerode theorem would need a finite
equivalence relation on orbit-relevant contextual states, stable under braid
generators and context insertion, distinguishing all bad pairs, and realized
by a finite rack quotient.

For fixed `M`, the maximal rack-realizable endpoint quotient is `E_M`.  Any
rack-realizable endpoint quotient factors through it, and under the harmful
hypothesis it collapses actual bad pairs.

Thus any refinement beyond `E_M` must use extra path or holonomy state.  For
Target A, that extra state must still be finite-rack realizable.  With
rack-realizability, the statement reduces to finite endpoint-change cover.

Likewise, a context-stable clopen core theorem in the profinite endpoint
alphabet

```text
hat{S}=hat{L_X} x X x hat{L_X}
```

is exactly the finite endpoint-change cover theorem in topological language:
bad pairs must be covered by finitely many detector-separated clopen
endpoint-change cylinders.  Compactness does not prove this; if no finite
cover exists, there is a harmful ultrafilter avoiding every such cylinder.

## Uniform Reachable Holonomy Separation

A kernel-fiber bad pair is actual holonomy:

```text
a -> beta a
```

inside a fiber of

```text
X^n -> P_X^n.
```

A holonomy strategy would need:

```text
Every actual nontrivial K_n(P_X)-holonomy has a one-coordinate finite-rack
separable endpoint change, and finitely many finite rack-valued holonomy
detectors suffice uniformly for all bad pairs.
```

Pointwise holonomy separation is insufficient:

```text
for every bad pair, exists D separating it
```

does not imply

```text
exists D separating every bad pair.
```

Holonomy becomes Target A only if it gives finite rack-valued endpoint labels
satisfying contextual rack relations.  Otherwise it is diagnostic, or belongs
to Target B only after constructing a total bijective YBE target with kernel
reflection.

The missing theorem is:

```text
uniform reachable rack-valued holonomy separation.
```

## Structure Of K_n(P_X)

Since `P_X` is finite, `B_n` acts on the finite set `P_X^n`, so

```text
K_n(P_X)=ker rho_n^{P_X}
```

has finite index in `B_n` for each fixed `n`.

Finite index for each `n` does not give a uniform finite basis over all `n`.
A useful theorem would say that the sequence `K_n(P_X)` has a bounded-support,
Markov-stable, operadic generating family whose action on `X^n`-fibers is
detector-visible through finitely many endpoint-change patterns.

Pure braid phenomena show why this is hard.  Elements such as `A_{ij}` span
intervals of observer strands, Brunnian braids can be globally nontrivial
while all deletions are trivial, and full twists have length growing
quadratically in `n`.

The missing theorem would be:

```text
bounded-support generation of actual harmful K_n(P_X)-monodromy, compatible
with rack endpoint separation.
```

## Target A Failure Does Not Imply Target B

Failure of Target A yields a harmful ultrafilter `U` such that, for every
finite `M`, `U`-almost every bad pair satisfies

```text
for all i, epsilon_i^M(a) equiv_M epsilon_i^M(beta a).
```

This is profinite, nonuniform, and potentially non-coordinatewise.  It does
not automatically produce a finite active factor.

To obtain Target B one would need finite data

```text
M, Z, r_Z:Z^2 -> Z^2, pi_{a,b}:X -> Z
```

with `|Z|<|X|`, total bijective YBE, contextual compatibility, braid
equivariance, and global orbit-injectivity.  Failure of finite endpoint-change
cover supplies none of these finite objects.  It may remain purely profinite
and non-coordinatewise.

## Strongest Valid Theorem

The strongest valid theorem is conditional.

Branch A:

```text
finite endpoint-change cover
iff
direct finite contextual rack absorption.
```

If it holds, one finite detector separates all bad pairs, so `P_X x Y`
dominates `X`.

Branch B:

```text
if an independent finite active factor exists with |Z|<|X|, total bijective
YBE, contextual compatibility, and global orbit-injectivity, then
ker rho_n^Z <= ker rho_n^X.
```

The unconditional finite extraction dichotomy remains unproved.

## Best Next Sublemma

The most precise next Target A sublemma is:

```text
No Brunnian harmful ultrafilter theorem.
Every harmful ultrafilter on actual kernel-fiber bad pairs contains some
finite-rack separable one-coordinate endpoint-change cylinder.
```

Concrete finite form:

```text
There exist finitely many finite-rack separable endpoint-change patterns
(M_j,s_j,t_j) such that every kernel-fiber bad pair realizes one of them.
```

The most promising proof direction, if one exists, is:

```text
uniform reachable rack-valued holonomy separation.
```

It directly targets actual kernel-fiber monodromy.  It must be uniform and
rack-valued; pointwise or profinite holonomy is insufficient.

The project should pursue Target A in this order:

```text
1. No Brunnian harmful ultrafilter theorem;
2. uniform reachable rack-valued holonomy separation;
3. bounded-support generation of harmful K_n(P_X)-monodromy;
4. bounded arity and bounded braid length only as strong special cases.
```

The current obstruction is exact:

```text
a harmful ultrafilter may make every finite coordinate endpoint change
finite-rack invisible.
```

Ruling that out is precisely the remaining Target A theorem.
