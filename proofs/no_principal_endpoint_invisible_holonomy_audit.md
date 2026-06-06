# No Principal Endpoint-Invisible Holonomy Audit

Date: 2026-06-05

This note records the audit of the no-principal-endpoint-invisible-holonomy
theorem.  The theorem is exactly pointwise endpoint-faithfulness, provided the
quantifiers are written in their nonuniform form.

## Exact Equivalence

Let

```text
rho_n^X:B_n -> Sym(X^n)
```

be the braid action, and let

```text
K_n(P_X)=ker rho_n^{P_X}.
```

For a rack `R`, define its finite residual congruence:

```text
Rad_fin(R)=intersection over q:R->Q, Q finite rack, of ker q.
```

For `R=C_M(X)`, write:

```text
u equiv_M v
```

if `(u,v) in Rad_fin(C_M(X))`.

A principal endpoint-invisible bad triple is:

```text
(n,a,beta),
a in X^n,
beta in K_n(P_X),
c=rho_n^X(beta)a != a,
```

such that:

```text
for every finite quotient M of L_X and every i <= n,
epsilon_i^M(a) equiv_M epsilon_i^M(c).
```

Expanding the residual congruence:

```text
for every M, every i <= n, and every finite rack quotient
q:C_M(X)->Q,

q(epsilon_i^M(a))=q(epsilon_i^M(c)).
```

Its negation is precisely:

```text
for all n,a,beta in K_n(P_X),
if rho_n^X(beta)a != a,
then there exist M, i<=n, and a finite rack quotient q:C_M(X)->Q such that

q(epsilon_i^M(a)) != q(epsilon_i^M(rho_n^X(beta)a)).
```

Thus:

```text
no principal endpoint-invisible bad triple
iff
pointwise endpoint-faithfulness.
```

There are three quantifier traps.

First, closed in `P_X` must mean:

```text
beta in K_n(P_X),
```

not merely:

```text
rho_n^{P_X}(beta) kappa^n(a)=kappa^n(a).
```

The latter is only pointwise closure of one labelled tuple and is too weak for
kernel domination.

Second, the finite quotient `M` may depend on the triple `(n,a,beta)`.
Asking for one `M` for all triples is the uniform theorem.

Third, the coordinate is existential.  A principal invisible triple is
invisible in every coordinate; to refute it, one separating coordinate is
enough.

## What P_X Does And Does Not Control

The universal rack shadow `P_X` factors ordinary finite rack-valued shadows of
single `X`-letters:

```text
X -> finite rack R.
```

Therefore, if:

```text
beta in K_n(P_X),
```

then every context-free finite rack shadow of `X` is blind to `beta`.

Contextual endpoint tests are different.  They have the form:

```text
epsilon_i^M:X^n -> C_M(X),
```

and after a finite rack quotient:

```text
q epsilon_i^M:X^n -> Q.
```

They depend on the whole word, the coordinate, and the finite context quotient
`M`.  They are not automatically finite rack shadows of the single endpoint
letter.

Thus the attempted proof:

```text
all finite endpoint tests factor through P_X
```

fails.  `P_X` encodes context-free finite rack shadows, not all contextual
endpoint tests.

Contextual endpoint tests may see more than `P_X`, but they may still miss
fiber monodromy if the relevant endpoint elements are:

```text
- equal in C_M(X), or
- equal in every finite rack quotient of C_M(X).
```

## Orbit-Relevant Residuality

Let `E_M^rel` be the set of endpoint elements that arise from principal
transitions:

```text
E_M^rel={
  epsilon_i^M(a), epsilon_i^M(c) :
  c=rho_n^X(beta)a,
  beta in K_n(P_X),
  c != a
}.
```

The needed residual-finiteness hypothesis is:

```text
for all e,e' in E_M^rel,
if e != e' in C_M(X),
then there exists q:C_M(X)->Q finite rack with q(e) != q(e').
```

Equivalently:

```text
Rad_fin(C_M(X)) cap (E_M^rel x E_M^rel)
=
Delta_{E_M^rel}.
```

This is much weaker than full residual finiteness of `C_M(X)`.  Target A only
needs finite residual separation on orbit-relevant endpoint elements.

## Strong Versus Residual Invisibility

Strong invisibility means:

```text
for every M and every i,
epsilon_i^M(a)=epsilon_i^M(c)
```

inside `C_M(X)`.

To rule this out one needs strong endpoint separation:

```text
c=rho_n^X(beta)a != a, beta in K_n(P_X)
implies
exists M,i with epsilon_i^M(a) != epsilon_i^M(c) in C_M(X).
```

This is not automatic.  Endpoint maps are not assumed to be injective on
`X^n`, and local YBE coherence does not imply injectivity.

Residual invisibility means endpoint elements may be distinct in `C_M(X)` but
equal in every finite rack quotient:

```text
epsilon_i^M(a) != epsilon_i^M(c),
but
epsilon_i^M(a) equiv_M epsilon_i^M(c).
```

Residual invisibility reduces to non-residual-finiteness only after strong
invisibility is excluded.

Thus the useful decomposition is:

```text
no principal invisibility
follows from
strong endpoint separation
+
orbit-relevant finite residuality.
```

## Minimal Arity And Deletion

If a principal invisible triple exists, choose one of minimal arity `n`.  Since
arity one has no nontrivial braid, `n>=2`.

