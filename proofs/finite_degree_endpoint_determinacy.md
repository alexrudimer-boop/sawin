# Finite-Degree Endpoint Determinacy

Date: 2026-06-04

This note records the sharpened endpoint fork from the same-chat Pro
separation query.  It does not prove finite-rack domination and it does not
give a counterexample.  It isolates the first finite-degree lemma whose proof
would close the positive endpoint route, and whose cofinal failure gives an
implementable search for a normalized-law no-rack sequence.

## Setup

Fix one actual completed-context interval `I`.  Let

```text
A = Art_I
```

be the universal Artin row group of the interval.  For `s >= 1`, let

```text
q_s : A -> A_s
```

be the product of all finite quotients of `A` of order at most `s`.  This is a
finite quotient: enumerate finite group tables of order at most `s`, enumerate
assignments of the generators of `A`, and retain the assignments satisfying the
Artin row relations.

For arity `n` and base context `c`, let `L_n(c)` be the actual residual branch
loop group.  It has readouts

```text
alpha_n : L_n(c) -> A^{T_n},
epsilon_n : L_n(c) -> U,
```

where `U` is the finite endpoint unit group.  For every survivor subset
`J subset {1,...,n}`, actual deletion gives

```text
d_J : L_n(c) -> L_J(d_J c),
```

compatible with both readouts.

## Finite Profile

For a branch

```text
gamma in L_n(c),
```

define its `(s,N)` deletion profile by

```text
Theta_{s,N}(gamma)
  =
  (
    q_s^{T_n} alpha_n(gamma),
    (
      q_s^{T_J} alpha_J(d_J gamma),
      epsilon_J(d_J gamma)
    )_{|J| <= N}
  ).
```

The full endpoint `epsilon_n(gamma)` is deliberately not part of this profile.

## Determinacy Lemma

The decisive positive lemma is:

```text
Finite-degree endpoint determinacy.

For every actual interval I, there exist integers

  s = s(I),      N = N(I)

such that, for every arity n, every base context c, and every pair of actual
branches gamma, delta in L_n(c),

  Theta_{s,N}(gamma) = Theta_{s,N}(delta)

implies

  epsilon_n(gamma) = epsilon_n(delta).
```

Equivalently, for all `n,c`, the endpoint map factors through the finite
deletion profile:

```text
epsilon_n = bar_epsilon_{n,c} o Theta_{s,N}.
```

This is stronger than bare profinite endpoint separation.  It says that after
passing to one finite Artin quotient and all deletion shadows of one bounded
width, the endpoint has bounded degree.

The same-chat Pro follow-up sharpened the first proof obligation further in
`proofs/vertical_kernel_endpoint_lemma.md`.  It is enough to prove this
determinacy only on the one-strand Fadell-Neuwirth vertical kernels
`ker(d_hat_n:L_n(c)->L_{n-1}(d_hat_n c))`; the full lemma then follows by
induction, lifting the lower-arity branch by a straight last strand and
applying the vertical statement to the quotient branch
`gamma tilde_gamma^{-1}`.

## Why It Implies Endpoint Separation

Assume the lemma.  Let `u in U`, `u != 1`, and set `q=q_s`.

Suppose there is an actual branch `gamma in L_n(c)` with

```text
epsilon_n(gamma) = u,
q^{T_n} alpha_n(gamma) = 1,
(
  q^{T_J} alpha_J(d_J gamma),
  epsilon_J(d_J gamma)
) = 1
for every |J| <= N.
```

Let `1_c in L_n(c)` be the trivial branch.  Then

```text
Theta_{s,N}(gamma) = Theta_{s,N}(1_c).
```

By endpoint determinacy,

```text
epsilon_n(gamma) = epsilon_n(1_c) = 1,
```

contradicting `u != 1`.  Thus no endpoint-`u` Artin-null Brunnian branch
survives after the fixed finite quotient `q_s` and width `N`.

If the determinacy lemma holds for every actual interval, the finite
Artin-null endpoint separation theorem follows, and the existing local rack
assembly supplies finite-rack domination.

## Finite Failure Computation

The same-chat Pro follow-up made the fixed-parameter computation completely
actual.  A finite search seed is not a formal partial row system; it is a
finite actual interval

```text
I = (X, r, C, tau, G, U, eta).
```

Here `X` is a finite set, `r:X^2 -> X^2` is a bijective YBE table, `C` is a
finite context set, and each `x in X` has a context transition
`tau_x:C -> C` satisfying the structure relation

```text
r(x,y)=(u,v)  =>  tau_x tau_y = tau_u tau_v.
```

The retained germs are `G subset C x X`.  A retained adjacent pair has the
form

```text
e = (s,x),        f = (s tau_x,y),
```

and if `r(x,y)=(u,v)` its actual row is

```text
B(e,f) = ((s,u),(s tau_u,v)).
```

