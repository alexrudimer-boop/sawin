# Residual-Rigid Harmful Collapse Exclusion

Date: 2026-06-05

This note records the audit of the Proper Contextual Dichotomy.  The dichotomy
is not a formal consequence of the current contextual machinery.  It is a
structured sufficient theorem for Sawin, and if proved it would imply Sawin by
induction, but it asks for extra data not contained in the statement of Sawin.

After residual endpoint extraction is ruled out, the contextual route has only
two coherent exits:

```text
direct finite rack absorption
```

or

```text
a genuinely independent proper active factor not induced by finite rack
quotients of C_M(X).
```

The second branch is now best regarded as an added extraction theorem, not
something forced by harmful contextual collapse.  The exact missing theorem is:

```text
residual-rigid harmful collapse exclusion.
```

It would say that a finite YBE solution cannot simultaneously have harmful
profinite contextual collapse, no finite rack absorption, and no independent
proper active factor.

## Proper Contextual Dichotomy Audit

The Proper Contextual Dichotomy says that every finite bijective YBE solution
`X` admits at least one of:

```text
1. finite contextual rack absorption;
2. a strictly smaller finite YBE solution Z with contextual maps
   pi_{a,b}:X -> Z whose induced maps Pi_n:X^n -> Z^n are braid-equivariant
   and globally orbit-injective.
```

This is not literally equivalent to Sawin's theorem.  Sawin asks only for a
finite rack `Y` with

```text
ker rho_n^Y <= ker rho_n^X
```

for every `n`.  It does not ask for:

```text
a contextual detector C_M(X) -> Y,
a strict descent X -> Z with |Z|<|X|,
coordinatewise orbit-injective maps Pi_n:X^n -> Z^n.
```

Thus the dichotomy is a structured sufficient theorem rather than a restatement.

However, as a proof strategy it is almost as strong as Sawin.  If the
dichotomy holds, Sawin follows by induction on `|X|`.  Conversely, a minimal
counterexample to Sawin would automatically violate the dichotomy.  The extra
structure requested is exactly:

```text
uniform finite contextual rack visibility
```

or

```text
strict orbit-injective YBE descent.
```

Neither is supplied by compactness, residual endpoint quotients, or ordinary
finite-state arguments.

## Direct Finite Rack Absorption

Let `D` range over finite contextual rack detectors, and let

```text
B_D={
  (n,beta,a):
  beta in K_n(P_X),
  beta a != a,
  Lambda_n^D(beta a)=Lambda_n^D(a)
}
```

be the bad pairs not separated by `D`.

If `D_1,D_2` are detectors, their product satisfies

```text
B_{D_1 x D_2}=B_{D_1} cap B_{D_2}.
```

Therefore finite rack absorption is exactly:

```text
exists D,  B_D=empty.
```

If no finite detector separates all bad pairs, then all `B_D` are nonempty and
the family `{B_D}` has the finite intersection property.  Hence there is a
harmful ultrafilter `U` containing every `B_D`.

A direct finite rack absorption theorem must prove a YBE-specific boundedness
principle, for example:

```text
bounded arity reduction,
bounded braid-complexity reduction,
finite-index YBE Myhill-Nerode,
context-stable clopen core cover.
```

None follows formally.  If a clopen core `C` is separated by a detector `D`,
then

```text
C cap B_D=empty
```

in the appropriate occurrence sense, so `C` is not contained in a harmful
ultrafilter containing `B_D`.  Thus a harmful ultrafilter can avoid every
already detector-separated finite clopen core unless a new YBE-specific
finite-cover theorem is proved.

Branch I is therefore not obtained from compactness, WQO, profinite
compactness, Stone duality, or ordinary automata theory.

## Independent Active Extraction

Under the no-detector hypothesis, an active factor cannot factor through the
fixed-`M` residual endpoint quotient `E_M`.

Recall that for fixed finite `M`,

```text
S_M=M x X x M,
```

and

```text
s equiv_M t
```

if every finite rack quotient of `C_M(X)` identifies `delta_s` and `delta_t`.
Let

```text
E_M=S_M/equiv_M.
```

One finite rack quotient

```text
Phi_M:C_M(X) -> Y_M
```

realizes `E_M` on endpoint generators.

Under no finite detector, even the strongest fixed-`M` detector fails.  Hence
for every finite `M`, there is an actual bad pair

