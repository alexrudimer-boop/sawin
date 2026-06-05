# Finite Extraction Dichotomy Boundary

Date: 2026-06-05

This note records the current endpoint of the contextual route.  The
Residual-Rigid Harmful Collapse Exclusion is the exact missing theorem for
this route.  It is not presently a consequence of residual endpoint machinery,
compactness, or local Yang-Baxter identities.

The strongest valid conclusion is conditional:

```text
Sawin follows if every finite X admits either finite rack absorption or strict
orbit-injective active descent.
```

After residual endpoint extraction is ruled out, the active descent branch is
not forced by the no-detector hypothesis.  It is an additional non-rack
extraction theorem that still needs proof.

## Formal Reduction To Residual-Rigid Harmful Collapse

Let `X` be a finite bijective set-theoretic YBE solution.  Let `P_X` be the
universal finite rack shadow, and let

```text
K_n(P_X)=ker rho_n^{P_X}.
```

A kernel-fiber bad pair is

```text
(a,beta a),
a in X^n,
beta in K_n(P_X),
beta a != a.
```

If there are no bad pairs, then

```text
K_n(P_X) <= ker rho_n^X
```

for every `n`, so the finite rack `P_X` already dominates `X`.

Suppose now that `X` is a minimal counterexample to Sawin with respect to
`|X|`.  Then:

```text
1. X has bad pairs.
2. No finite contextual rack detector separates all bad pairs.
3. For every finite M, the residual endpoint quotient E_M is non-orbit-
   injective on an actual bad pair.
4. There is no strictly proper active factor Z with |Z|<|X| and
   ker rho_n^Z <= ker rho_n^X.
```

Item 2 holds because a detector

```text
D=(M,phi:C_M(X)->Y)
```

separating all bad pairs would give a finite rack such as `P_X x Y` with

```text
ker rho_n^{P_X x Y} <= ker rho_n^X.
```

Item 3 is the residual endpoint obstruction: for every fixed `M`, the
strongest finite-rack observable endpoint system `E_M` is realized by one
finite rack quotient, so if it were bad-pair-injective then a finite detector
would exist.

Item 4 holds by minimality: a proper active factor `Z` with

```text
ker rho_n^Z <= ker rho_n^X
```

would be rack-dominated by induction, forcing `X` to be rack-dominated.

Thus every minimal counterexample to Sawin is a residual-rigid harmful
collapse.

The converse is not formal.  Sawin might still be true by a rack domination
mechanism not arising from contextual detectors or proper active descent.
Therefore the Proper Contextual Dichotomy is stronger and more structured
than Sawin, though it is exactly the missing theorem for this route.

## Local YBE Identities Are Not Enough

For

```text
r_X(x,y)=(L_x(y), R_y(x)),
```

the YBE gives the coordinate identities

```text
L_{L_x(y)} L_{R_y(x)}(z)=L_x L_y(z),

R_{L_{R_y(x)}(z)}(L_x(y))
=
L_{R_{L_y(z)}(x)}(R_z(y)),

R_z(R_y(x))
=
R_{R_z(y)}(R_{L_y(z)}(x)).
```

These hold without assuming individual `L_x` or `R_y` maps are bijective.
They are local identities on triples.  They guarantee that the braid action is
well-defined and that contextual labels transform compatibly when the
contextual rack relations hold.

They do not imply:

```text
finite detector existence,
finite-index residual stabilization,
orbit-injectivity of a quotient,
existence of a strictly smaller YBE factor,
YBE totalization on unreached triples.
```

Thus excluding residual-rigid harmful collapse requires a genuinely global
consequence of YBE, not just the local braid relation.

## Residual Endpoint Extraction Remains Closed

Fix a finite quotient

```text
theta:L_X -> M.
```

Let

```text
S_M=M x X x M,
delta_{a,x,b}=d_{a,x,b} in C_M(X).
```

Define `s equiv_M t` if every finite rack quotient of `C_M(X)` identifies
`delta_s` and `delta_t`, and let

