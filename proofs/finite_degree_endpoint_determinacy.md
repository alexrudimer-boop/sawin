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

## Executable Search

For fixed `I,s,N,n,c`, the check is finite.

1. Compute `A_s` by enumerating finite group tables of order at most `s` and
   all generator assignments satisfying the Artin row relations.

2. Build the residual branch automaton at arity `n`.  Since the interval is
   finite, the branch states are finite and the generators are the supported
   lifted braid moves `sigma_i^{+/-1}`.

3. Decorate each lifted generator by its full finite Artin readout, its full
   endpoint, and all bounded deletion readouts:

```text
q_s^{T_n} alpha_n,   epsilon_n,
(
  q_s^{T_J} alpha_J,
  epsilon_J
)_{|J| <= N}.
```

4. Close the finite subgroup/image `G_{I,s,N,n,c}` in the product above, storing
   one branch word for each reached element.

5. Compute the kernel of the projection forgetting only the full endpoint.  If
   an element in that kernel has nontrivial endpoint component, output its
   stored branch word.

For fixed parameters there is no hidden infinite braid-group quantifier.

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