```text
beta a != a,
beta a in B_n.a,
Pi_n^{E_M}(beta a)=Pi_n^{E_M}(a).
```

Every map factoring through `E_M` also collapses this pair.  Therefore an
active factor

```text
pi_{a,b}:X -> Z
```

can avoid the obstruction only if, for some `M`, it separates endpoint symbols
`s,t in S_M` with

```text
s equiv_M t
```

but

```text
pi(s) != pi(t).
```

Such a factor separates finite-rack-invisible endpoint pairs.  It is not
induced by any finite rack quotient of `C_M(X)`.

Possible sources of such information are:

```text
reachable path or holonomy data,
inert observer data,
non-endpoint finite states,
finite quotients of escape groupoids,
direct algebraic quotients of X.
```

Each source has the same trichotomy:

```text
if it satisfies rack relations, it is a finite rack detector;
if it satisfies total bijective YBE and orbit-injectivity, it is an active
factor;
otherwise it is diagnostic or bookkeeping data and gives no kernel inclusion.
```

## Hidden Reachable Holonomy

Hidden holonomy can supply missing information only if it becomes either a
finite rack detector or a finite active factor.

Suppose finite holonomy data gives labels

```text
pi_{a,b}:X -> Z.
```

To be an active factor, the following must hold.

First, the labels must be uniformly well-defined: `pi_{a,b}(x)` depends only
on `(a,x,b)`, not on a chosen braid path, normal form, or representative.

Second, contextual crossing compatibility must hold.  Whenever
`r_X(x,y)=(u,v)`,

```text
r_Z(
  pi_{a,lambda_y b}(x),
  pi_{a lambda_x,b}(y)
)
=
(
  pi_{a,lambda_v b}(u),
  pi_{a lambda_u,b}(v)
).
```

Third, functionality must hold: equal `Z^2` input labels arising from hidden
contexts have equal `Z^2` output labels.

Fourth, totality and cofunctionality must make

```text
r_Z:Z^2 -> Z^2
```

a bijection.

Fifth, the Yang-Baxter equation must hold on all triples in `Z^3`, including
unreached triples.

Sixth, the maps

```text
Pi_n:X^n -> Z^n
```

must be globally orbit-injective:

```text
Pi_n(a)=Pi_n(b),  b in B_n.a  =>  a=b.
```

This last condition is decisive and is not inferred from local YBE axioms.

If holonomy labels satisfy rack relations, they are Branch I.  If they satisfy
these active YBE conditions but not rack relations, they are Branch II.  If
neither, they do not imply domination.

## Ordinary Quotients And Inert Observers

A usual YBE quotient

```text
q:X -> Z
```

with

```text
r_Z(q(x),q(y))=(q(u),q(v))
```

gives a braid-equivariant map `q^n:X^n -> Z^n`.  But the automatic kernel
direction is the wrong way:

```text
ker rho_n^X <= ker rho_n^Z.
```

To get domination reduction, one still must prove orbit-injectivity:

```text
q^n(a)=q^n(b),  b in B_n.a  =>  a=b.
```

Similarly, an inert observer or passive invariant gives bookkeeping but not a
domination-reducing factor unless it becomes rack-valued detection or
YBE-valued orbit-injective active data.

## Possible Counterexample Pattern

A counterexample to the Proper Contextual Dichotomy would be a finite
bijective YBE solution `X` with:

```text
nontrivial kernel-fiber monodromy,
no finite contextual rack detector separating all bad pairs,
no strictly proper active factor with orbit-injective Pi_n.
```

Equivalently, `X` would exhibit:

```text
residual-rigid harmful contextual collapse.
```

Such an `X` would satisfy:

```text
for every finite M, E_M collapses an actual bad pair;
every quotient of E_M also collapses that pair;
every proposed non-rack finite active label pi_{a,b}:X -> Z fails at least
one of compatibility, functionality, totality, cofunctionality/bijectivity,
YBE on unreached triples, global orbit-injectivity, properness.
```

The current formalism does not rule this out.  YBE is local, while
orbit-injectivity is global over all braid orbits and all arities.  The
residual endpoint obstruction shows that local endpoint quotients cannot
enforce it.  Proving that residual-rigid harmful collapse is impossible would
be a genuinely new theorem.

