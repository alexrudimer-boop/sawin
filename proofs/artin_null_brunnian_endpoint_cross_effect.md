# Artin-null Brunnian endpoint cross-effect

Date: 2026-06-04

This note sharpens the bounded-width/no-high-arity endpoint question from
`proofs/completed_context_finite_artin_separation.md`.  It separates an
ordinary high-arity Brunnian endpoint gap from the stronger profinite
Artin-null obstruction that is actually equivalent to a normalized-law
no-rack sequence.

## Completed-context loop groups

Fix one actual completed-context interval.  For arity `n` and base context
`c`, let

```text
L_n(c)
```

be the group of actual residual braid branches based at `c`; equivalently it
is the loop group of the actual completed-context path category at `c`.  The
loop group has two readouts:

```text
alpha_n:   L_n(c) -> Art_I^{T_n},
epsilon_n: L_n(c) -> U.
```

Here `Art_I` is the universal Artin row group of the interval, `T_n` is the
finite set of terminal Artin slots in arity `n`, and `U` is the finite endpoint
unit group.

For each survivor subset

```text
J subset {1,...,n},
```

actual strand-forgetting gives a Fadell-Neuwirth deletion functor

```text
d_J: L_n(c) -> L_J(d_J c)
```

whenever the retained branch is supported.

## Bounded-deletion kernels

For a width bound `N`, define the bounded endpoint-deletion kernel by

```text
K_{n,N}(c)
  =
intersection_{J subset {1,...,n}, |J| <= N}
ker(epsilon_J d_J).
```

Thus `gamma in K_{n,N}(c)` has endpoint-trivial deletion shadow on every
survivor subset of size at most `N`.

The stronger bounded Artin-and-endpoint deletion kernel is

```text
K^{alpha,epsilon}_{n,N}(c)
  =
intersection_{J subset {1,...,n}, |J| <= N}
ker((alpha_J,epsilon_J) d_J).
```

Its elements have trivial endpoint and trivial Artin readout on every
bounded deletion shadow.

## Brunnian endpoint cross-effects

The ordinary Brunnian endpoint cross-effect is

```text
BrEnd_{n,N}(c) = epsilon_n(K_{n,N}(c)) <= U.
```

The Artin-shadow version is

```text
BrEnd^alpha_{n,N}(c)
  =
epsilon_n(K^{alpha,epsilon}_{n,N}(c)) <= U.
```

These groups measure high-arity endpoint units that become invisible under
all bounded Fadell-Neuwirth deletions.  They are endpoint analogues of
Brunnian pure-braid cross-effects.

## Bounded-width theorem

The bounded-width endpoint theorem is exactly the assertion that, for some
finite width depending only on the interval,

```text
exists N=N(I) such that
for all n,c,     BrEnd_{n,N}(c)=1.
```

Equivalently, every actual residual branch with nonidentity endpoint has a
nontrivial endpoint deletion shadow on at most `N` active strands.

The stronger Artin-shadow version asks for

```text
exists N=N(I) such that
for all n,c,     BrEnd^alpha_{n,N}(c)=1.
```

YBE cube coherence and Fadell-Neuwirth deletion compatibility make the maps
and diagrams well-defined, but they do not by themselves prove either
vanishing statement.  The ordinary Brunnian phenomenon leaves room for
branches whose every bounded deletion shadow is endpoint-trivial.

## Why ordinary Brunnian endpoints are not enough

Nonvanishing of `BrEnd_{n,N}(c)` for arbitrarily large `n` is only a gap.  A
high-arity Brunnian endpoint may still be detected by one fixed finite Artin
quotient

```text
q: Art_I -> H.
```

In that case it has no bounded deletion witness, but the detector rack still
sees it through `q^T alpha_n(gamma)`.

Thus:

```text
unbounded ordinary Brunnian endpoint cross-effect
does not imply
failure of finite rack domination.
```

## Profinite Artin-null Brunnian endpoint language

For a nonidentity endpoint value `u in U`, define the bounded Artin-null
Brunnian endpoint language

```text
W^{Br}_{u,N}
  =
{ alpha_n(gamma) :
    gamma in L_n(c) for some n,c,
    epsilon_n(gamma)=u,
    gamma in K^{alpha,epsilon}_{n,N}(c) }.
```

This is the language of actual branches with endpoint `u` whose every
`N`-strand deletion shadow has trivial endpoint and trivial Artin readout.

The exact high-arity no-rack obstruction is:

```text
1 in intersection_{N >= 1} closure(W^{Br}_{u,N})
```

in the profinite topology induced by all finite quotients of the relevant
terminal Artin groups.

Equivalently, for every finite list of finite detector groups
`G_1,...,G_m` and every width `N`, there is an actual residual branch `gamma`
such that

```text
epsilon(gamma)=u != 1,
((alpha_J,epsilon_J) d_J)(gamma)=1   for every |J| <= N,
```

and the full Artin readout `alpha(gamma)` is killed by every evaluation into
every `G_i`.

## Equivalence with normalized-law no-rack sequences

If the profinite Artin-null Brunnian obstruction holds for some `u != 1`,
enumerate the finite groups as

```text
G_1,G_2,...
```

For `m`, choose `N=m` and an actual residual branch `gamma_m` invisible to
`G_1,...,G_m` with endpoint `u`.  Let

```text
beta_m in B_{n_m}
```

realize `gamma_m`, stabilizing by unused strands if needed so that
`n_m -> infinity`.  Then every fixed finite group eventually sees identity
recursive-longitude data, while the endpoint value `u` moves the chosen
residual tuple.  This is the normalized-law no-rack obstruction sequence.

Conversely, any normalized-law no-rack sequence whose moving coordinate lies
in this interval has, after passing to a subsequence, one nonidentity endpoint
value `u`.  Its Artin readouts put `1` in the profinite closure of the
corresponding Artin-null Brunnian endpoint languages.

Therefore:

```text
unbounded ordinary Brunnian endpoint cross-effect
is not equivalent to a no-rack obstruction;

unbounded profinite Artin-null Brunnian endpoint cross-effect
is equivalent to the normalized-law no-rack obstruction.
```

## Current fork

The deletion/Fadell-Neuwirth pressure test is now:

```text
bounded-width endpoint theorem
  => positive finite-rack domination route;

profinite Artin-null Brunnian endpoint obstruction
  => negative finite-rack domination route;

ordinary high-arity Brunnian endpoint obstruction alone
  => neither conclusion.
```

This is consistent with the direct endpoint-language fork: the decisive
negative condition remains profinite Artin-null nonseparation for actual
braid-realizable branches, not merely the existence of high-arity branches
with endpoint-trivial bounded deletion shadows.
