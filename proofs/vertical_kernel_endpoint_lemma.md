# Vertical-Kernel Endpoint Lemma

Date: 2026-06-04

This note records the same-chat Pro follow-up to
`proofs/finite_degree_endpoint_determinacy.md`.  It does not prove
finite-rack domination and it does not give a counterexample.  It isolates a
smaller Fadell-Neuwirth endpoint theorem whose proof implies finite-degree
endpoint determinacy by induction, and whose cofinal failure gives a more
focused actual search.

## Setup

Fix an actual finite completed-context interval

```text
I = (X,r,C,tau,G,U,eta).
```

Let

```text
A = Art_I
```

be its universal Artin row group.  For `s >= 1`, let

```text
q_s : A -> A_s
```

be the product of all finite quotient images of `A` of order at most `s`.

For arity `n` and base context `c`, write

```text
L_n(c)
```

for the actual residual branch loop group, with readouts

```text
alpha_n : L_n(c) -> A^{T_n},
epsilon_n : L_n(c) -> U.
```

For `n >= 2`, let

```text
d_hat_n : L_n(c) -> L_{n-1}(d_hat_n c)
```

be deletion of the last strand.  Define the one-strand vertical subgroup

```text
V_n(c) = ker d_hat_n.
```

Thus `zeta in V_n(c)` is an actual residual branch loop whose last-strand
deletion is the trivial lower-arity branch.

## Vertical Lemma

The first genuinely decisive local endpoint theorem is:

```text
Vertical-kernel endpoint lemma.

For every actual finite interval I, there exist finite integers s=s(I) and
N=N(I) such that, for every n,c, every vertical loop zeta in V_n(c) satisfying

  q_s^{T_n} alpha_n(zeta) = 1

and

  (q_s^{T_J} alpha_J(d_J zeta), epsilon_J(d_J zeta)) = (1,1)
  for every |J| <= N

also satisfies

  epsilon_n(zeta) = 1.
```

This is strictly smaller than the full endpoint determinacy statement because
it only concerns the Fadell-Neuwirth kernel obtained by forgetting one strand.
It is the actual-YBE analogue of the free point-pushing kernel in

```text
1 -> F_{n-1} -> P_n -> P_{n-1} -> 1.
```

The content is not that vertical Brunnian phenomena cannot occur.  They do
occur in finite rack actions.  The content is that endpoint-nontrivial vertical
commutators cannot remain simultaneously invisible to the fixed finite Artin
quotient and all bounded deletion endpoint/Artin shadows.

## Induction To Full Determinacy

Assume the vertical lemma for `I`, with constants `s,N`.  Let

```text
gamma in L_n(c)
```

be a branch with

```text
q_s^{T_n} alpha_n(gamma) = 1
```

and

```text
(q_s^{T_J} alpha_J(d_J gamma), epsilon_J(d_J gamma)) = (1,1)
for every |J| <= N.
```

We prove `epsilon_n(gamma)=1` by induction on `n`.

If `n <= N`, take `J={1,...,n}`; the deletion condition is the original
branch, so `epsilon_n(gamma)=1`.

If `n>N`, set

```text
bar_gamma = d_hat_n gamma.
```

Deletion compatibility gives trivial full finite-Artin readout for
`bar_gamma`, and every `|J|<=N` deletion shadow of `bar_gamma` is a deletion
shadow of `gamma`.  By induction,

```text
epsilon_{n-1}(bar_gamma)=1.
```

Lift `bar_gamma` back to arity `n` by adding the last strand straight on the
right.  The lift is actual because crossings among the first `n-1` strands
change the prefix context by the same product relation

```text
r(x,y)=(u,v)  =>  tau_x tau_y = tau_u tau_v.
```

Call the lift `tilde_gamma`.  Then

```text
d_hat_n tilde_gamma = bar_gamma,
epsilon_n(tilde_gamma)=epsilon_{n-1}(bar_gamma)=1.
```

Now put

```text
zeta = gamma tilde_gamma^{-1}.
```

Then `zeta in V_n(c)`.  Its full finite-Artin readout and bounded deletion
profiles are trivial because those of `gamma` and `tilde_gamma` are trivial.
The vertical lemma gives

```text
epsilon_n(zeta)=1.
```

Therefore

```text
epsilon_n(gamma)
  = epsilon_n(zeta) epsilon_n(tilde_gamma)
  = 1.
```

So the vertical lemma implies finite-degree endpoint determinacy, hence the
positive endpoint separation route.

