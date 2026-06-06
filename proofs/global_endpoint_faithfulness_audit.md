# Global Endpoint-Faithfulness Audit

Date: 2026-06-05

This note separates endpoint-faithfulness into pointwise and uniform forms.
It records exactly what follows from the directed system of finite context
quotients, and what still requires a new global theorem.

## Directed Visibility

Let `Q` be the directed set of finite quotients `M` of `L_X`, ordered by
refinement:

```text
N >= M means N -> M.
```

For a bad triple

```text
b=(n,a,beta),
a in X^n,
beta in K_n(P_X),
beta a != a,
```

define:

```text
D_M={
  b in B :
  exists i <= n with
  epsilon_i^M(a) not equiv_M epsilon_i^M(beta a)
}.
```

The contextual construction is functorial under refinement, so:

```text
N >= M implies D_M subset D_N.
```

For finitely many quotients `M_1,...,M_r`, their product quotient `N`
dominates all of them, hence:

```text
D_{M_1} union ... union D_{M_r} subset D_N.
```

This directedness is why a finite cover by quotient levels is equivalent to a
single finite quotient `M_*` with:

```text
B=D_{M_*}.
```

Also, membership in `D_M` depends on `beta` only through the endpoint word:

```text
c=beta a.
```

It does not depend on the braid word or path realizing `beta`.  The witnessed
triple is still useful for deletion, support, and Brunnian operations.

## Pointwise And Uniform Forms

The two forms are:

```text
Pointwise:
B=union_{M in Q} D_M.

Uniform:
exists M_* in Q with B=D_{M_*}.
```

Uniform implies pointwise.  Pointwise does not imply uniform without an
additional compactness, Noetherianity, finite-index, or bounded-support
theorem.

Pointwise gives only the finite-set version:

```text
for every finite F subset B, exists M_F with F subset D_{M_F}.
```

Choose a detecting quotient for each `b in F` and take a common refinement.

The obstruction to uniformity is the filter base:

```text
F_0={B \ D_M : M in Q}.
```

If uniform fails, every finite intersection of members of `F_0` is nonempty.
For `M_1,...,M_r`, choose a common refinement `N`.  If uniform fails, then
`B \ D_N` is nonempty, and:

```text
B \ D_N subset (B \ D_{M_1}) cap ... cap (B \ D_{M_r}).
```

Thus `F_0` extends to an ultrafilter `U` with:

```text
B \ D_M in U
```

for every finite quotient `M`.

Therefore:

```text
Uniform endpoint-faithfulness
iff
no harmful ultrafilter, principal or nonprincipal.
```

Pointwise endpoint-faithfulness excludes only principal harmful ultrafilters:

```text
Pointwise endpoint-faithfulness
iff
no principal harmful ultrafilter.
```

If pointwise holds and uniform fails, the harmful ultrafilter is necessarily
nonprincipal.

## Pointwise Endpoint-Faithfulness

Fix a bad triple:

```text
b=(n,a,beta),
beta in K_n(P_X),
c=beta a != a.
```

Since `c != a`, some coordinate changes:

```text
c_i != a_i.
```

Thus there is a formal endpoint change:

```text
epsilon_i^M(a)=(p_M,a_i,q_M),
epsilon_i^M(c)=(p'_M,c_i,q'_M).
```

The missing step is finite-rack separability:

```text
epsilon_i^M(a) not equiv_M epsilon_i^M(c)
```

for some finite `M`.

Equivalently, if `theta_M` is the finite residual congruence on `C_M(X)`,
then:

```text
s equiv_M t iff (d_s,d_t) in theta_M.
```

Pointwise endpoint-faithfulness says that every bad triple has some coordinate
endpoint pair escaping `theta_M` at some finite context level.

This does not follow formally from the universal rack shadow.  Since
`beta in K_n(P_X)`, the shadow returns:

```text
kappa^n(c)=kappa^n(a).
```

Thus every changed coordinate lies inside a `kappa`-fiber.  Noncontextual
finite rack shadows are already blind to it.

Residual finiteness of `L_X` also does not suffice.  It may separate prefixes
or suffixes in finite context quotients, but after choosing `M`, one still
needs a finite rack quotient of `C_M(X)` separating the endpoint generators.

The exact principal obstruction is:

```text
exists (n,a,beta) in B such that for every finite M and every i <= n,
epsilon_i^M(a) equiv_M epsilon_i^M(beta a).
```

This is a principal endpoint-invisible bad triple.

## Fixed-Arity Uniformity

Pointwise endpoint-faithfulness implies uniformity at each fixed arity.

For fixed `n`, define the finite transition set:

```text
T_n={
  (a,c) in X^n x X^n :
  c != a and exists beta in K_n(P_X) with c=beta a
}.
```

This is finite.  Also, `D_M`-membership depends only on `(n,a,c)`, not on the
chosen braid word.

If pointwise holds, choose a detecting quotient for every transition in
`T_n` and take their product.  This gives `M_n` such that every bad triple of
arity `n` lies in `D_{M_n}`.

Therefore, if pointwise holds but uniform fails, the harmful ultrafilter must
escape every bounded arity:

```text
{b=(n,a,beta) in B : n > N} in U
```

for every `N`.

Support escape, braid-word escape, and profinite non-clopen escape are
mechanisms for this arity escape.  Braid-word complexity is not independent at
fixed arity because `D_M` only sees the endpoint transition `(a,beta a)`.

## Profinite Relation R_infty

Let:

```text
hat S = hat{L_X} x X x hat{L_X}.
```

Each finite quotient `M` pulls back `equiv_M` to a clopen relation `R_M` on
`hat S`.  Define:

```text
R_infty = intersection_M R_M.
```

This relation is closed, but need not be open or finite-index.

