# Residual Endpoint Orbit-Injectivity Obstruction

Date: 2026-06-05

This note records a negative result for a tempting finite extraction strategy.
The maximal finite-rack residual endpoint system for a fixed finite state
quotient `M` cannot, under the no-detector hypothesis, be promoted through a
quotient or totalization into an orbit-injective active factor.  The
obstruction is already present before totality or YBE on unreached triples:

```text
failure of global orbit-injectivity.
```

## Maximal Fixed-M Residual Endpoint System

Fix a finite quotient

```text
theta:L_X -> M.
```

Let

```text
S_M=M x X x M
```

be the finite set of contextual endpoint symbols.  Write

```text
delta_{a,x,b}=d_{a,x,b} in C_M(X).
```

Define an equivalence relation `equiv_M` on `S_M` by

```text
(a,x,b) equiv_M (a',x',b')
```

if and only if every finite rack quotient

```text
phi:C_M(X) -> Y
```

identifies the corresponding endpoint generators:

```text
phi(d_{a,x,b})=phi(d_{a',x',b'}).
```

Let

```text
E_M=S_M/equiv_M,
eta_M:S_M -> E_M
```

be the quotient.  This is the finite endpoint system seen by all possible
finite rack quotients of `C_M(X)` on the endpoint generators.

## Realization By One Finite Rack Detector

Since `S_M` is finite, there are only finitely many endpoint-symbol pairs.
For every pair

```text
s,t in S_M,  s not equiv_M t,
```

there is a finite rack quotient

```text
phi_{s,t}:C_M(X) -> Y_{s,t}
```

with

```text
phi_{s,t}(delta_s) != phi_{s,t}(delta_t).
```

Taking the finite product

```text
Y_M=prod_{s not equiv_M t} Y_{s,t}
```

and the product map

```text
Phi_M:C_M(X) -> Y_M
```

gives one finite rack detector such that, on endpoint generators,

```text
Phi_M(delta_s)=Phi_M(delta_t)
iff
s equiv_M t.
```

Thus

```text
D_M=(M,Phi_M)
```

is the strongest fixed-`M` finite contextual rack detector as far as endpoint
generators are concerned.

## No-Detector Hypothesis Forces Non-Orbit-Injectivity

Assume:

```text
No finite contextual rack detector separates every kernel-fiber bad pair.
```

Apply this to the finite detector `D_M=(M,Phi_M)`.  Since `D_M` fails, there
exist

```text
n >= 1,
beta in K_n(P_X),
a in X^n
```

such that

```text
beta a != a
```

but

```text
Phi_M^n Theta_n^M(beta a)=Phi_M^n Theta_n^M(a).
```

Because `Phi_M` realizes the finite-rack residual endpoint quotient, equality
under `Phi_M` on endpoint generators is exactly equality in `E_M`.  Hence

```text
eta_M^n Theta_n^M(beta a)=eta_M^n Theta_n^M(a).
```

Define

```text
Pi_n^{E_M}:X^n -> E_M^n
```

by

```text
Pi_n^{E_M}(x_1,...,x_n)_i =
eta_M(a_i,x_i,b_i),
```

where the contextual states are computed in `M`:

```text
a_i=theta(lambda_{x_1}...lambda_{x_{i-1}}),
b_i=theta(lambda_{x_{i+1}}...lambda_{x_n}).
```

Then the bad pair above gives

```text
Pi_n^{E_M}(beta a)=Pi_n^{E_M}(a),
```

while

```text
beta a in B_n.a,
beta a != a.
```

Therefore `Pi_n^{E_M}` is not globally orbit-injective.

Thus, for every finite `M`, the strongest finite-rack observable endpoint
system collapses some actual same-orbit bad pair whenever no finite detector
works.

## Quotients Cannot Repair The Collapse

Let

```text
q:E_M -> Z
```

be any map, in particular any quotient map used in a proposed totalization.
Define

```text
pi_{a,b}(x)=q(eta_M(a,x,b)).
```

Then

```text
Pi_n^Z=q^n Pi_n^{E_M}.
```

For the bad pair found above,

```text
Pi_n^{E_M}(beta a)=Pi_n^{E_M}(a),
```

so automatically

```text
Pi_n^Z(beta a)=Pi_n^Z(a).
```

Since `beta a != a` and `beta a` is in the braid orbit of `a`, the maps
`Pi_n^Z` are not orbit-injective.

