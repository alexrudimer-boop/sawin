# Normalized-law domination dichotomy

Date: 2026-05-30

This note strengthens the diagonal obstruction lemma.  It proves that the
normalized-law sequence requested for outcome B is not an extra format
assumption.  For a fixed finite solution, failure of finite-rack domination
forces such a sequence.

The note does not construct an explicit counterexample.  It shows that once a
finite solution, or a local residual interval, is proved to have no fixed
finite group detector, the normalized-law obstruction follows formally.

## Global statement

Let `X` be a finite nonempty bijective set-theoretic Yang-Baxter solution.
For a finite group `G`, define

```text
K_G(n) = { beta in B_n :
          Lambda_{G,n}(beta)=Lambda_{G,n}(1) }.
```

In the repository convention `Lambda` includes the Artin strand permutation.
Equivalently, by the sharp detector theorem,

```text
K_G(n) = ker rho_{A_G,n},
```

where

```text
A_G = T_2 x (G x G),
(a,u) rack (b,v) = (aba^-1, av).
```

Then the following are equivalent.

1. `X` is finitely rack-dominated: there is a finite rack `Y`, independent of
   `n`, such that

   ```text
   ker rho_{Y,n} <= ker rho_{X,n}
   ```

   for every `n`.

2. `X` is finitely group-longitude dominated: there is a finite group `G`,
   independent of `n`, such that

   ```text
   K_G(n) <= ker rho_{X,n}
   ```

   for every `n`.

3. There is no normalized-law obstruction sequence: there are no braid words

   ```text
   beta_j in B_{q_j},     q_j -> infinity,
   ```

   such that `beta_j in K_G(q_j)` eventually for every finite group `G`, but

   ```text
   rho_{X,q_j}(beta_j) != 1
   ```

   for every `j`.

Thus, for a fixed finite solution `X`, exactly one of the following holds:

```text
X is finitely rack-dominated;
X admits a normalized-law obstruction sequence.
```

## Lemma 1: rack domination reduces to the inner-group detector

Let `Y` be a finite rack in left convention

```text
R_Y(a,b) = (a rack b, a).
```

Write `L_a(b)=a rack b`, and let

```text
G = Inn(Y) = < L_a : a in Y > <= Sym(Y).
```

Then, for every `n`,

```text
K_G(n) = ker rho_{A_G,n} <= ker rho_{Y,n}.
```

Proof.  Let `beta in K_G(n)`.  The sharp detector theorem says that
`p_beta=id` and that, for every homomorphism `phi:F_n -> G`,

```text
phi(L_i(beta)) = 1
```

for all recursive Artin longitudes `L_i(beta)`.

For any tuple `y=(y_1,...,y_n) in Y^n`, define

```text
phi_y:F_n -> G,      phi_y(x_i)=L_{y_i}.
```

The standard rack longitude factorization gives

```text
rho_{Y,n}(beta)(y)_i
  = phi_y(L_i(beta))( y_{p_beta(i)} ).
```

For a positive generator this is exactly

```text
(y_i,y_{i+1}) |-> (L_{y_i}(y_{i+1}), y_i),
```

and the general case follows by induction on the braid word, using the same
recursive Artin longitude convention as the detector rack.  Since `p_beta=id`
and every `phi_y(L_i(beta))` is the identity permutation, `beta` fixes every
tuple of `Y^n`.  Hence `beta in ker rho_{Y,n}`.  QED.

## Lemma 2: finite rack domination equals finite group-longitude domination

If `Y` dominates `X`, take `G=Inn(Y)`.  Lemma 1 gives

```text
K_G(n) <= ker rho_{Y,n} <= ker rho_{X,n}
```

for every `n`, so `X` is finitely group-longitude dominated.

Conversely, if a finite group `G` satisfies

```text
K_G(n) <= ker rho_{X,n}
```

for every `n`, then the finite rack `A_G` itself dominates `X`.  Thus finite
rack domination and finite group-longitude domination are equivalent.

## Lemma 3: failure gives a normalized-law sequence

Assume no finite group `G` satisfies

```text
K_G(n) <= ker rho_{X,n}
```

for all `n`.  Enumerate finite groups up to isomorphism as

```text
G_1, G_2, G_3, ...
```

