# Finite Endpoint-Change Cover Theorem

Date: 2026-06-05

This note records the sharp Target A formulation.  Because finite contextual
rack detectors label words coordinatewise, direct finite rack absorption is
equivalent to a finite basis theorem for one-coordinate contextual endpoint
changes.  Multi-coordinate primitive cores are unnecessary for Target A.

## Endpoint-Change Patterns

Fix a finite quotient

```text
theta:L_X -> M.
```

Let

```text
S_M=M x X x M.
```

For

```text
s=(a,x,b) in S_M
```

write

```text
delta_s=d_{a,x,b} in C_M(X).
```

For a word

```text
w=(x_1,...,x_n) in X^n,
```

define its `i`-th contextual endpoint symbol by

```text
epsilon_i^M(w)=(a_i,x_i,b_i) in S_M,
```

where the contexts are computed in `M`:

```text
a_i=theta(lambda_{x_1}...lambda_{x_{i-1}}),
b_i=theta(lambda_{x_{i+1}}...lambda_{x_n}).
```

Then

```text
Theta_n^M(w)_i=delta_{epsilon_i^M(w)}.
```

An endpoint-change pattern is a triple

```text
(M,s,t),  s,t in S_M.
```

It is finite-rack separable if there exists a finite rack quotient

```text
phi:C_M(X) -> Y
```

such that

```text
phi(delta_s) != phi(delta_t).
```

A bad pair

```text
(a,beta a)
```

realizes `(M,s,t)` if for some coordinate `i`,

```text
epsilon_i^M(a)=s,
epsilon_i^M(beta a)=t.
```

## Primitive Endpoint-Change Basis

The precise Target A theorem is:

```text
Primitive endpoint-change finite-basis theorem.

There exist finitely many finite-rack separable endpoint-change patterns
(M_j,s_j,t_j), j=1,...,k, such that every kernel-fiber bad pair realizes at
least one of them.
```

This theorem implies finite rack absorption.  For each `j`, choose a finite
rack quotient

```text
phi_j:C_{M_j}(X) -> Y_j
```

with

```text
phi_j(delta_{s_j}) != phi_j(delta_{t_j}).
```

Let

```text
M=M_1 x ... x M_k.
```

For each `j`, the projection `M -> M_j` induces a rack homomorphism

```text
C_M(X) -> C_{M_j}(X),
d_{a,x,b} -> d_{pr_j(a),x,pr_j(b)}.
```

Pull back each `phi_j` along this map and take the product finite rack

```text
Y=Y_1 x ... x Y_k.
```

The resulting detector

```text
D=(M,phi:C_M(X)->Y)
```

separates every bad pair: if a bad pair realizes `(M_j,s_j,t_j)`, the
`j`-th coordinate separates it.

Conversely, if one finite detector

```text
D=(M,phi:C_M(X)->Y)
```

separates all bad pairs, then the finite set

```text
P_D={
  (M,s,t):
  s,t in S_M,
  phi(delta_s) != phi(delta_t)
}
```

is a finite endpoint-change basis.  Every bad pair separated by `D` has

```text
Lambda_n^D(a) != Lambda_n^D(beta a),
```

so some coordinate differs, hence realizes a pattern in `P_D`.

Therefore:

```text
Primitive endpoint-change finite basis
iff
direct finite contextual rack absorption.
```

If a multi-coordinate tuple is separated by a finite rack detector, then some
coordinate is already separated.  Thus multi-coordinate primitive cores do not
add anything for Target A.

## Bounded Arity Obstruction

A bounded-arity theorem would say that every kernel-fiber bad pair has a
detector-separable bad core involving at most `N=N(X)` strands, and that
separation of the reduced pair forces separation of the original pair.

Current status:

```text
open; not supplied by local YBE identities.
```

A serious obstruction pattern is Brunnian kernel-fiber monodromy.  One could
have braids

```text
beta_n in K_n(P_X)
```

such that:

```text
1. beta_n acts nontrivially on some fiber F_p subset X^n;
2. deleting any strand makes the induced action trivial or detector-invisible;
3. the nontriviality depends on all n observer strands.
```