Minimality does not produce a contradiction.  A deletion argument would need
to preserve all of:

```text
beta in K_n(P_X),
beta a != a,
endpoint invisibility,
and contextual rack separability.
```

Deleting an observer strand is not dynamically neutral.  The deleted strand
may cross retained strands and temporarily change their colors via `L_x` or
`R_y`; removing it before applying the braid removes those operations.

An observer strand can be essential because it:

```text
1. makes beta lie in K_n(P_X);
2. supplies contextual M-state;
3. changes another strand and later returns to its endpoint;
4. participates in cancellations visible in P_X but not in X.
```

Thus minimal arity only says every strand is essential in the sense that
deleting it fails at least one required property.

## Braid Witnesses

Endpoint invisibility depends only on:

```text
(a,c), where c=rho_n^X(beta)a.
```

It does not depend on the braid word.

For fixed `a,c`, the witness set is:

```text
W(a,c)={beta in K_n(P_X): rho_n^X(beta)a=c}.
```

If `beta,beta' in W(a,c)`, then `beta'^{-1}beta` stabilizes `a` and lies in
`K_n(P_X)`.  Choosing a shorter or more local representative is a
coset-minimization problem.  There is no formal theorem that such a
representative exists.

Path-dependent holonomy cannot refute endpoint invisibility unless it
descends to word-defined finite rack-valued endpoint data.

## Special Branches

Racks rule out principal invisible triples internally: if `X` is already a
finite rack, then `P_X` is essentially `X`, so `K_n(P_X)=K_n(X)` and no
nonclosed principal transition exists.

Left-nondegenerate solutions are handled if one invokes derived-rack or
guitar-map recoverability and if that recoverability is contextually
realized.  Without contextual realization, it may prove a separate rack
absorber but not no invisibility inside the `C_M(X)` framework.

Nondegenerate involutive or symmetric solutions require a concrete recovery or
finite rack-valued endpoint theorem for the same reason.  Involutivity alone
does not prove finite residual separation in `C_M(X)`.

Permutation or constant-action solutions are safe when the finite permutation
fiber action is finitely rack-recoverable by endpoint labels.  This does not
follow from `P_X` alone.

Products require compatibility of contextual endpoint projections.  Padding
preserves some bad triples but illustrates why deletion is not formal.

## Finite-Table Obstruction Pattern

A finite-table obstruction would require:

```text
1. a finite bijective YBE table r(x,y)=(L_x(y),R_y(x));
2. a nontrivial rack-shadow fiber x != y with kappa(x)=kappa(y);
3. n,a,beta with beta in K_n(P_X) but rho_n^X(beta)a != a;
4. for every finite M and every i, the endpoint pair lies in
   Rad_fin(C_M(X)).
```

The first item is controlled by the component YBE identities and bijectivity.
The fourth item is not merely finite-table data.  It is a statement about all
finite rack quotients of all contextual endpoint racks.

Any genuine counterpattern must force either:

```text
strong endpoint collapse,
```

or:

```text
non-residual-finite endpoint pairs in every relevant C_M(X).
```

## No Automatic Enrichment Or Target B

A principal invisible triple is negative information:

```text
c != a,
but all current finite contextual endpoint tests identify a and c.
```

If the triple is strongly invisible, there is no endpoint distinction to
quotient.  If it is residually invisible, finite residual separation is
exactly what is missing.

To turn the triple into Target B, one must independently construct finite
coordinatewise YBE data:

```text
Z finite,
r_Z:Z^2 -> Z^2 total bijective YBE,
word-defined labels Lambda_n:X^n -> Z^n,
braid equivariance,
global orbit-injectivity or kernel inclusion.
```

Path holonomy is not enough unless it descends to word-defined, finite
rack-valued endpoint data or to a genuine finite YBE action.

## Sharp Valid Theorem

Let `X` be finite bijective, with universal finite rack shadow `kappa:X->P_X`,
and let `C_M(X)` be the contextual endpoint racks.  Define principal
transitions:

```text
a -> c if c=rho_n^X(beta)a for some beta in K_n(P_X).
```

Then the following are equivalent:

```text
1. no principal endpoint-invisible bad triple;

2. for every principal transition a -> c with c != a, there exist finite M,
   i <= n, finite rack Q, and q:C_M(X)->Q such that

   q(epsilon_i^M(a)) != q(epsilon_i^M(c)).
```

This is pointwise endpoint-faithfulness.

Sufficient hypotheses include:

```text
A. endpoint residual faithfulness directly;
B. strong endpoint separation plus orbit-relevant finite residuality;
C. full residual finiteness of relevant C_M(X) plus strong endpoint separation;
D. contextually realized enriched finite endpoint labels;
E. derived-rack/guitar-map recoverability plus contextual realization;
F. the rack case;
G. no-principal-holonomy as an axiom.
```

## Current Boundary

Principal endpoint-invisible bad triples cannot be ruled out from:

```text
- the universal property of P_X alone;
- local YBE coherence alone;
- contextual endpoint transport coherence alone.
```

The exact missing theorem is:

```text
Every nontrivial K_n(P_X)-principal endpoint transition is separated by some
finite residual contextual endpoint rack.
```

A useful decomposition is:

```text
strong endpoint separation
+
finite residuality on orbit-relevant endpoint generators.
```

Without one of these hypotheses, contextual endpoints may see more than
`P_X`, but may still miss `K_n(P_X)`-fiber monodromy.