and set

```text
P_j = G_1 x ... x G_j.
```

Since `P_j` is finite and does not dominate `X`, choose `n_j` and
`alpha_j in B_{n_j}` such that

```text
alpha_j in K_{P_j}(n_j),
rho_{X,n_j}(alpha_j) != 1.
```

Choose a tuple `x_j in X^{n_j}` moved by `alpha_j`.  Stabilize on the right by
adding unused strands:

```text
q_j = n_j + j,
beta_j = iota_j(alpha_j) in B_{q_j}.
```

Since `X` is nonempty, choose `x_0 in X` and extend

```text
tilde x_j = (x_j,x_0,...,x_0) in X^{q_j}.
```

The stabilized braid still moves `tilde x_j`, while `q_j -> infinity`.

For any fixed finite group representative `G_r`, if `j >= r`, projection
`P_j -> G_r` sends identity `P_j`-longitude data to identity `G_r`-longitude
data.  Right stabilization preserves old recursive longitudes and gives empty
longitudes on the added strands.  Therefore

```text
beta_j in K_{G_r}(q_j)
```

for every `j >= r`.  If `G` is isomorphic to `G_r`, the same conclusion holds
for `G` by transporting assignments across the isomorphism.  Hence the
sequence is eventually invisible to every finite group and still moves `X`.
QED.

## Lemma 4: a normalized-law sequence defeats every finite rack

Let `beta_j in B_{q_j}` be a normalized-law obstruction sequence for `X`.
For any finite rack `Y`, put `G=Inn(Y)`.  Eventually `beta_j in K_G(q_j)`.
By Lemma 1,

```text
beta_j in ker rho_{Y,q_j}
```

eventually.  But by hypothesis

```text
beta_j notin ker rho_{X,q_j}.
```

Thus `ker rho_{Y,q_j}` is not contained in `ker rho_{X,q_j}` for large `j`.
No finite rack `Y` dominates `X`.

This proves the global equivalence.

## Local residual version

Fix a quotient interval

```text
pi:X -> Z
```

with `Z` dominated by a finite rack `Q`, and set

```text
N_n = ker rho_{Q,n}.
```

For `z in Z^n`, let

```text
delta_{n,z}:N_n -> Sym(X_z)
```

be the residual action and let `Delta_n(beta)` be the tuple of all residual
actions over base tuples.

Exactly one of the following holds.

1. There is a finite group `G(pi,Q)`, independent of `n`, such that for every
   `beta in N_n`,

   ```text
   Lambda_{G(pi,Q),n}(beta)=Lambda_{G(pi,Q),n}(1)
     => Delta_n(beta)=1.
   ```

2. There are braid words

   ```text
   beta_j in B_{q_j},     q_j -> infinity,
   ```

   such that

   ```text
   beta_j in N_{q_j},
   Lambda_{G,q_j}(beta_j)=Lambda_{G,q_j}(1)
   ```

   eventually for every finite group `G`, but

   ```text
   Delta_{q_j}(beta_j) != 1
   ```

   for every `j`.

The proof is the same diagonal argument, with the witnesses chosen inside
`N_n`.  Stabilization preserves membership in `N_n`: if `alpha in N_n`, then
the braid obtained by adding trivial right strands acts as `alpha` on the
first `n` coordinates of `Q^q` and as the identity on the added coordinates,
so it lies in `N_q`.  If `Delta_n(alpha) != 1`, choose a base tuple `z` and a
fibre tuple `x in X_z` that is moved.  Extend `z` and `x` by an arbitrary
quotient colour and a fibre point over it.  The stabilized residual action
still moves the extended tuple.

## Consequence

The normalized-law obstruction required for outcome B is forced by failure of
finite-rack domination, globally and locally.  Therefore the branch's current
gap has a precise fork:

1. prove the uniform descent-separation and endpoint-longitudinalization
   theorem, yielding a fixed finite `G(pi,Q)`; or
2. exhibit an explicit finite local-minimal interval with no such finite group,
   in which case the normalized-law residual obstruction sequence follows by
   the theorem above.

This step is symbolic and all-`n`; it uses no finite-search or timeout
evidence.  It does not replace the need for an explicit interval or solution
in outcome B.