Let `Pi` be the closure of the orbit-relevant endpoint-pair set:

```text
Pi = closure{
  (hat epsilon_i(a), hat epsilon_i(beta a)) :
  (n,a,beta) in B, 1 <= i <= n
}.
```

The useful finite-index hypothesis is:

```text
R_infty cap Pi is relatively clopen in Pi.
```

Equivalently, there is one finite quotient `M_0` such that:

```text
R_infty cap Pi = R_{M_0} cap Pi.
```

This is the contextual Myhill-Nerode finite-index condition for
orbit-relevant endpoint contexts.

Pointwise endpoint-faithfulness plus this finite-index condition implies
uniform endpoint-faithfulness.  If every bad triple has some coordinate
endpoint pair outside `R_infty`, then the same pair is outside `R_{M_0}`, so
every bad triple lies in `D_{M_0}`.

Thus:

```text
pointwise endpoint residuality
+
finite-index contextual Myhill-Nerode
implies
Target A uniformity.
```

The finite-index hypothesis is narrower in subject matter than Sawin's full
rack-domination question, but it is not known to be logically strictly weaker.

## Deletion And Contraction

A deletion or contraction proof would need operations:

```text
partial_I(n,a,beta)=(m,a_I,beta_I), m<n,
```

with:

```text
beta in K_n(P_X) implies beta_I in K_m(P_X),
beta a != a implies some minor remains bad,
visibility of the minor lifts to visibility of the original bad triple.
```

The obstruction is that YBE color propagation is not functorial under strand
deletion.  Removing a strand also removes crossings that may have changed the
colors on retained strands:

```text
delete after acting != act after deleting.
```

A Brunnian bad triple can be nontrivial globally while every proper deletion
or contraction either:

```text
- is not compatible with the YBE action,
- leaves the kernel K_m(P_X),
- becomes trivial,
- loses the endpoint visibility relation,
- or fails to lift visibility back to the original triple.
```

A deletion proof must rule out such Brunnian behavior by a new global
visibility-reflecting minor theorem.

## Bounded-Support Criterion

A bounded-support theorem strong enough for uniformity would be:

```text
There exists N such that every bad triple has a bad visibility-reflecting
minor of arity <= N.
```

If pointwise holds, finitely many endpoint transitions in arities `<=N` can be
detected by one finite quotient, and the minor-lifting property detects every
bad triple.

Finite index of `K_n(P_X)` in `B_n` for each fixed `n` is not enough.  It gives
no uniform bound in `n`, no bounded-support generation, and no control of the
finite-stage complexity of the contextual rack relation.

## Special Branches

In finite rack solutions, `P_X` is already faithful and there are no bad
triples relative to the rack shadow.

In the trivial solution, the braid action is trivial and there are no bad
triples.

In left-nondegenerate solutions, derived-rack and guitar-map machinery gives
arity-uniform rack control of the YBE action.  This prevents Brunnian
endpoint-invisible monodromy, but it uses branch recoverability not available
for general bijective solutions.

In nondegenerate involutive or symmetric solutions, the left-nondegenerate
branch applies and pure braid-word Brunnian escape is eliminated by the
finite permutation/rack model.

Bare involutive but degenerate solutions are not automatically covered by
that derived-rack control.

In constant-action and permutation classes, the action reduces to finite
one-strand group/permutation data, so finite-state endpoint recognition
prevents higher contextual holonomy.

Products of positive branches remain positive under product detection.
Padding does not break the corrected arity-relative formulation, but it shows
why fixed-coordinate formulations are wrong.

## Target B Does Not Follow

Failure of endpoint-faithfulness gives negative information about finite rack
quotients of contextual endpoint racks.  It does not construct finite active
YBE data:

```text
Z, r_Z:Z^2 -> Z^2, pi
```

with total bijective YBE, coordinatewise compatibility, and global
orbit-injectivity.

Residual endpoint quotients are tests, not active factors.  Target B remains
an independent extraction theorem.

## Sharp Valid Theorems

Theorem A: directed-cover / ultrafilter equivalence.

Assuming functoriality `N>=M => D_M subset D_N`, the following are equivalent:

```text
exists M_* with B=D_{M_*};

there is no ultrafilter U on B with B\D_M in U for every M.
```

Pointwise endpoint-faithfulness is equivalent to nonexistence of principal
harmful ultrafilters.

Theorem B: fixed-arity uniformity.

If pointwise endpoint-faithfulness holds, then for every `N` there exists a
finite quotient `M_{<=N}` such that:

```text
{b in B : arity(b) <= N} subset D_{M_{<=N}}.
```

Hence any nonprincipal harmful ultrafilter must escape to unbounded arity.

Theorem C: profinite contextual Myhill-Nerode criterion.

If pointwise endpoint-faithfulness holds and `R_infty cap Pi` is relatively
clopen in `Pi`, then there exists one finite quotient `M_*` with:

```text
B=D_{M_*}.
```

Theorem D: bounded-minor criterion.

If every bad triple has a bad visibility-reflecting minor of arity at most
`N`, then pointwise endpoint-faithfulness implies uniform
endpoint-faithfulness.

## Remaining Gap

The current YBE/contextual machinery proves neither:

```text
pointwise endpoint-faithfulness
```

nor:

```text
uniform endpoint-faithfulness from pointwise.
```

The missing theorem must be one of:

```text
contextual endpoint residuality;
finite-index/profinite contextual Myhill-Nerode;
bounded-support/deletion/no-Brunnian theorem;
independent active extraction.
```

The global endpoint-faithfulness principle is therefore not a formal
consequence of the present definitions.  It is the missing finite-index or
no-Brunnian assertion needed to pass from local contextual separation to one
uniform finite rack-dominating construction.
