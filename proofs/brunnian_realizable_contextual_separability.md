# Brunnian-Realizable Contextual Separability

This note separates finite-quotient inseparability in the contextual augmented
action from actual Brunnian realizability.  A nonseparable contextual
transporter is harmless unless it is realized by quotient-trivial Brunnian
braid motion.

## Universal Contextual Transporter

Let

```text
hat P=M_L x X x M_R
```

be the raw contextual states, and let

```text
P_0=hat P / ~_0
```

be the same-strand quotient.  Let `C_X` be the finite labelled contextual
action graph with vertices `P_0` and edges

```text
[q] --g_p--> [r]
```

whenever `p*q=r` is a forced compatible contextual product.

For vertices

```text
v=[p],        w=[p'],
```

let

```text
T(v,w)={g in G_X : g omega_v=omega_w}
```

be the full contextual transporter in the universal contextual action.  If
`v,w` are connected and `tau_0` is one path label from `v` to `w`, then

```text
T(v,w)=tau_0 Lambda_v,
```

where

```text
Lambda_v=Stab_{G_X}(omega_v)
```

is the loop subgroup at `v`.

## Brunnian-Realizable Transporter Subset

Fix a braided congruence `E` on `X`.  Define

```text
T_Br^E(p,p') subset T([p],[p'])
```

as follows.

An element `tau` lies in `T_Br^E(p,p')` iff there exist:

```text
n>=2,
beta in Brun_n cap ker rho^{X/E}_n,
xword in X^n,
j in {1,...,n},
```

such that

```text
hat c_j(xword)=p,
hat c_j(rho^X_n(beta)xword)=p',
```

and the same physical strand, followed through a braid word for `beta`, traces
a path in `C_X` with label `tau`.

Thus `T_Br^E(p,p')` is the subset of the contextual transporter consisting of
paths actually realized by quotient-trivial Brunnian braid trajectories.  It
can be strictly smaller than the full transporter `T([p],[p'])`: the full
contextual graph includes locally forced edges whose paths need not be
globally fillable by one `X`-word and one braid trajectory.

## Finite Quotient Obstruction For A Fixed Transition

Let

```text
q:G_X->H
```

be a finite quotient, and let

```text
Y_H=Omega_H x H
```

be the associated finite augmented contextual rack.

Suppose a Brunnian trajectory realizes `p->p'` with transporter label

```text
tau in T_Br^E(p,p').
```

Then this trajectory is invisible to `Y_H` only if both

```text
q(g_p)=q(g_{p'}),
```

and, with `v=[p]`,

```text
q(tau) in q(Lambda_v).
```

Equivalently,

```text
q(g_p^{-1}g_{p'})=1
```

and the image of the transporter coset meets the image of the loop subgroup.

Therefore a finite quotient `q` kills no Brunnian-realizable transition from
`p` to `p'` if either

```text
q(g_p) != q(g_{p'}),
```

or

```text
q(T_Br^E(p,p')) cap q(Lambda_v)=emptyset.
```

If `T_Br^E(p,p')` is empty, the second condition holds automatically.

## Exact Brunnian-Realizable Separability Criterion

Assume `X/E` is dominated by a finite rack.

Suppose that for every color-changing contextual pair

```text
p=(A,a,B),        p'=(A',b,B'),
```

with

```text
a E b,        a != b,
```

there exists a finite quotient

```text
q:G_X->H
```

such that either

```text
q(g_p) != q(g_{p'}),
```

or

```text
q(T_Br^E(p,p')) cap q(Lambda_[p])=emptyset.
```

Then `X` is finite-rack dominated.

### Proof

There are finitely many raw contextual pairs.  Choose one finite quotient
separating each color-changing pair in the stated sense, and take their
product quotient.  Let the corresponding finite contextual rack be
`Y_ctx`.  Let `Y_E` be a finite rack dominating `X/E`, and set

```text
Q=Y_E^0 x Y_ctx^0 x T_2.
```

If `Q` failed to dominate `X`, the Brunnian reduction would give

```text
beta in Brun_n cap ker rho^Q_n
```

with

```text
rho^X_n(beta) != 1.
```

The `Y_E^0` factor gives

```text
beta in ker rho^{X/E}_n.
```

Since `beta` moves some `X^n`-state while acting trivially on `(X/E)^n`, some
coordinate realizes a color-changing contextual transition

```text
p->p'
```

with

```text
a E b,        a != b.
```

Let

```text
tau in T_Br^E(p,p')
```

be the actual contextual path label followed by that strand.  Since

```text
beta in ker rho^{Y_ctx^0}_n,
```

the chosen finite quotient for that pair must identify the before and after
contextual augmented colors.  Hence

```text
q(g_p)=q(g_{p'})
```

and

```text
q(tau) in q(Lambda_[p]).
```

This contradicts the separating property of the quotient chosen for
`p,p'`.  Therefore no such Brunnian witness exists, and `Q` dominates `X`.

## Minimal-Counterexample Consequence

Let `X` be a smallest nonsimple counterexample with monolith

```text
mu=mu_X.
```

Then there is a fixed color-changing contextual pair

```text
p_*=(A_*,a_*,B_*),
p'_*=(A'_*,b'_*,B'_*),
```

with

```text
a_* != b_*,
a_* mu b_*,
```

such that for every finite quotient `q:G_X->H`,

```text
q(g_{p_*})=q(g_{p'_*}),
```

and

```text
q(T_Br^mu(p_*,p'_*)) cap q(Lambda_[p_*]) != emptyset.
```

Equivalently,

```text
g_{p_*}^{-1}g_{p'_*} in Res(G_X),
```

where `Res(G_X)` is the finite residual of `G_X`, and

```text
closure_prof(T_Br^mu(p_*,p'_*))
  cap
closure_prof(Lambda_[p_*])
  != emptyset
```

inside the profinite completion of `G_X`.

This is stronger and more accurate than the earlier condition

```text
tau in closure_prof(Lambda_v)
```

for an arbitrary transporter `tau`.  The actual transporter may vary among
Brunnian realizations, and arbitrary elements of the full transporter may be
virtual.

## Consequence

The positive contextual target is now:

```text
For every finite X, every dominated congruence E, and every color-changing
contextual pair p,p' with a E b and a != b, find a finite quotient q:G_X->H
such that either q(g_p) != q(g_{p'}) or
q(T_Br^E(p,p')) cap q(Lambda_[p])=emptyset.
```

The negative target is:

```text
Construct one fixed finite X, one dominated congruence E, and one fixed
color-changing contextual transition p->p' such that
g_p^{-1}g_{p'} in Res(G_X) and
closure_prof(T_Br^E(p,p')) cap closure_prof(Lambda_[p]) is nonempty,
with the intersection realized cofinally by actual quotient-trivial Brunnian
motions invisible to every finite rack detector.
```

This is the realization-aware contextual separability boundary.