The retained set is required to be closed under all supported rows and inverse
rows.  The finite endpoint group is `U`, and each supported positive row has
an endpoint label `eta(e,f) in U`; inverse rows use the inverse labels.  These
labels must satisfy the endpoint cube cocycle equation on every supported
actual YBE cube, so the endpoint readout descends from braid words to actual
residual branches.

The Artin row group attached to this actual interval has generators
`a_e,l_e` for `e in G` and, for every actual row `B(e,f)=(e',f')`, the row
relations

```text
a_{e'} = a_e a_f a_e^-1,     l_{e'} = a_e l_f,
a_{f'} = a_e,                l_{f'} = l_e.
```

For fixed quotient degree `s`, the finite group `A_s` can be computed by
enumerating all finite groups of order at most `s`, enumerating assignments of
the generators `a_e,l_e` into those groups, retaining exactly the assignments
satisfying the row relators, and comparing values in the resulting finite
evaluation product.

For fixed parameters `I,s,N,n,c`, define the finite decorated image

```text
G_{I,s,N,n,c}
  =
  im(
    L_n(c) ->
    A_s^{T_n} x U x
    prod_{|J| <= N}(A_s^{T_J} x U)
  ),
```

where a branch `gamma` is sent to

```text
(
  q_s^{T_n} alpha_n(gamma),
  epsilon_n(gamma),
  (
    q_s^{T_J} alpha_J(d_J gamma),
    epsilon_J(d_J gamma)
  )_{|J| <= N}
).
```

Let `Pi_{s,N}` be the projection that forgets only the full endpoint
coordinate `epsilon_n(gamma)`.  Define

```text
K_{I,s,N,n,c} = ker(Pi_{s,N} | G_{I,s,N,n,c}).
```

Then finite-degree endpoint determinacy at `(s,N,n,c)` is exactly:

```text
K_{I,s,N,n,c} has trivial endpoint component.
```

Equivalently, determinacy fails at `(s,N,n,c)` if and only if this finite
kernel contains an element represented by an actual branch word `eta` such
that

```text
q_s^{T_n} alpha_n(eta) = 1,
(
  q_s^{T_J} alpha_J(d_J eta),
  epsilon_J(d_J eta)
) = 1
for every |J| <= N,
```

but

```text
epsilon_n(eta) != 1.
```

This is precisely the finite-level Artin-null Brunnian endpoint obstruction.

## Labelled Graph Certificate

For fixed `I,s,N,n,c`, build a finite labelled residual graph.

A residual state is a composable retained germ word

```text
e = (e_1,...,e_n),       e_i=(s_i,x_i),
s_1=c,                  s_{i+1}=s_i tau_{x_i}.
```

To track deletion functorially, use moving strand IDs.  A full vertex contains

```text
v = (e, pi, (e_J, pi_J)_{1 <= |J| <= N}),
```

where `pi` records the current order of the original strand IDs, and
`(e_J,pi_J)` is the corresponding deleted residual state for survivor set
`J`.  A supported generator `sigma_i^{+/-1}` updates the full state by the
actual row or inverse row.  In the `J`-deleted component:

```text
if neither or exactly one crossed moving ID lies in J:
    the J-component sees no crossing;
if both crossed moving IDs lie in J:
    apply the corresponding adjacent generator in the current deleted order.
```

This is the standard braid deletion map written in moving-strand labels.

Let

```text
D_{s,N,n}
  =
  A_s^{T_n} x U x
  prod_{1 <= |J| <= N}(A_s^{T_J} x U).
```

Each directed edge carries a label in `D_{s,N,n}`:

```text
(
  q_s^{T_n} lambda_i^{+/-}(e),
  mu_i^{+/-}(e),
  (
    q_s^{T_J} lambda_{J,i}^{+/-}(e_J),
    mu_{J,i}^{+/-}(e_J)
  )_J
).
```

If the crossing disappears under deletion to `J`, its `J`-label is `(1,1)`.
The graph includes both positive and inverse lifted braid moves, so it is
inverse-closed as a labelled graph over the finite group `D_{s,N,n}`.

Actual residual branch loops based at `(n,c)` are exactly loops at the base
vertex `v_0`.  Let

```text
Lambda_{I,s,N,n,c} <= D_{s,N,n}
```

be the subgroup of labels of all such loops.  It is computed by the standard
spanning-tree cycle closure:

1. Compute the reachable component of `v_0`.
2. Choose a spanning tree and store the tree path label `p_v` from `v_0` to
   each vertex `v`.
3. For every directed edge `e:v -> w` with label `ell(e)`, add the cycle label

```text
p_v ell(e) p_w^-1
```

to a generator list.
4. The subgroup generated by these cycle labels is exactly
   `Lambda_{I,s,N,n,c}`.

The generic finite-group helper
`labelled_loop_subgroup_audit(...)` implements this last graph-theoretic step
for inverse-closed finite labelled graphs.

