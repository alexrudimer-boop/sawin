# Contextual Endpoint Residuality Audit

Date: 2026-06-05

This note records the audit of pointwise endpoint-faithfulness.  The conclusion
is:

```text
Pointwise endpoint-faithfulness is not presently formal.
```

It is a finite-residual injectivity statement for contextual endpoint profiles
on `K_n(P_X)`-fiber monodromy.  Local YBE identities make the endpoint
machinery coherent, but they do not prove finite rack residual separation.

The current Target A route therefore still has a principal obstruction:

```text
a single endpoint-invisible bad triple.
```

## Pointwise Endpoint-Faithfulness

Let

```text
kappa:X -> P_X
```

be the universal finite rack shadow.  A bad triple is

```text
(n,a,beta),
a in X^n,
beta in K_n(P_X),
beta a != a.
```

Since `beta in K_n(P_X)`,

```text
kappa^n(beta a)
=
rho_n^{P_X}(beta) kappa^n(a)
=
kappa^n(a).
```

Thus the motion is entirely inside a `kappa^n`-fiber.

For a finite quotient `M` of `L_X`, endpoint detectors only see finite
residual classes of labels:

```text
d_{epsilon_i^M(a)},
d_{epsilon_i^M(beta a)}
```

inside the contextual rack `C_M(X)`.

Pointwise endpoint-faithfulness asserts:

```text
beta in K_n(P_X), beta a != a
implies
exists finite M and i <= n such that
d_{epsilon_i^M(a)}
not equiv_M
d_{epsilon_i^M(beta a)}.
```

Equivalently:

```text
beta a != a
implies
exists M,i such that the two endpoint labels are separated by a finite rack
quotient of C_M(X).
```

This is an endpoint residuality theorem.  It is not contained in the
definitions.

## Finite Residual Congruence

For each `M`, define the finite residual congruence:

```text
theta_M^fin =
intersection over q:C_M(X)->Q, Q finite rack, of ker q.
```

Then:

```text
s equiv_M t
iff
(d_s,d_t) in theta_M^fin.
```

Equivalently, let

```text
hat{C_M(X)} =
lim_{q:C_M(X)->Q, Q finite rack} Q
```

and let

```text
eta_M:C_M(X)->hat{C_M(X)}
```

be the canonical map.  Then:

```text
s equiv_M t
iff
eta_M(d_s)=eta_M(d_t).
```

For fixed `n`, define the residual endpoint profile:

```text
E_n(a)=(
  eta_M(d_{epsilon_1^M(a)}), ...,
  eta_M(d_{epsilon_n^M(a)})
)_M
in product_M hat{C_M(X)}^n.
```

Pointwise endpoint-faithfulness is exactly:

```text
beta in K_n(P_X), E_n(beta a)=E_n(a)
implies
beta a=a.
```

So `E_n` must be injective on nontrivial `K_n(P_X)`-transitions inside
`kappa^n`-fibers.

The natural monodromy map is a source-target endpoint-profile map:

```text
K_n(P_X) semidirect X^n
  -> (product_M hat{C_M(X)}^n)^2,

(beta,a) -> (E_n(a),E_n(beta a)).
```

Pointwise faithfulness says this map has no off-diagonal invisible arrows.

## Fixed Arity

For fixed `n`, define:

```text
H_n =
< (rho_n^X(sigma_i), rho_n^P(sigma_i)) : 1 <= i < n >
<= Sym(X^n) x Sym(P_X^n).
```

The image of `K_n(P_X)` on `X^n` is:

```text
G_n^{X/P}={
  g in Sym(X^n) : (g,id_{P_X^n}) in H_n
}.
```

The finite transition set is:

```text
T_n={
  (a,ga) : a in X^n, g in G_n^{X/P}, ga != a
}.
```

This is finite because `X^n` is finite.

Assuming pointwise endpoint-faithfulness, choose one finite quotient detecting
each `(a,c) in T_n`, then take a common refinement.  This yields one finite
quotient `M_n` with:

```text
B_n subset D_{M_n}.
```

Thus:

```text
pointwise endpoint-faithfulness implies fixed-arity uniformity.
```

