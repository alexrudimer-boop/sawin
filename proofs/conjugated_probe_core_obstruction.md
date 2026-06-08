# Conjugated-Probe Core Obstruction

This note sharpens the probe-central branch from
`probe_centralizer_chief_obstruction.md`.  The one-probe centralizer only tests
the added strand against the original old strand positions.  A Brunnian
obstruction can also be probed after first moving old strands by any
last-strand image.  The correct finite centralizer is therefore the normal
core of the one-probe centralizer.

## Conjugated Probe Derivatives

Let

```text
beta in Brun_n cap ker rho^Q_n.
```

Embed `beta` into `B_{n+1}` by adding a new idle last strand:

```text
iota(beta) in B_{n+1}.
```

Let

```text
eta in F_{n-1}=ker(d_n:P_n->P_{n-1})
```

be any last-strand braid on the old `n` strands, and let `tau_i in B_{n+1}`
be the half-twist exchanging old strand `i` with the new strand.  Define the
conjugated probe

```text
tau_{i,eta}=iota(eta) tau_i iota(eta)^{-1}.
```

Define the conjugated Brunnian derivative

```text
D_{i,eta} beta=[iota(beta),tau_{i,eta}].
```

## Lemma: Conjugated Derivatives Are Brunnian And Detector-Invisible

For every `i` and every `eta`,

```text
D_{i,eta} beta in Brun_{n+1} cap ker rho^Q_{n+1}.
```

### Proof

Deleting the new strand gives

```text
d_{n+1}(D_{i,eta} beta)
  =
[beta,d_{n+1}(tau_{i,eta})].
```

But

```text
d_{n+1}(tau_{i,eta})=eta 1 eta^{-1}=1,
```

so the new-strand deletion is trivial.

Deleting an old strand `j` gives

```text
d_j(D_{i,eta} beta)
  =
[d_j(iota beta),d_j(tau_{i,eta})].
```

Since `beta` is Brunnian, `d_j(iota beta)=1`.  Hence every old-strand deletion
is trivial, so `D_{i,eta} beta` is Brunnian.

Also,

```text
rho^Q_{n+1}(iota beta)=1
```

because `beta in ker rho^Q_n` and the added strand is idle.  Therefore

```text
rho^Q_{n+1}(D_{i,eta} beta)
  =
[1,rho^Q_{n+1}(tau_{i,eta})]
  =
1.
```

So the conjugated derivative remains `Q`-invisible.

## Conjugated-Probe Centralizer

Let

```text
G^X_n=rho^X_n(F_{n-1}).
```

Embed `G^X_n` into `Sym(X^{n+1})` by adding a new idle coordinate; denote this
embedding by `iota_n`.

For `h in G^X_n`, choose any `eta in F_{n-1}` with

```text
rho^X_n(eta)=h.
```

For `1<=i<=n`, set

```text
T_{i,h}=rho^X_{n+1}(iota(eta) tau_i iota(eta)^{-1}).
```

This is well-defined: if two choices of `eta` have the same `X^n`-image, then
their idle-strand embeddings have the same `X^{n+1}`-image, so they conjugate
`rho^X_{n+1}(tau_i)` by the same permutation.

Define

```text
CPC_n(X)
  =
{ g in G^X_n : [iota_n(g),T_{i,h}]=1
                for every i and every h in G^X_n }.
```

Equivalently, if

```text
Z^pr_n(X)
  =
{g in G^X_n : [iota_n(g),T_{i,1}]=1 for every i},
```

then

```text
CPC_n(X)=cap_{h in G^X_n} h Z^pr_n(X) h^{-1}.
```

Indeed, `g` centralizes `iota_n(h)T_{i,1}iota_n(h)^{-1}` iff
`h^{-1}gh` centralizes `T_{i,1}`.  Thus `CPC_n(X)` is the normal core of
`Z^pr_n(X)` in `G^X_n`, and

```text
CPC_n(X) normal G^X_n.
```

For a combined detector image

```text
Phi_n:F_{n-1}->Gamma_n
  <= Sym(Q^n) x Sym(X^n),
```

let `p_X:Gamma_n->G^X_n` be the `X`-projection and define

```text
CPC^Gamma_n=p_X^{-1}(CPC_n(X)).
```

Then

```text
CPC^Gamma_n normal Gamma_n.
```

## Theorem: Conjugated-Probe Core Obstruction