A minimal counterexample to Sawin, if one existed, would necessarily have this
residual-rigid pattern.  But a counterexample to the Proper Contextual
Dichotomy would not automatically disprove Sawin; Sawin could still hold by a
rack domination mechanism outside the contextual detector/active-descent
framework.

## Larger Finite State Quotients Do Not Help Inside E_M

For fixed `M`, let `D_M=(M,Phi_M)` be the strongest finite rack detector on
endpoint generators.  Then:

```text
E_M separates every kernel-fiber bad pair
iff
D_M separates every kernel-fiber bad pair.
```

Equality in `E_M^n` is exactly equality under `Phi_M^n Theta_n^M`.

Therefore, if there existed a larger finite quotient `M_0` such that
`Pi_n^{E_{M_0}}` were even bad-pair-injective, then `D_{M_0}` would be a
finite contextual rack detector separating every bad pair.

Under the no-detector hypothesis, no finite refinement `M_0` makes
`E_{M_0}` orbit-injective.  State refinement through residual endpoint systems
is unavailable.

## Independently Given Active Factor Conditions

Let finite data be given:

```text
M, Z, r_Z:Z^2 -> Z^2, pi_{a,b}:X -> Z.
```

Define

```text
Pi_n(x_1,...,x_n)_i=pi_{a_i,b_i}(x_i),
```

where

```text
a_i=theta(lambda_{x_1}...lambda_{x_{i-1}}),
b_i=theta(lambda_{x_{i+1}}...lambda_{x_n}).
```

The following are sufficient for kernel reflection:

```text
1. r_Z is total bijective YBE;
2. contextual compatibility holds for every r_X(x,y)=(u,v);
3. Pi_n is globally orbit-injective on braid orbits.
```

Then `Pi_n` is braid-equivariant.  If `beta in ker rho_n^Z`, then

```text
Pi_n(beta a)=beta Pi_n(a)=Pi_n(a).
```

Since `beta a in B_n.a`, orbit-injectivity gives `beta a=a`; hence

```text
ker rho_n^Z <= ker rho_n^X.
```

The truly necessary condition for kernel reflection is slightly weaker:

```text
for all beta in ker rho_n^Z and all a in X^n,
Pi_n(beta a)=Pi_n(a) => beta a=a.
```

But global orbit-injectivity is the clean structural condition.

The no-detector hypothesis forces none of:

```text
existence of Z,
|Z|<|X|,
contextual compatibility,
functionality/cofunctionality,
totality,
YBE on unreached triples,
orbit-injectivity.
```

## Conditional Contextual Reduction Theorem

The strongest currently valid theorem is conditional.

Let `X` be a finite bijective YBE solution.  Suppose at least one branch holds.

Branch I: direct finite rack absorption.  There is a finite contextual rack
detector

```text
D=(M,phi:C_M(X) -> Y)
```

separating every kernel-fiber bad pair.  Then a finite rack detector gives
the desired kernel inclusion for `X`.

Branch II: independent proper active factor.  There is a finite bijective YBE
solution `Z` with `|Z|<|X|`, a finite quotient `M` of `L_X`, and maps
`pi_{a,b}:X -> Z` such that the induced `Pi_n` are braid-equivariant and
globally orbit-injective.  Then

```text
ker rho_n^Z <= ker rho_n^X.
```

If every smaller finite bijective YBE solution is rack-dominated, then `X` is
rack-dominated.

This theorem is valid.  What is missing is the unconditional assertion that
one of the two branches always occurs.

## Residual-Rigid Harmful Collapse Exclusion

The missing theorem should be called:

```text
Finite Extraction Dichotomy
```

or, in the sharper no-detector formulation,

```text
Residual-Rigid Harmful Collapse Exclusion.
```

It says there is no finite bijective YBE solution `X` satisfying all three:

```text
1. no finite contextual rack detector separates all kernel-fiber bad pairs;
2. every residual endpoint system E_M is non-orbit-injective on an actual bad
   pair;
3. no strictly proper independent active factor Z with orbit-injective Pi_n
   exists.
```

Equivalently:

```text
harmful contextual collapse must either be finitely rack-absorbed or yield
independent strict active descent.
```

This is the exact remaining route.  The Proper Contextual Dichotomy is a
plausible structured theorem to aim for, but it is not currently supported by
the residual endpoint machinery.  It is not merely Sawin in new words, but
proving it requires a new theorem strong enough to exclude residual-rigid
harmful collapse.
