# Brunnian Derivative Chief Dichotomy

This note differentiates a deletion-null monolith-chief obstruction by adding
one probing strand.  The result is a dichotomy:

```text
either the obstruction propagates to a new Brunnian obstruction in arity n+1,
or its X-motion centralizes every one-strand probe.
```

The second branch is much more rigid than high support: it says the
monolith-generating motion is externally central with respect to every added
test strand.

## Setup

Let `X` be a smallest finite bijective YBE solution not dominated by any
finite rack, and let

```text
mu=mu_X
```

be its unique first-fold monolith.

Fix a rack prefix `P_m`, a rack `Y_mu` dominating `X/mu`, and a
bounded-support detector `B_s(X)`.  Set

```text
Q=Q_{m,s}=(P_m x Y_mu)^0 x T_2 x B_s(X).
```

For arity `n`, let

```text
F_{n-1}=ker(d_n:P_n->P_{n-1})
```

with meridian generators

```text
x_i=A_{i,n}.
```

Let

```text
Phi_n:F_{n-1}->Gamma_n
  <= Sym(Q^n) x Sym(X^n).
```

Define

```text
K_n=ker(Gamma_n->rho^Q_n(F_{n-1})),
L_n=ker(Gamma_n->rho^X_n(F_{n-1})),
```

and

```text
C_n=[N_{1,n},...,N_{n-1,n}]_Sigma,
N_{i,n}=<<Phi_n(x_i)>>_{Gamma_n}.
```

By `proofs/deletion_null_monolith_chief_obstruction.md`, for unbounded `n`
there is a chief factor

```text
A/B
```

with

```text
B < A <= K_n cap C_n,
```

such that every nontrivial element of `A` has a `Q`-invisible Brunnian
representative, and its `X`-motion generates `mu`.

## Brunnian Derivative

Take `a in A`.  Choose

```text
beta_a in Brun_n cap ker rho^Q_n
```

with

```text
Phi_n(beta_a)=a.
```

Embed `beta_a` into `B_{n+1}` by adding a new last strand, and write this
embedding as

```text
iota(beta_a).
```

For an old strand `i in {1,...,n}`, let

```text
tau_i in B_{n+1}
```

be the half-twist exchanging strand `i` with the new strand.  Define the
Brunnian derivative

```text
D_i beta_a = [iota(beta_a), tau_i].
```

## Lemma: The Derivative Is Brunnian And Detector-Invisible

For every `a in A` and every old strand `i`,

```text
D_i beta_a in Brun_{n+1} cap ker rho^Q_{n+1}.
```

### Proof

Deleting the new strand gives

```text
d_{n+1}(D_i beta_a) = [beta_a,1] = 1.
```

Deleting an old strand `j` gives

```text
d_j(D_i beta_a) = [d_j(iota beta_a), d_j(tau_i)].
```

Since `beta_a` is Brunnian, `d_j(iota beta_a)=1`.  Hence

```text
d_j(D_i beta_a)=1.
```

Thus `D_i beta_a` is Brunnian.

Also, `rho^Q_{n+1}(iota beta_a)=1` because `beta_a in ker rho^Q_n` and the
new strand is idle.  Therefore

```text
rho^Q_{n+1}(D_i beta_a)
  =
[1,rho^Q_{n+1}(tau_i)]
  =
1.
```

So the derivative is `Q`-invisible.

## Derivative Image

Define

```text
partial_i(a)=Phi_{n+1}(D_i beta_a) in Gamma_{n+1}.
```

This is independent of the chosen Brunnian representative `beta_a`.

Indeed, if `beta_a'` is another representative with `Phi_n(beta_a')=a`, then
`beta_a` and `beta_a'` have the same `Q`- and `X`-images in arity `n`.  After
adding an idle strand, their embedded `Q`- and `X`-images in arity `n+1` are
still equal.  Commuting both with the same probe braid `tau_i` therefore
gives the same combined image.

Thus

```text
partial_i:A->Gamma_{n+1}
```

is a well-defined set map, though not necessarily a homomorphism.

Moreover,

```text
partial_i(a) in K_{n+1} cap C_{n+1},
```

because `D_i beta_a` is `Q`-invisible and Brunnian.

## Chief-Factor Derivative Dichotomy

For each deletion-null obstruction chief factor `A/B`, exactly one of the
following alternatives holds.

### Branch I: Derivative-Visible Obstruction

There exist

```text
a in A,
i in {1,...,n}
```

such that

```text
partial_i(a) != 1.
```

Then

```text
K_{n+1} cap C_{n+1} != 1.
```

The `X`-projection of `partial_i(a)` is nontrivial because

```text
K_{n+1} cap L_{n+1}=1.
```

Since `partial_i(a) in K_{n+1}`, it is invisible to the `Y_mu^0` factor of
`Q`, so it acts trivially on

```text
(X/mu)^{n+1}.
```

Thus its coordinate mismatches lie inside `mu`-fibres.  Since the `X`-motion
is nontrivial, these mismatches generate a nontrivial braided congruence
contained in `mu`; by monolith minimality, they generate `mu`.

So a nontrivial derivative produces a new deletion-null, monolith-generating
Brunnian obstruction in arity `n+1`.  A chief factor can then be chosen
inside the new nontrivial subgroup `K_{n+1} cap C_{n+1}` if one wants to
continue the chief-factor analysis.

### Branch II: Probe-Central Obstruction

For every

```text
a in A
```

and every old strand `i`,

```text
partial_i(a)=1.
```

Equivalently, in the `X`-image after adding one new strand,

```text
[rho^X_{n+1}(iota beta_a), rho^X_{n+1}(tau_i)] = 1
```

for every representative `beta_a`, every `a in A`, and every old strand
`i`.  Since the embedded `X`-image of `iota beta_a` depends only on `p_X(a)`,
this says:

```text
p_X(A) centralizes every one-strand probe half-twist after adding a new
strand.
```

Thus the monolith-generating `X`-motion is invisible not only to the detector
but also to every single added test strand.

## Consequence

A smallest counterexample must support one of two cofinal behaviours.

### Derivative-Propagating Branch

Deletion-null monolith-chief factors keep producing nontrivial Brunnian
derivatives in higher arity:

```text
A/B  ->  partial_i(A) subset K_{n+1} cap C_{n+1}.
```

This gives an infinite tower of deletion-null monolith-generating Brunnian
obstructions.

### Probe-Central Branch

There are cofinally many deletion-null chief factors

```text
A/B <= K_n cap C_n
```

whose `X`-projection generates the first-fold monolith `mu`, but whose entire
`X`-action centralizes all one-strand probes:

```text
[p_X(A), rho^X_{n+1}(tau_i)] = 1        for every i.
```

This is much stronger than high support.  It is external centrality with
respect to every possible added-strand test.

The positive target is now to rule out both:

```text
infinite derivative-propagating monolith chief towers,
probe-central deletion-null monolith chief factors.
```

The negative target is to construct one fixed finite `X` whose first-fold
monolith supports one of these two cofinal behaviours against every finite
rack prefix.