Define the endpoint witness subgroup

```text
H_{I,s,N,n,c}
  =
  { u in U : (1,u,(1,1)_J) in Lambda_{I,s,N,n,c} }.
```

Then

```text
u in H_{I,s,N,n,c}
```

if and only if there is an actual residual branch loop `gamma in L_n(c)` with

```text
epsilon_n(gamma) = u,
q_s^{T_n} alpha_n(gamma) = 1,
q_s^{T_J} alpha_J(d_J gamma) = 1,
epsilon_J(d_J gamma) = 1
for every 1 <= |J| <= N.
```

Thus finite-degree endpoint determinacy for `I` is equivalent to

```text
exists s,N such that for all n,c:
    H_{I,s,N,n,c} = {1}.
```

For fixed `s,N,n,c`, this is a finite graph and finite group computation.

## Executable Search

For fixed `I,s,N,n,c`, the check is finite.

1. Compute `A_s` by enumerating finite groups of order at most `s` and all
   generator assignments satisfying the Artin row relations.

2. Build the deletion-decorated residual branch graph at arity `n` with
   moving strand IDs.

3. Decorate each lifted generator by its full finite Artin readout, its full
   endpoint, and all bounded deletion readouts:

```text
q_s^{T_n} alpha_n,   epsilon_n,
(
  q_s^{T_J} alpha_J,
  epsilon_J
)_{|J| <= N}.
```

4. Compute the based loop-label subgroup `Lambda_{I,s,N,n,c}` by the
   spanning-tree cycle method.

5. Intersect it with the finite endpoint kernel coordinates to compute
   `H_{I,s,N,n,c}`.  If this subgroup contains `u != 1`, output a branch word
   producing `(1,u,(1,1)_J)`.

For fixed parameters there is no hidden infinite braid-group quantifier.

A finite failure certificate is therefore a tuple

```text
Cert = (I,s,N,n,c,u,w)
```

where `u in U`, `u != 1`, and `w` is a word in supported lifted residual
generators such that:

1. `w` starts at the base vertex `v_0` and returns to `v_0`;
2. the full endpoint is `epsilon_n(w)=u`;
3. the full finite Artin readout is trivial:
   `q_s^{T_n} alpha_n(w)=1`;
4. every deletion shadow of width at most `N` has trivial finite Artin readout
   and trivial endpoint.

The certificate is checked entirely inside finite data.  A cofinal negative
seed would be one actual interval `I`, one endpoint `u != 1`, and an effective
procedure that, for every pair `(s,N)`, outputs such a certificate with
parameters `n(s,N),c(s,N)`.

## Negative Diagonal

If, for one actual interval `I` and one nonidentity endpoint `u`, such finite
kernel witnesses persist cofinally as `s,N -> infinity`, then diagonalizing
over finite quotient degree and deletion width gives the normalized-law
no-rack sequence.  Namely, choose witnesses invisible to the first `s`-degree
finite Artin quotients and all `N`-strand deletion profiles, with endpoint
`u != 1`; then stabilize in unused strands as needed.

This is the precise actual-YBE version of the profinite Artin-null Brunnian
obstruction.

## What This Does Not Prove

Finite automata alone do not prove the lemma.  They make the endpoint languages
rational subsets of finitely generated groups, but rational subset
separability is much stronger and fails in broad group-theoretic settings.

Residual finiteness alone also does not prove the lemma.  It detects each
fixed nontrivial braid or endpoint word in some finite quotient, but Sawin's
problem needs one finite rack detector working uniformly across all arities
and all visible branches of `X`.

Thus the missing ingredient is genuinely finite-YBE-specific:

```text
actual YBE locality and deletion structure must force endpoint information to
have bounded finite quotient/deletion degree after one finite Artin quotient.
```

The known fixed-`Q_3` Brunnian pressure for the affine rack
`R(x,y)=(-x+2y,x)` over `F_5` does not refute this lemma, because that example
is itself a rack and hence dominates itself.  It only shows that the finite
quotient/deletion profile cannot be replaced by one fixed small rack detector
such as `Q_3`.

## Fork

The decisive fork is now:

```text
prove finite-degree endpoint determinacy for every actual completed-context
interval
```

or

```text
find one actual finite YBE interval with cofinal finite-kernel witnesses in
K_{I,s,N,n,c}.
```

The first closes the positive route.  The second gives an explicit, executable
negative search target; if the witnesses persist cofinally in `s,N`, they
diagonalize to the required no-rack sequence.

The sharper first local target is the vertical version:

```text
prove H^vert_{I,s,N,n,c}={1} for all n,c after one fixed s,N,
```

where `H^vert` is computed from the deletion-decorated graph generated only by
the last-strand point-pushing generators `A_{i,n}`.  This is recorded in
`proofs/vertical_kernel_endpoint_lemma.md`.