```text
E_M=S_M/equiv_M.
```

Because `S_M` is finite, one finite rack quotient

```text
Phi_M:C_M(X)->Y_M
```

realizes `E_M` on endpoint generators.

Under the no-detector hypothesis, even this strongest fixed-`M` detector
fails.  Therefore there are

```text
n, a in X^n, beta in K_n(P_X)
```

with

```text
beta a != a
```

but

```text
Phi_M^n Theta_n^M(beta a)=Phi_M^n Theta_n^M(a).
```

Equivalently,

```text
Pi_n^{E_M}(beta a)=Pi_n^{E_M}(a).
```

Thus `E_M` is not orbit-injective.  If `q:E_M -> Z` is any quotient, then

```text
Pi_n^Z=q^n Pi_n^{E_M}
```

also collapses the same bad pair.  No quotient or totalization factoring
through `E_M` can restore orbit-injectivity.

The same argument rules out a larger finite `M_0` if the construction still
factors through `E_{M_0}`.  If `E_{M_0}` were bad-pair-injective, then the
corresponding strongest detector `D_{M_0}` would separate all bad pairs.

## Branch I: Direct Finite Rack Absorption

Branch I asks for one finite detector

```text
D=(M,phi:C_M(X)->Y)
```

that separates every bad pair.

Let

```text
B_D={bad pairs not separated by D}.
```

Product detectors satisfy

```text
B_{D_1 x D_2}=B_{D_1} cap B_{D_2}.
```

Therefore finite rack absorption is equivalent to

```text
exists D, B_D=empty.
```

If no detector works, the family `{B_D}` has the finite intersection property
and yields a harmful ultrafilter containing every `B_D`.

A direct absorption theorem must prove a finite boundedness statement, such
as:

```text
all bad pairs are covered by finitely many detector-separated cores.
```

Possible mechanisms include:

```text
bounded arity reduction,
bounded braid-complexity reduction,
finite-index YBE Myhill-Nerode,
context-stable clopen core cover,
uniform reachable holonomy separation.
```

None follows formally from compactness, Higman, Stone duality, profinite
closedness, or ordinary automata theory.

## Branch II: Independent Active Extraction

Branch II asks for finite data

```text
M, Z, r_Z:Z^2 -> Z^2, pi_{a,b}:X -> Z
```

with `|Z|<|X|` such that the induced maps

```text
Pi_n:X^n -> Z^n
```

are braid-equivariant and globally orbit-injective.

Under the no-detector hypothesis, `Z` cannot factor through `E_M`.  Therefore
for some finite `M`, there must be endpoint symbols `s,t in S_M` with

```text
s equiv_M t
```

but

```text
pi(s) != pi(t).
```

So `Z` separates finite-rack-invisible endpoint data.  It is genuinely
non-rack data.

Possible sources include:

```text
reachable path or holonomy data,
inert observer data,
non-endpoint finite states,
escape groupoid quotients,
ordinary algebraic quotients of X.
```

Each source must become either a finite rack detector or a finite active YBE
factor.  If it is neither, it is only diagnostic.

## Exact Requirements For A Non-E_M Active Factor

Let finite data be given:

```text
M, Z, pi_{a,b}:X -> Z, r_Z:Z^2 -> Z^2.
```

The requirements are:

```text
1. uniform well-definedness:
   pi_{a,b}(x) depends only on a,b in M and x in X;

2. contextual compatibility:
   for r_X(x,y)=(u,v),
   r_Z(pi_{a,lambda_y b}(x), pi_{a lambda_x,b}(y))
   =
   (pi_{a,lambda_v b}(u), pi_{a lambda_u,b}(v));

3. functionality:
   equal Z^2 input labels have equal Z^2 output labels;

4. cofunctionality:
   equal Z^2 output labels come from equal Z^2 input labels;

5. totality:
   every pair in Z^2 has an assigned image;

6. bijectivity:
   r_Z:Z^2 -> Z^2 is a bijection;

7. YBE on all triples in Z^3, including unreached triples;

8. braid equivariance of Pi_n;

9. global orbit-injectivity:
   Pi_n(a)=Pi_n(b), b in B_n.a => a=b;

10. properness:
   |Z|<|X|.
```