Let `X` be a smallest finite bijective YBE solution not dominated by any
finite rack, and let

```text
mu=mu_X
```

be its unique first-fold monolith.

For a rack prefix `P_m`, choose a finite rack `Y_mu` dominating `X/mu`, include
the bounded-support detector `B_s(X)`, and set

```text
Q=(P_m x Y_mu)^0 x T_2 x B_s(X).
```

Let

```text
K_n=ker(Gamma_n->rho^Q_n(F_{n-1})),
C_n=[N_{1,n},...,N_{n-1,n}]_Sigma
```

be the detector kernel and the exact all-meridian subgroup in the finite
image.

Then for every `m,s,N`, there exists `n>N` such that one of the following
alternatives holds.

### Branch A: Conjugated-Derivative Visible

There is an element

```text
a in K_n cap C_n
```

and a conjugated probe `(i,h)` such that

```text
[iota_n(p_X(a)),T_{i,h}] != 1.
```

Equivalently, a conjugated Brunnian derivative gives a new nontrivial element
in

```text
K_{n+1} cap C_{n+1}.
```

Its `X`-motion is inside `mu`-fibres and generates `mu`.

### Branch B: Conjugated-Probe Core

There is a nontrivial chief factor

```text
A/B
```

of `Gamma_n` such that

```text
B < A <= K_n cap C_n cap CPC^Gamma_n,
```

and the `X`-projection of `A` acts nontrivially inside `mu`-fibres and
generates `mu`.

Equivalently, if the conjugated-derivative branch fails cofinally, then the
remaining obstruction is exactly cofinal nontriviality of

```text
K_n cap C_n cap CPC^Gamma_n.
```

## Proof

By `deletion_null_monolith_chief_obstruction.md`, for every `m,s,N` there are
unbounded arities with a chief factor

```text
B < A <= K_n cap C_n
```

such that every nontrivial `a in A` has a Brunnian `Q`-invisible representative
and nontrivial `X`-motion generating `mu`.

Take `a in A` and choose

```text
beta_a in Brun_n cap ker rho^Q_n
```

with

```text
Phi_n(beta_a)=a.
```

For any `h in G^X_n`, choose `eta in F_{n-1}` mapping to `h`.  The conjugated
derivative

```text
D_{i,eta} beta_a=[iota(beta_a),iota(eta)tau_i iota(eta)^{-1}]
```

is Brunnian and `Q`-invisible by the lemma.  Its `X`-projection is

```text
[iota_n(p_X(a)),T_{i,h}].
```

If this commutator is nontrivial for some `(i,h)`, then Branch A holds.
Because the derivative is still `Q`-invisible, it is invisible to the
`Y_mu^0` factor and therefore acts trivially on `(X/mu)^{n+1}`.  Since its
`X`-projection is nontrivial, its coordinate mismatches generate a nontrivial
braided congruence contained in `mu`; by monolith minimality, they generate
`mu`.

If Branch A fails for every `a in A`, then

```text
[iota_n(p_X(a)),T_{i,h}]=1
```

for every `a in A`, every `i`, and every `h in G^X_n`.  Therefore

```text
p_X(a) in CPC_n(X)
```

for every `a in A`, hence

```text
A <= CPC^Gamma_n.
```

Together with `A <= K_n cap C_n`, this gives

```text
B < A <= K_n cap C_n cap CPC^Gamma_n.
```

The monolith-generation statement is inherited from the deletion-null chief
obstruction: `A <= K_n` makes the `X`-motion trivial modulo `mu`, while
`K_n cap L_n=1` makes the `X`-projection of `A` nontrivial.  The generated
coordinate-mismatch congruence is therefore nontrivial and contained in
`mu`, hence equals `mu`.

This proves the theorem.

## Consequence

The central branch is now strictly stronger than one-probe centrality.  A
surviving central obstruction must centralize every added-strand probe after
every possible old-strand last-strand motion.

A positive proof can now attack the finite-image statement

```text
K_n cap C_n cap CPC^Gamma_n=1 eventually
```

for an appropriate detector.  If this holds, the only remaining negative
route is an infinite tower of nontrivial conjugated Brunnian derivatives.

A true counterexample must therefore support one of these exact behaviours:

```text
an infinite conjugated-derivative tower of monolith-generating Brunnian
obstructions;
```

or

```text
cofinal chief factors inside K_n cap C_n cap CPC^Gamma_n.
```
