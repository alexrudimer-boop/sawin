# Fixed-M Endpoint Finiteness Boundary

Date: 2026-06-05

This note records the refinement after the orbit-relevance audit.  Factorial
holonomy may occur in the ambient associated group `As(C_M(X))`, but for a
fixed finite state quotient `M`, actual endpoint contextual labels of
`Theta_n^M` lie in a finite set.

Therefore the shift-rack-style factorial obstruction cannot appear as a
fixed-`M` endpoint-label obstruction.  It can appear only as ambient holonomy,
hidden path holonomy, exact finite-symbolic collisions in unbounded arity, or
through unbounded refinement of the finite state quotient.

The remaining possible obstruction is:

```text
unbounded arity/refinement escape of exact finite contextual labels or hidden
path holonomy, not fixed-M endpoint factoriality.
```

## Fixed-M Endpoint Finiteness

Fix a finite quotient

```text
theta:L_X -> M.
```

Let

```text
S_M={d_{a,x,b}:a,b in M, x in X} subset C_M(X).
```

This set is finite.

For every arity `n` and every word

```text
x=(x_1,...,x_n) in X^n,
```

the contextual label tuple satisfies

```text
Theta_n^M(x) in S_M^n.
```

Thus actual endpoint labels appearing in contextual words are drawn from the
finite generator set `S_M`, not from the whole infinite rack `C_M(X)`.

This is the key difference from the shift-rack factorial obstruction, whose
force comes from the infinitely many endpoint elements

```text
0, 1!, 2!, 3!, ...
```

in the shift rack.

## Finite Rack Separation Of The Endpoint Set

Suppose every distinct pair `r,s in S_M` is separated by some finite rack
quotient of `C_M(X)`.  Then there is a single finite rack quotient

```text
phi_M:C_M(X) -> Y_M
```

that is injective on `S_M`.

Indeed, for every ordered pair `r != s` in the finite set `S_M`, choose a
finite rack quotient

```text
phi_{r,s}:C_M(X) -> Y_{r,s}
```

with `phi_{r,s}(r) != phi_{r,s}(s)`.  Take the finite product over all such
pairs.

Consequently,

```text
phi_M^n Theta_n^M(x)=phi_M^n Theta_n^M(x')
```

iff

```text
Theta_n^M(x)=Theta_n^M(x')
```

as tuples in `S_M^n`.

Once `M` is fixed and `S_M` is finite-rack separated, all remaining bad pairs
are exact equality failures of the finite-state contextual label map
`Theta_n^M`.  They are not fixed-`M` factorial endpoint phenomena.

## Transporter Version

Let

```text
R=C_M(X),
G=As(R).
```

For `r in R`, let

```text
H_r=Stab_G(r).
```

Suppose actual braid trajectories give transporters `g_j in G` from a fixed
initial contextual label `r in S_M` to endpoint labels

```text
s_j=g_j.r in S_M.
```

Since `S_M` is finite, on an infinite subsequence or ultrafilter-large set the
endpoint is constant:

```text
s_j=s.
```

Choose one transporter `g_0` with `g_0.r=s`.  Then every such `g_j` lies in
the coset

```text
g_0 H_r.
```

If the endpoint pair `r,s` is separated by a finite rack quotient, then the
same finite rack quotient separates every transporter in the family from acting
like a stabilizer at `r`: every element of `H_r` fixes `r`, while every
transporter in `g_0H_r` sends `r` to `s`.

Thus:

```text
For fixed M, endpoint-relevant transporter nonuniformity cannot be factorial
if endpoint pairs in S_M are pointwise separable.
```

A factorial family can matter only as hidden path holonomy in the stabilizer
or through varying/refining the state quotient `M`.

## One-Point Free-Quandle Example Is Ambient

For the one-point solution

```text
X={*},
r(*,*)=(*,*),
```

and finite cyclic quotient `M=C_m`, the contextual rack is the free quandle on
generators `e_0,...,e_{m-1}`.  Thus

```text
As(C_M(X)) ~= F_m
```

and ambient factorial families exist in the associated group.

But actual contextual labels in arity `n` are much smaller.  Writing

```text
d_{i,j}=d_{t^i,*,t^j},
e_s=d_{i,j}, s=i+j mod m,
```

one has

```text
Theta_n^M(*,...,*)_i
=
d_{t^{i-1},*,t^{n-i}}
=
e_{n-1 mod m}.
```

So every coordinate has the same label:

```text
Theta_n^M(*,...,*)=(e_s,...,e_s).
```

The ambient transporter family `g_1^{n!}` acting on `e_0` is not reached by
actual one-point contextual braid dynamics.  The only reachable labels are
diagonal and fixed.  Moreover,

```text
Omega_n=empty
```

for every `n`.  Hence the example is harmless.

## Product And Padding

If

```text
X={*} x Z,
```

then `X` is just `Z` as a YBE solution.  The one-point free-quandle holonomy
does not add an active component.

If

```text
X=E_triv x Z
```

with `E_triv` having trivial braid action, then