Contextual compatibility plus total bijective YBE gives braid equivariance.
Kernel reflection follows from orbit-injectivity:

```text
ker rho_n^Z <= ker rho_n^X.
```

The no-detector hypothesis forces none of the structural requirements above.
Therefore Branch II is an added extraction theorem, not a formal consequence
of harmful contextual collapse.

## Possible Counterexample Pattern

A counterexample to the Residual-Rigid Harmful Collapse Exclusion would be a
finite bijective YBE solution `X` satisfying:

```text
1. kernel-fiber monodromy over P_X is nontrivial;
2. no finite contextual rack detector separates all bad pairs;
3. for every finite M, E_M collapses an actual bad pair;
4. every active-factor attempt fails well-definedness, compatibility,
   functionality, cofunctionality, totality, bijectivity, YBE on unreached
   triples, braid equivariance, global orbit-injectivity, or properness.
```

Such a solution would be active-simple in the domination sense: it has no
proper orbit-injective YBE descent.

YBE makes such a construction nontrivial because all braid dynamics must come
from one local bijection `r_X:X^2 -> X^2`.  But YBE is local, while detector
absorption and orbit-injectivity are global over all arities.  The current
formalism neither constructs nor excludes this pattern.

## Logical Status

The Proper Contextual Dichotomy is not Sawin in new words.  It asks for
structured data:

```text
finite contextual rack detector
```

or

```text
strict orbit-injective active descent.
```

Sawin asks only for some finite rack `Y` with

```text
ker rho_n^Y <= ker rho_n^X.
```

The dichotomy is strong enough to prove Sawin by induction, but the missing
Residual-Rigid Harmful Collapse Exclusion is exactly the unsupported step.

## Conditional Contextual Reduction Theorem

Let `X` be finite bijective.  Assume at least one branch holds.

Branch I: direct finite rack absorption.  There is a finite contextual rack
detector

```text
D=(M,phi:C_M(X)->Y)
```

separating every kernel-fiber bad pair.  Then `P_X x Y` is a finite rack with

```text
ker rho_n^{P_X x Y} <= ker rho_n^X.
```

Branch II: independent proper active factor.  There is a finite bijective YBE
solution `Z` with `|Z|<|X|`, finite `M`, and maps `pi_{a,b}:X -> Z` such that
`Pi_n` is braid-equivariant and globally orbit-injective.  Then

```text
ker rho_n^Z <= ker rho_n^X.
```

If every smaller finite bijective YBE solution is rack-dominated, then `X` is
rack-dominated.

This theorem is valid.  What remains unproved is the unconditional assertion
that one branch must always occur.

## Next Actionable Target

The next theorem should be stated as:

```text
Residual-Rigid Harmful Collapse Exclusion.
```

Equivalently:

```text
A finite bijective YBE solution with harmful contextual collapse must either
admit direct finite rack absorption or admit an independently constructed
strictly proper active factor with orbit-injective coordinate maps.
```

This has two subtargets:

```text
Target A: Direct finite rack absorption.
  Prove a YBE-specific bounded-core / finite-index / holonomy-uniformity
  theorem producing one finite contextual rack detector.

Target B: Independent active extraction.
  Construct non-rack finite data M,Z,r_Z,pi_{a,b} not factoring through E_M
  and prove |Z|<|X|, total bijective YBE, braid equivariance, and global
  orbit-injectivity.
```

At the present boundary, Target B is an added extraction theorem.  It is not
forced by residual endpoint collapse.

The precise missing sublemma is:

```text
finite extraction dichotomy / residual-rigid harmful collapse exclusion.
```