Such a bad pair has no bounded-arity subcore.  Pure braid groups contain
Brunnian braids of arbitrarily large support, and for rack shadows `P_X`, the
groups `K_n(P_X)` may contain pure-braid-like stabilizers.  Local YBE
identities do not rule out a lift to `X^n` detecting such a Brunnian element
only globally.

Thus a bounded-arity theorem would require a new YBE-specific result:

```text
No actual kernel-fiber bad monodromy can be Brunnian of unbounded support.
```

## Bounded Braid Complexity

A bounded braid-complexity theorem would say there is `L=L(X)` such that
every bad pair `(a,beta a)` admits another bad representative `(a,gamma a)`
with

```text
gamma in K_n(P_X),  |gamma| <= L,
```

and whose separation forces separation of `(a,beta a)`.

Current status:

```text
open and probably too strong without extra structure.
```

For fixed `n`, the image of `B_n` in `Sym(X^n)` is finite, so every
nontrivial action has a shortest braid representative.  But `|X^n|` grows
with `n`, and there is no uniform bound on the Cayley diameter of these finite
images.

Mechanisms forcing word length growth include:

```text
pure braids A_{1n},
full twists Delta_n^2,
Brunnian commutators.
```

Even though `K_n(P_X)` has finite index in `B_n` for each fixed `n`, this gives
no uniform finite word bound over all `n`.

The needed theorem would be:

```text
every nontrivial K_n(P_X)-action on X^n has a uniformly short
detector-relevant representative.
```

No known YBE identity gives this.

## Finite-Index Contextual Myhill-Nerode

A useful theorem would give a finite-index equivalence relation on all
orbit-relevant contextual braid states, stable under braid generators and
contextual extension, distinguishing bad states from their bases, and realized
by a finite rack quotient of some `C_M(X)`.

Current status:

```text
open; ordinary Myhill-Nerode theory does not apply.
```

The arity varies, the braid group varies, and contextual states involve
products in quotients of `L_X`.  For fixed `M`, the endpoint-level finite-index
approximation is the residual endpoint quotient `E_M`, and under the harmful
hypothesis `E_M` collapses actual bad pairs.

To go beyond `E_M`, one needs extra state such as path or holonomy state.  To
remain Target A, this extra state must be realized by a finite rack quotient.

The missing theorem is:

```text
reachable contextual holonomy has a finite-index quotient that is
rack-realizable and uniformly separates all bad pairs.
```

## Context-Stable Clopen Endpoint Cylinders

Let

```text
hat{S}=hat{L_X} x X x hat{L_X}
```

be the profinite contextual endpoint alphabet.  A finite quotient `M` gives
clopen cylinders in `hat{S}`.  A detector-separated endpoint cylinder is
determined by finite `M` and endpoint symbols `s,t in S_M` such that some
finite rack quotient separates `delta_s,delta_t in C_M(X)`.

A context-stable clopen core theorem, in the sharpened one-coordinate form,
would say:

```text
There exist finitely many detector-separated endpoint cylinders
C_1,...,C_k subset hat{S} x hat{S}
such that every kernel-fiber bad pair has some coordinate endpoint change in
one of the C_i.
```

This is exactly the topological form of the primitive endpoint-change finite
basis.

Current status:

```text
open; compactness does not prove it.
```

If no finite detector separates all bad pairs, there is a harmful ultrafilter
`U` containing all bad sets `B_D`.  If a cylinder `C` is separated by `D`, then

```text
C cap B_D=empty,
```

so `C notin U`.  Compactness does not force a detector-separated clopen
cylinder into a harmful ultrafilter.  A finite clopen cover theorem requires a
new YBE-specific mechanism, such as:

```text
Noetherianity of reachable bad endpoint changes,
bounded Brunnian rank,
finite generation of harmful holonomy as a rack-visible ideal,
deletion/contraction theorem for kernel-fiber monodromy.
```

## Uniform Reachable Escape-Holonomy Separation

An actual bad pair `(a,beta a)` can be viewed as nontrivial holonomy in a
kernel fiber over `P_X^n`.  A holonomy separation theorem would say:

```text
Every actual nontrivial K_n(P_X)-holonomy is detected by finite rack-valued
contextual holonomy, and finitely many such finite rack quotients detect all
actual bad pairs.
```

Uniformity is essential.  Pointwise separability says every bad pair has some
detector.  Target A requires one detector for all bad pairs.

Holonomy data solves Target A only if it becomes a finite rack quotient of
some `C_M(X)`.  If the holonomy state is not expressible as endpoint generator
labels satisfying contextual rack relations, it is not a finite contextual
rack detector.

Current status:

```text
promising, but only if one proves uniform rack-valued realization.
```

Otherwise holonomy is diagnostic.

## Structure Of K_n(P_X)

Since `P_X` is finite, `B_n` has finite image on `P_X^n`, so

```text
K_n(P_X)=ker rho_n^{P_X}
```

has finite index in `B_n`.

A useful theorem would say that the tower

```text
K_bullet(P_X)={K_n(P_X)}
```

has a uniform finite basis of detector-relevant moves, stable under spectator
insertion, conjugation, and contextual extension.

Current status:

```text
open; finite index for each n is not enough.
```

Pure and Brunnian braid phenomena can have complexity growing with `n`.  Even
bounded abstract generation of `K_n(P_X)` would not automatically give bounded
contextual detection, because the lifted `X`-action may depend on intervening
observer contexts.

The missing ingredient would be:

```text
bounded-support generation compatible with X-fiber monodromy and contextual
rack separability.
```

## Failure Data And Target B

Failure of the primitive endpoint-change finite-basis theorem means:

```text
For every finite family of finite-rack separable endpoint-change patterns,
there is an actual bad pair avoiding all of them.
```

Equivalently, there is a harmful ultrafilter on actual bad pairs avoiding
every detector-separated endpoint cylinder.

This failure data is generally profinite and non-coordinatewise.  It does not
automatically produce Target B.

To produce Target B, one would need finite non-rack coordinate labels

```text
pi_{a,b}:X -> Z
```

that:

```text
1. separate some finite-rack-invisible endpoint pair;
2. define a functional and cofunctional crossing relation;
3. extend to a total bijection r_Z:Z^2 -> Z^2;
4. satisfy YBE on all of Z^3;
5. give globally orbit-injective Pi_n.
```

None of these follows merely from failure of Target A.  The failure can remain
purely profinite and non-coordinatewise.

## Conditional Finite Extraction Theorem

The strongest valid theorem is conditional.

Branch A: finite endpoint-change basis.  If finitely many finite-rack
separable endpoint-change patterns cover all kernel-fiber bad pairs, then one
finite contextual rack detector separates all bad pairs.  Hence a finite rack
dominates `X`.

Branch B: independent proper active descent.  If there are finite data

```text
M, Z, r_Z, pi_{a,b}
```

with `|Z|<|X|`, `r_Z` total bijective YBE, contextual compatibility, and
globally orbit-injective `Pi_n`, then

```text
ker rho_n^Z <= ker rho_n^X.
```

If every smaller finite YBE solution is rack-dominated, then `X` is
rack-dominated.

The missing theorem is the unconditional assertion that Branch A or Branch B
always holds.

## Next Actionable Target

The best Target A sublemma is:

```text
Finite endpoint-change cover theorem.
The set of all kernel-fiber bad pairs is covered by finitely many finite-rack
separable one-coordinate contextual endpoint-change cylinders.
```

Equivalently:

```text
There is no harmful ultrafilter on actual bad pairs that avoids every
finite-rack separable endpoint-change cylinder.
```

A structural version is:

```text
No Brunnian harmful ultrafilter theorem.
Actual harmful kernel-fiber monodromy cannot remain invisible to all
finite-rack endpoint changes by escaping through unbounded observer-strand or
Brunnian configurations.
```

This is the most actionable next theorem because it directly attacks the
obstruction created by residual endpoint failure while staying inside Target
A.

Target B remains secondary unless one discovers explicit non-rack coordinate
data.  Failure of Target A alone does not automatically produce such data.