```text
rho_n^X = id_{E^n} x rho_n^Z,
ker rho_n^X = ker rho_n^Z.
```

So the projection to `Z` is kernel-reflecting.  Any holonomy living purely in
the padding factor is inert.  If `E_triv` is nontrivial, `Z` is a proper
domination-equivalent active factor, so such `X` is not residual-rigid.

Product padding cannot create a new minimal harmful obstruction once the
factors are solved.

## Reachability Conditions

For a group element `g in As(C_M(X))` to be endpoint-reachable from
`r in S_M` to `s in S_M`, there must be:

```text
n,
x in X^n,
beta in B_n,
x'=rho_n^X(beta)x,
```

and a marked strand such that:

```text
initial contextual label = r,
final contextual label = s,
escape cocycle = g,
s=g.r.
```

Therefore a family `g_j=h^{j!}` with `h^{j!}.r` taking infinitely many
distinct values in `C_M(X)` is not endpoint-relevant for fixed `M`.  It can be
orbit-relevant only if, on an ultrafilter-large set, the endpoint is a fixed
`s in S_M`, or if `M` itself varies.

If `s != r` and `r,s` are finite-rack separable, the finite-endpoint lemma
uniformly separates the family.  If `s=r`, then the transporters lie in the
stabilizer and represent pure path holonomy rather than endpoint discrepancy.

Hence:

```text
For fixed M, a factorial transporter can be harmful only as hidden path
holonomy, not as endpoint label variation, unless a fixed generator pair is
already nonseparable.
```

## Harmful Bad-Pair Ultrafilters

To produce a harmful bad-pair ultrafilter, a transporter sequence is not
enough.  One needs actual same-orbit pairs

```text
omega_j=(x^(j),x'^(j)) in Omega_{k_j}
```

such that for every finite detector `D`,

```text
omega_j in B_D
```

on an ultrafilter-large set.

For fixed `M`, after finite-rack separating `S_M`, every remaining bad pair
satisfies

```text
Theta_n^M(x^(j)) = Theta_n^M(x'^(j))
```

on an ultrafilter-large set.

Therefore harmfulness is not a fixed-`M` factorial endpoint problem.  What
remains can still have two forms:

```text
fixed-M unbounded arity:
  exact Theta^M-label collisions persist in arbitrarily large arities;

state-refinement escape:
  every fixed finite M is eventually defeated, so finer and finer state
  quotients are needed.
```

Hidden stabilizer/path holonomy can also remain as profinite escape data, but
it is not detected by fixed-`M` endpoint variation after `S_M` is separated.

## Active Extraction Is Still Not Automatic

If actual same-orbit bad pairs with escape holonomy `h^{n!}` are somehow
constructed, finite active extraction remains nontrivial.  A finite active
factor requires finite `M`, finite `Z`, maps

```text
pi_{a,b}:X -> Z,
```

and a total bijective YBE map `r_Z:Z^2 -> Z^2` satisfying functionality,
totality, cofunctionality, YBE on all triples, braid equivariance, and kernel
reflection

```text
ker rho_n^Z <= ker rho_n^X.
```

Factorial holonomy is usually infinite-index.  Any finite `Z` sees the
transporter with finite period, so `h^{n!}` eventually becomes invisible.  If
one forces a finite quotient, extraction may still fail by nonfunctionality,
partiality, nonbijectivity, YBE failure on unreached triples, or loss of
orbit-injectivity.

Residual rigidity excludes only proper finite active factors with the correct
kernel direction.  It does not remove purely profinite holonomy.

## Escape Holonomy As Diagnostic

The escape action groupoid should have objects given by reachable pointed
contextual labels, for example pairs `(x,i)` with `x in X^n`, together with
their labels

```text
kappa_i^M(x)=d_{a_i,x_i,b_i} in S_M.
```

Morphisms are generated by braid moves following a marked strand through a
braid trajectory.  There is a functor to the action groupoid of
`As(C_M(X))` acting on `C_M(X)`.

This separates ambient holonomy from reachable holonomy.  In the one-point
example, `As(C_M(X))` contains `g_1^{n!}`, but the reachable escape groupoid
sees only diagonal labels and stabilizer holonomy.

Escape holonomy compresses to finite rack labels precisely when relevant
transporter cosets are uniformly separated:

```text
closure(T) cap closure(H)=empty.
```

If this fails, escape holonomy remains genuinely profinite.

## Current Missing Lemma

The fixed-`M` endpoint-finiteness lemma shows that the remaining obstruction is
not ambient factorial endpoint holonomy in a fixed contextual rack.  It is:

```text
Can a harmful ultrafilter escape fixed finite endpoint control through
unbounded arity exact contextual-label collisions, state-refinement escape, or
hidden profinite path holonomy that is not active-factor extractable?
```

Equivalently, the sharp missing lemma is:

```text
Every orbit-relevant profinite escape-holonomy collapse is either
finite-state/rack-absorbed or yields a proper finite active factor.
```

This remains strictly smaller than Sawin and is the exact point where the
contextual tower still needs new input.
