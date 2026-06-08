# Probe-Centralizer Chief Obstruction

This note makes the probe-central branch from
`brunnian_derivative_chief_dichotomy.md` finite and computable.  The vague
condition

```text
the X-motion centralizes every one-strand probe
```

is exactly membership in a finite centralizer subgroup of the permutation
image of the last-strand free group.

## Probe Centralizer In The X-Image

Fix arity `n`.  Let

```text
F_{n-1}=ker(d_n:P_n->P_{n-1})
```

be the last-strand free group, and set

```text
G^X_n=rho^X_n(F_{n-1}) <= Sym(X^n).
```

Embed `B_n` into `B_{n+1}` by adding a new idle last strand.  This induces a
well-defined embedding of permutation images

```text
iota_n:G^X_n -> Sym(X^{n+1}),
```

because two braids with the same `X^n`-action still have the same action after
adding an idle coordinate.

For each old strand `i=1,...,n`, fix a half-twist

```text
tau_i in B_{n+1}
```

exchanging strand `i` with the new strand, and define

```text
T_{i,n}=rho^X_{n+1}(tau_i) in Sym(X^{n+1}).
```

Define the probe-centralizer subgroup

```text
Z^pr_n(X)
  =
{ g in G^X_n : [iota_n(g),T_{i,n}]=1 for every i=1,...,n }.
```

This is an explicitly computable finite subgroup of `G^X_n`: it is the
intersection of the preimages under `iota_n` of the centralizers of the
finite permutations `T_{i,n}`.

## Pullback To A Combined Detector Image

Let `Q` be a finite rack detector and let

```text
Phi_n:F_{n-1}->Gamma_n
  <= Sym(Q^n) x Sym(X^n)
```

be the combined finite image.  Let

```text
p_X:Gamma_n->G^X_n
```

be projection to the `X`-image, and define

```text
PC_n=p_X^{-1}(Z^pr_n(X)).
```

Thus `PC_n` is the finite subgroup of combined-image elements whose `X`
projection is probe-central.

Keep the standard notation

```text
K_n=ker(Gamma_n->rho^Q_n(F_{n-1})),
L_n=ker(Gamma_n->rho^X_n(F_{n-1})),
```

and, for meridians `x_i=A_{i,n}`,

```text
N_{i,n}=<<Phi_n(x_i)>>_{Gamma_n},
C_n=[N_{1,n},...,N_{n-1,n}]_Sigma.
```

Inside the product image,

```text
K_n cap L_n=1.
```

## Theorem: Probe-Central Chief-Factor Branch

Let `X` be a smallest finite bijective YBE solution not dominated by any
finite rack.  Let

```text
mu=mu_X
```

be its unique first-fold monolith.

For a rack prefix `P_m`, choose a finite rack `Y_mu` dominating the proper
quotient `X/mu`, and include the bounded-support detector factors as before:

```text
Q=Q_{m,s}=(P_m x Y_mu)^0 x T_2 x B_s(X).
```

If the derivative-visible branch fails cofinally, then for every `m,s,N`
there exists `n>N` and a chief factor

```text
A/B
```

of `Gamma_n` such that

```text
B < A <= K_n cap C_n cap PC_n,
```

and the `X`-projection of `A` acts nontrivially inside `mu`-fibres and
generates `mu` by coordinate mismatches.

Equivalently, the probe-central obstruction is cofinal nontriviality of the
finite centralizer intersection

```text
K_n cap C_n cap PC_n.
```

## Proof

By `deletion_null_monolith_chief_obstruction.md`, for every `m,s,N` there are
unbounded arities with a deletion-null monolith chief factor

```text
B < A <= K_n cap C_n.
```

Every nontrivial `a in A` has a Brunnian `Q`-invisible representative

```text
beta_a in Brun_n cap ker rho^Q_n
```

with

```text
Phi_n(beta_a)=a.
```

For each old strand `i`, form the Brunnian derivative

```text
D_i beta_a=[iota(beta_a),tau_i] in Brun_{n+1} cap ker rho^Q_{n+1}.
```

Its combined image is

```text
partial_i(a)=Phi_{n+1}(D_i beta_a) in K_{n+1} cap C_{n+1}.
```

On the `X`-projection this image is exactly

```text
p_X(partial_i(a))
  =
[iota_n(p_X(a)),T_{i,n}].
```

If the derivative-visible branch fails cofinally, then after passing to the
cofinal deletion-null obstruction factors under consideration,

```text
partial_i(a)=1
```

for every `a in A` and every old strand `i`.  Therefore

```text
[iota_n(p_X(a)),T_{i,n}]=1
```

for every `a in A` and every `i`.  Hence

```text
p_X(a) in Z^pr_n(X),
```

so `a in PC_n`.  Since this holds for all `a in A`,

```text
A <= PC_n.
```

Together with `A <= K_n cap C_n`, this gives

```text
B < A <= K_n cap C_n cap PC_n.
```

It remains only to record why the factor still generates the monolith.  Since
`A <= K_n`, every element of `A` is invisible to the `Y_mu^0` factor of `Q`.
Because `Y_mu` dominates `X/mu`, the `X`-projection of `A` acts trivially on

```text
(X/mu)^n.
```

Thus every coordinate color change produced by `p_X(A)` lies inside a
`mu`-class.

Also `A` is nontrivial and `K_n cap L_n=1`, so `p_X(A)` is nontrivial.  Hence
some element of `A` moves some `X^n`-state.  The braided congruence generated
by all resulting nontrivial coordinate mismatches is nontrivial and contained
in `mu`.  Since `mu` is the monolith, this generated congruence is exactly
`mu`.

This proves the theorem.

## Consequence

The remaining obstruction split is now finite and exact.

### Branch A: Derivative-Propagating

For every detector prefix and support cutoff, deletion-null monolith chief
factors keep producing nontrivial Brunnian derivatives in higher arity:

```text
partial_i(A) subset K_{n+1} cap C_{n+1}
```

for some probe `i`.  This creates an infinite derivative tower of
monolith-generating Brunnian obstructions.

### Branch B: Probe-Central

The obstruction lies cofinally in

```text
K_n cap C_n cap PC_n.
```

Equivalently, detector-invisible all-meridian chief factors survive while
their `X`-projection centralizes every one-strand probe after adding a new
strand.

Thus a positive proof can attack two finite-image statements:

```text
no infinite derivative-propagating deletion-null monolith-chief tower;
K_n cap C_n cap PC_n=1 eventually.
```

A negative proof must construct one fixed finite `X` whose first-fold monolith
survives cofinally in one of these two exact ways.