## Finite Vertical Search Object

For fixed `I,s,N,n,c`, the vertical obstruction is finite and more focused
than the full residual graph.

Use the standard last-strand point-pushing generators

```text
A_{i,n}
  =
  sigma_{n-1} sigma_{n-2} ... sigma_{i+1} sigma_i^2
  sigma_{i+1}^{-1} ... sigma_{n-2}^{-1} sigma_{n-1}^{-1},
  1 <= i < n.
```

These generate the vertical kernel of `P_n -> P_{n-1}`.

Build a finite directed graph whose vertices are the full residual state plus
all deletion states of size at most `N`:

```text
v = (e, pi, (e_J, pi_J)_{1 <= |J| <= N}).
```

For every `i<n`, add an edge labelled by `A_{i,n}` when the expanded braid
word is supported from that vertex, and add the inverse edge when
`A_{i,n}^{-1}` is supported.  Each edge label is the product of the labels of
the expanded `sigma_j^{+/-1}` moves in

```text
D_{s,N,n}
  =
  A_s^{T_n} x U x
  prod_{1 <= |J| <= N}(A_s^{T_J} x U).
```

Let

```text
Lambda^vert_{I,s,N,n,c} <= D_{s,N,n}
```

be the subgroup of labels of loops at the base vertex.  It is computed by the
same spanning-tree cycle method as in `labelled_loop_subgroup_audit(...)`:
for each directed edge `e:v->w` with label `ell(e)` and tree path labels
`p_v,p_w`, add

```text
p_v ell(e) p_w^{-1}
```

to the generator list.

Define the vertical endpoint obstruction subgroup

```text
H^vert_{I,s,N,n,c}
  =
  { u in U : (1,u,(1,1)_J) in Lambda^vert_{I,s,N,n,c} }.
```

Then

```text
H^vert_{I,s,N,n,c} != 1
```

if and only if there exists an actual vertical residual branch loop `zeta`
with

```text
q_s^{T_n} alpha_n(zeta)=1,
(q_s^{T_J} alpha_J(d_J zeta), epsilon_J(d_J zeta))=(1,1)
for every |J| <= N,
epsilon_n(zeta) != 1.
```

This is the exact finite certificate for failure of the vertical lemma at
fixed `(s,N,n,c)`.

## Negative Certificate

A vertical-route refutation must output

```text
(I,u,W)
```

where `I` is an actual finite interval, `u in U` is nonidentity, and `W` is an
effective procedure that for every pair `(s,N)` returns

```text
n(s,N), c(s,N), w_{s,N}(A_{1,n},...,A_{n-1,n})
```

such that the expanded branch word is supported and verifies

```text
q_s^{T_n} alpha_n(w_{s,N}) = 1,
epsilon_n(w_{s,N}) = u,
(q_s^{T_J} alpha_J(d_J w_{s,N}), epsilon_J(d_J w_{s,N})) = (1,1)
for every |J| <= N.
```

This is smaller than searching arbitrary braid words because it only searches
vertical point-pushing words.

## Small Search Target

The affine `F_2^3` pressure row is not the next vertical search seed, because
the position-dependent gauge recorded in
`proofs/affine_f2_hidden_cyclic_gauge.md` makes it kernel-equivalent to the
two-element cyclic rack.

The next finite search should start with whole YBE tables of size `5` or `6`
that pass the following filters:

```text
bijective YBE,
not left-nondegenerate,
non-involutive,
not flip-across decomposable,
not kernel-equivalent to a rack of size <= 3 through observed arities.
```

For each such `X`, enumerate small actual intervals by choosing small context
sets `C`, maps `tau_x` satisfying the structure relation, retained subsets
`G` closed under rows and inverse rows, small endpoint groups `U`, and row
labels `eta` satisfying cube cocycles.

The first finite pressure targets are

```text
H^vert_{I,2,2,3,c} != 1
```

or

```text
H^vert_{I,3,2,3,c} != 1.
```

Such a hit is only a finite-level pressure witness.  A no-rack outcome still
requires a cofinal recursive family in `(s,N)`.

## Current Fork

The decisive missing theorem is now:

```text
for every actual finite interval I, there exist s,N such that
H^vert_{I,s,N,n,c}={1} for every n,c.
```

Proving this completes finite Artin-null endpoint separation.  Cofinal failure
of this vertical statement gives the required actual normalized-law no-rack
branch family.
