# Target A Primitive Bad-Core Frontier

Date: 2026-06-05

This note records the split between Target A and Target B after the finite
extraction dichotomy audit.  The contextual route is now reduced to:

```text
Residual-Rigid Harmful Collapse Exclusion
```

or equivalently:

```text
Finite Extraction Dichotomy.
```

Harmful contextual collapse must either be finitely rack-absorbed or yield an
independently constructed strict active descent.

This is not proved by compactness, residual endpoint quotients, local YBE
identities, or ordinary finite-state arguments.  It is also not merely Sawin
rewritten: it asks for a specific mechanism, namely contextual rack absorption
or strict orbit-injective YBE descent.  But proving it would imply Sawin by
induction.

The most actionable subtarget is Target A, direct finite rack absorption.
Target B is logically possible but currently behaves like an added hypothesis
unless one finds a genuinely non-rack source of coordinatewise YBE data.

## Target A As A Finite Cover Problem

Let `D` range over finite contextual rack detectors.  For a detector `D`,
define

```text
B_D={bad pairs not separated by D}.
```

Then `D` separates all bad pairs if and only if

```text
B_D=empty.
```

If `D_1,D_2` are detectors, their product detector satisfies

```text
B_{D_1 x D_2}=B_{D_1} cap B_{D_2}.
```

Therefore direct finite rack absorption is equivalent to:

```text
There exist finitely many detectors D_1,...,D_k such that every bad pair is
separated by at least one D_i.
```

Taking the product detector

```text
D=D_1 x ... x D_k
```

then separates every bad pair.

Thus every proposed Target A mechanism must produce a finite cover of the
bad-pair set by detector-separated pieces.

## Bounded Arity

A useful theorem would be:

```text
Bounded bad-arity theorem.
There exists N=N(X) such that if a detector separates all bad pairs in
arities <= N, then it separates all bad pairs in every arity.
```

This would reduce uniform absorption to finitely many finite sets
`X^1,...,X^N`, assuming pointwise finite contextual separability in those
arities.

Current status:

```text
open; not supplied by known tools.
```

The difficulty is that bad pairs may arise from braid words involving
arbitrarily many strands.  The local YBE relation controls three adjacent
strands but does not imply that every nontrivial kernel-fiber monodromy has a
bounded-size subconfiguration witnessing it.

The missing sublemma would be:

```text
every harmful kernel-fiber monodromy contains a bounded arity harmful core.
```

## Bounded Braid Word Complexity

A useful theorem would be:

```text
Bounded kernel-word theorem.
There exists L=L(X) such that every bad pair (a,beta a) has another bad
representative (a,gamma a) with gamma in K_n(P_X), |gamma| <= L, and whose
contextual labels force separation of the original bad pair.
```

A version with `L` depending on `n` would not by itself give one uniform
detector over all arities.

Current status:

```text
open and probably too strong without extra structure.
```

For fixed `n`, the image of `B_n` in `Sym(X^n)` is finite, so finite word
representatives exist.  Their lengths can grow with `n`, and local YBE
identities give no uniform shortening theorem for elements of

```text
K_n(P_X)
```

acting nontrivially on `X^n`.

## Finite-Index Contextual Myhill-Nerode

A useful theorem would be:

```text
Contextual Myhill-Nerode theorem.
There is a finite-index equivalence relation on all orbit-relevant contextual
braid states such that:
1. it is stable under braid generators and contextual extension;
2. it distinguishes every bad state from its base state;
3. it is realized by a finite rack quotient of some C_M(X).
```

Current status:

```text
not proved; ordinary Myhill-Nerode does not apply.
```

The relevant language is not a regular language over a fixed finite alphabet:
the arity varies, the braid group varies, and the contextual labels depend on
products in finite quotients of `L_X`.  The fixed-`M` finite-index endpoint
approximation is exactly `E_M`, and under the harmful hypothesis `E_M` is
already known to collapse actual bad pairs.

Thus a successful theorem must use more than endpoint states.  It would need
a finite-index theory of reachable braid holonomy that is also rack-realizable.

## Context-Stable Clopen Core Cover

A useful theorem would be:

```text
Context-stable clopen core theorem.
The bad-pair set admits a finite cover B subset C_1 union ... union C_k by
context-stable clopen sets, and for each C_i there is a finite detector D_i
separating every bad pair in C_i.
```

Then the product detector separates all bad pairs.

Current status:

```text
open; compactness alone does not prove it.
```

If no finite detector separates all bad pairs, every `B_D` is nonempty and the
family `{B_D}` has the finite intersection property.  Hence there is a
harmful ultrafilter `U` containing all `B_D`.

If `C` is a clopen core separated by `D`, then

```text
C cap B_D = empty.
```

Since `B_D in U`, one has `C notin U`.  Thus harmful ultrafilters avoid every
already detector-separated finite clopen core unless a new YBE-specific finite
cover theorem is proved.

## Uniform Reachable Escape-Holonomy Separation

A useful theorem would be:

```text
Uniform reachable holonomy separation theorem.
Every nontrivial actual kernel-fiber monodromy element is detected by finite
rack-valued contextual holonomy, and finitely many such finite rack quotients
detect all actual bad pairs.
```

