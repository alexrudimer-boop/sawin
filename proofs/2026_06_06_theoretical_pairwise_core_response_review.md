# Review: Pairwise-Core Response

Date: 2026-06-06

Verdict: C.  The response does not prove Sawin's statement and does not give a
cofinal rack-prefix counterexample.  It gives proof-grade progress by showing
that the all-meridian symmetric commutator is contained in every pairwise
commutator subgroup.

## Theorem/Proof Progress

The pairwise-depth theorem is valid.  If `N_1,...,N_r` are normal in `G` and

```text
C=[N_1,...,N_r]_Sigma,
```

then

```text
C <= [N_a,N_b]
```

for every distinct pair `a,b`.  The proof by the lowest commutator-tree vertex
whose descendant leaves contain both `a` and `b` is correct: the two child
subcommutators lie in `N_a` and `N_b`, their commutator lies in `[N_a,N_b]`,
and normality keeps the remaining upper commutators inside `[N_a,N_b]`.

Consequently, in the finite-image setup,

```text
C_n <= D_n := intersection_{i<j}[N_{i,n},N_{j,n}].
```

Thus

```text
K_n cap D_n = 1
```

is a sufficient large-arity condition for domination after adding fixed-arity
detectors for the small arities.  This is strictly weaker than requiring
`K_n cap [N_{i,n},N_{j,n}]=1` pair-by-pair.

The central-chief-factor corollary is valid.  A central Type C chief factor
covered by `C_n` is covered by every pairwise commutator subgroup because
`C_n<=[N_{i,n},N_{j,n}]` for every pair.  If the factor is central and chief,
it is cyclic of prime order.

The relative commutator-injectivity criterion is valid as a conditional
criterion.  If `Z` is a braided quotient of `X` dominated by a finite rack
`Y_Z`, and

```text
E_n = ker(rho^X_n(F_{n-1}) -> rho^Z_n(F_{n-1}))
```

has trivial intersection with `gamma_2(rho^X_n(F_{n-1}))` in all sufficiently
large arities, then using `Q=Y_Z^0 x T_2` kills `K_n cap D_n` in large arity.
Fixed-arity rack cofinality handles the remaining small arities.

## Finite Evidence

None.  This response is purely theoretical.

## External Status

The response's statement that the public MathOverflow question currently has
no posted answer is external status, not mathematical evidence.  It should not
be used as a proof obligation or proof step.

## Heuristic Value

The result collapses the previous pairwise-or-central split into one
pairwise-core target:

```text
K_n cap intersection_{i<j}[N_{i,n},N_{j,n}] = 1.
```

It also identifies a clean quotient strategy: find a dominated quotient whose
relative kernel is disjoint from the commutator subgroup of the last-strand
`X`-image.

## Unsupported Claims

The response does not prove that every finite bijective solution has a
detector `Q` satisfying pairwise-core vanishing.

The response does not prove that every finite bijective solution has a
dominated quotient `Z` satisfying

```text
E_n cap gamma_2(G^X_n)=1
```

in large arity.

The response does not construct an explicit finite solution with cofinal
nontrivial elements in

```text
K_n cap C_n <= K_n cap D_n.
```

No bounded-arity computation is promoted to an all-arity theorem.