The detecting quotient depends only on the endpoint transition `(a,c)`, not
on the braid witness `beta`; the witness only certifies membership in `T_n`.

## Principal Endpoint-Invisible Bad Triple

A principal invisible bad triple consists of:

```text
(n,a,beta),
beta in B_n,
a in X^n,
```

such that:

```text
1. beta in K_n(P_X);
2. c=beta a != a;
3. kappa^n(c)=kappa^n(a);
4. for every finite quotient M of L_X and every i <= n,
   epsilon_i^M(a) equiv_M epsilon_i^M(c).
```

Equivalently, for every finite `M`, every coordinate endpoint displacement
lies in the finite residual congruence:

```text
(
  d_{epsilon_i^M(a)},
  d_{epsilon_i^M(c)}
) in theta_M^fin.
```

If `beta=s_l ... s_1` is a braid word and:

```text
a^0=a,
a^{t+1}=rho_n^X(s_{t+1})(a^t),
a^l=c,
```

then the projected path:

```text
p^t=kappa^n(a^t)
```

closes in `P_X^n` but not in `X^n`.

The obstruction pattern is:

```text
closed in P_X,
nonclosed in X,
endpoint-residually closed in every C_M(X).
```

There are two subtypes.

Strong invisibility:

```text
epsilon_i^M(a)=epsilon_i^M(c) for all M,i.
```

Residual invisibility:

```text
endpoint symbols may differ, but they are identified by every finite rack
quotient of every C_M(X).
```

The residual subtype is the serious one.

## Where Local YBE Stops

Write:

```text
r(x,y)=(L_x(y),R_y(x)).
```

The component YBE identities ensure braid coherence:

```text
L_{L_x(y)} L_{R_y(x)}(z)=L_x L_y(z),

R_{L_{R_y(x)}(z)}(L_x(y))
=
L_{R_{L_y(z)}(x)}(R_z(y)),

R_z R_y(x)
=
R_{R_z(y)} R_{L_y(z)}(x).
```

They guarantee that contextual rack relations are coherent and that different
braid words representing the same braid give the same formal endpoint
transport.

The attempted pointwise proof would need:

```text
beta a != a
implies
exists M,i:
d_{epsilon_i^M(a)}
not equiv_M
d_{epsilon_i^M(beta a)}.
```

Local identities do not imply this.  The first failed step is:

```text
d_s != d_t in C_M(X)
implies
d_s not equiv_M d_t.
```

This is finite residuality of endpoint elements, not a YBE identity.

There can be an even earlier failure if endpoint profiles themselves do not
separate the changed coordinate:

```text
beta a != a
does not formally imply
exists M,i with epsilon_i^M(a) != epsilon_i^M(beta a).
```

Thus local YBE proves braid coherence, not endpoint residuality.

## Special Branches

In finite racks, the universal rack shadow is already faithful and there are
no bad triples.

In left-nondegenerate bijective solutions, direct rack domination is known
through derived-rack/guitar machinery.  Pointwise endpoint-faithfulness follows
inside Target A only if those derived labels are represented by the contextual
endpoint system.  The special branch uses invertibility of the `L_x` maps and
therefore does not extend formally to all bijective solutions.

In nondegenerate involutive or symmetric solutions, direct domination is
positive.  Target-A pointwise again depends on whether the finite symmetric or
derived-rack labels live inside the contextual endpoint racks.

In degenerate involutive solutions, braid actions factor through symmetric
actions, so direct rack domination may be easy, but Target-A pointwise
residuality is not automatic.

In constant-action or permutation solutions, pointwise is direct when finite
permutation labels are word-defined endpoint data.  Otherwise it is a separate
finite-state argument, not a formal consequence of `C_M(X)`.

Products inherit pointwise from factors if contextual endpoints project to
factor endpoints.  Padding is safe only if the padding cocycle is
finite-rack-visible; otherwise padding can mimic endpoint-invisible holonomy.

The key distinction is:

```text
direct finite rack domination
does not imply
Target-A pointwise endpoint-faithfulness.
```

The finite rack absorber might not arise from the contextual endpoint detector
framework.

## Effect On Target A

