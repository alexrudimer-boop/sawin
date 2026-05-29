# Hereditary domination closure

Date: 2026-05-28

This note records two all-degree heredity facts for Sawin finite-rack
domination.  They do not prove the Master Local-Minimal Residual Theorem, but
they sharpen both the positive induction and the counterexample search.

## Quotients

Let

```text
pi : X -> Z
```

be a surjective braided-set homomorphism of finite bijective YBE solutions.
For every braid `beta in B_n` and every tuple `x in X^n`,

```text
pi^n(rho_{X,n}(beta)(x))
  =
rho_{Z,n}(beta)(pi^n(x)).
```

This is immediate for one braid generator from the homomorphism condition,
and then follows for every braid word by induction on word length, including
negative generators because all crossings are bijective.

Consequently,

```text
ker rho_{X,n} subset ker rho_{Z,n}.
```

If a finite rack `Y` dominates `X`, then

```text
ker rho_{Y,n} subset ker rho_{X,n} subset ker rho_{Z,n}
```

for every `n`, so the same `Y` dominates every quotient `Z`.

The contrapositive is useful for outcome B: if a quotient `Z` is not
dominated by any finite rack, then neither is `X`.  In practice one would
state the smaller quotient `Z` as the explicit counterexample.

## Subsolutions

Let `S subset X` be a nonempty subset such that

```text
R_X(S x S) subset S x S.
```

Since `R_X` is injective and `S x S` is finite, the restricted map is a
bijection `S x S -> S x S`.  The Yang-Baxter equation restricts from `X^3`
to `S^3`, so `S` is a finite bijective YBE solution.

For every braid word, the action of `X` on tuples in `S^n` agrees with the
action of the restricted solution `S`.  Therefore

```text
ker rho_{X,n} subset ker rho_{S,n}.
```

If `Y` dominates `X`, then `Y` also dominates `S`.  Thus any undominated
subsolution is already a counterexample, and any minimal B counterexample
may be assumed to have no proper undominated subsolution.

## Consequences For The Search

These closure facts are all-`n` kernel inclusions, not finite search.

They imply that a genuine minimal counterexample should be simultaneously:

- quotient-minimal among braided-set homomorphic images; and
- subsolution-minimal among crossing-closed subsets.

They also explain why the congruence-chain reduction loses no generality.
If a quotient interval or subobject already carries a normalized-law
obstruction sequence, the larger solution cannot be rescued by adding extra
points or refining fibres.

## Executable Convention Checks

The helper `is_subsolution_subset(X,S)` checks crossing closure, and
`subsolution(X,S)` builds the restricted finite braided set.  Regression
tests verify that restricted braid actions agree with the ambient action and
that nonclosed subsets are rejected.

For quotients, `QuotientMap` already validates the crossing-level
homomorphism.  A regression test verifies the braid-word consequence:
projecting the total braid action through `pi` agrees with applying the
quotient braid action after projection.