Therefore:

```text
No quotient of the finite residual contextual endpoint system can be
orbit-injective.
```

Adding a total bijective YBE operation on `Z^2`, even if possible, cannot
restore information that the endpoint map has already lost.  Totality,
cofunctionality, bijectivity, and YBE on unreached triples do not resurrect
the collapsed actual bad pair.

## Disproved Extraction Principle

The following implication is false as a finite residual endpoint extraction
principle:

```text
No finite contextual rack detector separates all bad pairs

=> some finite residual contextual endpoint system, or quotient of it,
   totalizes to a strictly proper orbit-injective Yang-Baxter factor.
```

The antecedent implies the opposite for every fixed finite `M`: the maximal
finite-rack residual endpoint system for that `M` collapses an actual
kernel-fiber bad pair.

So the attempted extraction fails at:

```text
global orbit-injectivity.
```

Other possible failures remain real:

```text
no canonical finite M,
residual endpoint classes need not be closed under rack operations,
partial contextual crossing need not totalize,
YBE on unreached triples is not forced.
```

But even if those issues were repaired, any construction factoring through
the residual finite-rack endpoint quotient would still fail orbit-injectivity.

## Valid Conditional Active-Factor Theorem

The valid theorem is conditional.

Assume one is independently given finite data

```text
Z,
r_Z:Z^2 -> Z^2,
M,
pi_{a,b}:X -> Z
```

such that:

```text
1. r_Z is a finite bijective YBE solution;
2. contextual compatibility holds;
3. the induced maps Pi_n:X^n -> Z^n are globally orbit-injective.
```

The compatibility condition is that whenever `r_X(x,y)=(u,v)`,

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

Define

```text
Pi_n(x_1,...,x_n)_i=pi_{a_i,b_i}(x_i).
```

Then the maps `Pi_n` are braid-equivariant.  For a generator `sigma_i`, write

```text
x_i=x, x_{i+1}=y, r_X(x,y)=(u,v),
a=lambda_{x_1}...lambda_{x_{i-1}},
b=lambda_{x_{i+2}}...lambda_{x_n}.
```

Before applying `sigma_i`, the two relevant labels are

```text
pi_{a,lambda_y b}(x),
pi_{a lambda_x,b}(y).
```

After applying `sigma_i`, they are

```text
pi_{a,lambda_v b}(u),
pi_{a lambda_u,b}(v).
```

Contextual compatibility says these are related by `r_Z`.  All other
coordinates have unchanged contexts because in `M`

```text
lambda_x lambda_y=lambda_u lambda_v.
```

Thus

```text
Pi_n(sigma_i a)=sigma_i Pi_n(a).
```

Bijectivity gives the inverse generator relation, so

```text
Pi_n(beta a)=beta Pi_n(a)
```

for every braid `beta`.

If `beta in ker rho_n^Z`, then

```text
Pi_n(beta a)=beta Pi_n(a)=Pi_n(a)
```

for every `a in X^n`.  Since `beta a` lies in the braid orbit of `a`,
global orbit-injectivity gives

```text
beta a=a.
```

Hence `beta` fixes all of `X^n`, so

```text
beta in ker rho_n^X.
```

Therefore

```text
ker rho_n^Z <= ker rho_n^X
```

for every `n`.

## Exact Additional Hypothesis

To make active extraction valid, one must add an independent hypothesis:

```text
There exists a finite quotient M, a finite set Z with |Z|<|X|, maps
pi_{a,b}:X -> Z, and a total bijective YBE map r_Z:Z^2 -> Z^2, such that
contextual compatibility holds and the induced maps Pi_n are globally
orbit-injective.
```

Without this added hypothesis, failure of uniform finite contextual rack
detection only gives collapsed bad pairs in every finite residual
rack-observable endpoint system.  It does not produce an orbit-injective
proper active factor.

## Boundary

The finite residual endpoint quotient `E_M` is useful for understanding what
finite rack endpoint detectors can see, but under the no-detector hypothesis
it is guaranteed not to be orbit-injective.

Thus any successful extraction theorem must use additional information not
factoring through the already-collapsed residual endpoint system, or it must
prove finite rack absorption directly.  The missing input is no longer merely
totalization.  It is the independent creation of a globally orbit-injective,
contextually compatible finite active factor.