This is stronger than pointwise residual finiteness.  Pointwise separation
says:

```text
for every bad pair, there exists D separating it.
```

Uniform absorption requires:

```text
there exists one D separating all bad pairs.
```

Current status:

```text
open; pointwise holonomy detection is not enough.
```

Reachable holonomy is relevant only if it is realized by actual pairs

```text
a, beta a,  beta in K_n(P_X).
```

Ambient holonomy in a completion or groupoid is irrelevant unless it appears
on actual `X^n` orbits.

## Special Structure Of K_n(P_X)

Since `P_X` is a rack, `B_n` acts on `P_X^n`, and

```text
K_n(P_X)=ker rho_n^{P_X}
```

has finite index in `B_n`.

A useful theorem would be:

```text
Uniform rack-kernel finite-basis theorem.
The actual action of all groups K_n(P_X) on all fibers F_p subset X^n is
generated, up to contextual detection, by finitely many local kernel moves.
```

Then finitely many detectors could separate all primitive moves and therefore
all bad pairs.

Current status:

```text
open.
```

For each fixed `n`, `K_n(P_X)` has finite index in `B_n`, but the family over
all `n` is unbounded.  YBE identities give braid consistency, not a finite
basis for all `P_X`-trivial braid monodromy on `X^n`.

## Target B Audit

An independent active factor consists of finite data

```text
M, Z, r_Z:Z^2 -> Z^2, pi_{a,b}:X -> Z
```

with `|Z|<|X|`, such that `r_Z` is total bijective YBE, contextual
compatibility holds, and the induced maps

```text
Pi_n:X^n -> Z^n
```

are globally orbit-injective.

Under the no-detector hypothesis, this active factor cannot factor through
`E_M`.  It must separate finite-rack-invisible endpoint pairs:

```text
s equiv_M t but pi(s) != pi(t).
```

This is genuinely non-rack data.

Possible sources include:

```text
reachable holonomy,
inert observers,
non-endpoint finite states,
escape groupoid finite quotients,
ordinary YBE quotients,
algebraic decompositions of X,
semigroup / Green / Rees structure.
```

Each source currently falls into the same trichotomy:

```text
if it satisfies rack relations, it is Target A;
if it satisfies total bijective YBE and orbit-injectivity, it is Target B;
otherwise it is diagnostic data.
```

The missing bridge is:

```text
finite-rack-invisible reachable holonomy must be finitely coordinatizable as
a proper orbit-injective YBE factor.
```

No current argument supplies this.  Target B is therefore less currently
actionable than Target A.

## Counterexample Pattern

A counterexample to the finite extraction dichotomy would be a finite
bijective YBE solution `X` with:

```text
1. nontrivial kernel-fiber monodromy over P_X;
2. no finite contextual detector separating all bad pairs;
3. for every finite quotient M of L_X, E_M collapses an actual bad pair;
4. every proper candidate active factor fails well-definedness, contextual
   compatibility, functionality, cofunctionality, totality, bijectivity, YBE
   on all Z^3, braid equivariance, global orbit-injectivity, or kernel
   reflection.
```

Such an `X` would be residual-rigid and active-simple.

YBE imposes strong local identities, so arbitrary finite permutation data on
all `X^n` cannot be realized.  But local YBE identities do not force finite
detector existence, uniform finite bad-pair covers, bounded arity, bounded
braid complexity, orbit-injectivity of proper quotients, or total YBE
extension on unreached triples.

No explicit finite counterexample is produced by the formalism, but the
formalism also does not exclude the pattern.

## Logical Status

Residual-Rigid Harmful Collapse Exclusion is more structured than Sawin and
therefore logically stronger as a route.  Sawin asks only for a finite rack
`Y` with

```text
ker rho_n^Y <= ker rho_n^X.
```

The exclusion asks that harmful contextual collapse be resolved by one of two
specific mechanisms:

```text
finite contextual detector,
strict orbit-injective active descent.
```

Every minimal Sawin counterexample would be a residual-rigid harmful collapse.
Thus the exclusion implies Sawin.  But Sawin could still hold even if the
exclusion failed, via a rack domination mechanism outside contextual
detectors and active factors.

## Sharpest Next Theorem

The most precise remaining theorem is:

```text
Finite Extraction Dichotomy.

Every finite bijective set-theoretic YBE solution X admits either:

Branch I: direct finite rack absorption by a finite contextual rack detector;

Branch II: independent proper active descent through finite non-rack data
M,Z,r_Z,pi_{a,b} not factoring through residual endpoint quotients E_M,
with total bijective YBE, braid equivariance, and global orbit-injectivity.
```

Target A is more actionable because it stays inside the finite rack-detector
framework.  Its most concrete formulation is:

```text
Primitive bad-pair finite-basis theorem.
There exists a finite set of primitive bad-pair patterns such that every bad
pair contains, reduces to, or factors through one of them in a context-stable
YBE-compatible way; moreover each primitive pattern is separated by a finite
contextual rack detector.
```

Taking the product of the finitely many primitive-pattern detectors would give
direct finite rack absorption.

Target B remains a fallback: if Target A fails, the failure data should be
searched for genuinely non-rack holonomy capable of satisfying the full
active-factor axioms.