If pointwise endpoint-faithfulness fails, there exists a bad triple `b` with:

```text
b notin D_M for every finite M.
```

Then no refinement, compactness argument, or uniformity argument can prove:

```text
B=D_{M_*}
```

inside the current endpoint-detector framework.

Thus failure of pointwise kills Target A as currently formulated.  It does not
disprove Sawin, because an independent finite rack absorber might exist
outside the contextual endpoint racks.

The `D_M` framework is complete for detectors of the form:

```text
C_M(X) -> Q, Q finite rack.
```

It is not complete for arbitrary active factors or unrelated finite rack
domination mechanisms.

## Target B Does Not Follow

A principal invisible triple gives:

```text
a in X^n,
c=beta a != a,
beta in K_n(P_X),
```

and a braid path from `a` to `c`.

Target B would require finite coordinatewise YBE data:

```text
Z finite,
r_Z:Z^2 -> Z^2 total bijective YBE,
pi or pi_{a,b}:X -> Z,
global braid equivariance,
global orbit-injectivity or kernel inclusion.
```

A single invisible transition supplies none of this global coordinatewise
structure.  It gives a finite orbit fragment, not a closed YBE table or a
kernel-inclusion proof in every arity.

Thus:

```text
principal invisibility suggests where to search for Target B,
but does not produce Target B.
```

## Useful Additional Hypotheses

The weakest pointwise hypothesis is pairwise residual endpoint separation:

```text
(EP)
for every n and every (a,c) in T_n,
E_n(a) != E_n(c).
```

Equivalently:

```text
for every bad endpoint transition, some coordinate endpoint pair is separated
in a finite residual contextual endpoint rack.
```

Other sufficient hypotheses:

Endpoint residual faithfulness:

```text
the map s -> eta_M(d_s) is injective on endpoint pairs arising from bad
transitions, for suitable finite M.
```

Enriched finite endpoint labels:

```text
a separating family of word-defined finite rack labels extending the
contextual endpoint labels.
```

Local-to-global endpoint residuality:

```text
every nontrivial X-fiber monodromy produced by K_n(P_X) gives a nontrivial
element in the finite residual completion of some contextual endpoint rack.
```

No-principal-holonomy theorem:

```text
there is no braid path closed in P_X, nonclosed in X, and closed in every
finite residual contextual endpoint rack.
```

## Sharp Valid Theorems

Theorem A: fixed arity under pointwise.

If pointwise endpoint-faithfulness holds, then for every fixed `n` there is a
finite quotient `M_n` with:

```text
B_n subset D_{M_n}.
```

Proof: reduce to the finite transition set `T_n`, choose a detecting quotient
for each transition pair, and take a common directed refinement.

Theorem B: pointwise characterization.

Pointwise is equivalent to:

```text
for every n and every (a,c) in T_n,
exists M,i with
eta_M(d_{epsilon_i^M(a)})
!=
eta_M(d_{epsilon_i^M(c)}).
```

This is not currently derivable from local YBE identities or from the
universal finite rack shadow alone.  It is an endpoint residuality theorem.

Theorem C: remaining uniformity.

Uniform endpoint-faithfulness asks for one quotient:

```text
exists M_* with B=D_{M_*}.
```

Pointwise gives fixed-arity uniformity but not a single quotient across all
arities.  If pointwise holds but uniformity fails, the obstruction is a
nonprincipal arity-escaping harmful ultrafilter.

Theorem D: Target B boundary.

Target B begins only when one constructs independent finite coordinatewise
YBE or rack active data with global orbit-injectivity or kernel inclusion.
Residual endpoint quotients and principal invisible triples do not supply this
automatically.

## Final Conclusion

The contextual Target A route currently proves:

```text
pointwise endpoint-faithfulness
implies
fixed-arity uniformity.
```

It does not currently prove pointwise endpoint-faithfulness itself.

Pointwise is finite-residual injectivity of contextual endpoint profiles on
`K_n(P_X)`-fiber monodromy.  Principal endpoint-invisible bad triples remain a
genuine possible obstruction to Target A until a no-principal-holonomy or
endpoint-residuality theorem is proved.
