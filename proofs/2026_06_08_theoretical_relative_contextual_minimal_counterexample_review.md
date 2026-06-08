# Theoretical Review: Relative Contextual Minimal Counterexample Criterion

Date: 2026-06-08.

## Verdict

This is useful theorem-level progress.  It reframes the quotient route without
requiring quotient fibres to have identical context maps.

Given any dominated braided quotient `pi:X->Z`, the combined readout

```text
K_n(x) = (pi^n(x), J_n(x))
```

is enough: if it is injective for every arity and the contextual rack
completion exists, then a finite rack dominates `X`.

The all-arity injectivity condition is finite-checkable by reachability in a
finite graph.  This is now implemented locally as

```text
relative_contextual_separation_summary(...)
```

and used in the small contextual audits.

## Theorem

Let `pi:X->Z` be a braided quotient.  Suppose:

```text
1. Z is dominated by a finite rack Y_0;
2. P_X has a finite rack completion preserving forced products, so J_n is
   braid-equivariant;
3. (pi^n,J_n):X^n -> Z^n x P_X^n is injective for every n.
```

Then

```text
Y_0 x P_X x T_2
```

dominates `X`.

If a braid is invisible to that product detector, the `Y_0` factor fixes the
quotient `Z^n`, the `P_X` factor fixes the contextual readout, and injectivity
of `(pi^n,J_n)` recovers the original `X^n` point.

## Finite Reachability Criterion

For a braided congruence `E`, build the graph with vertices

```text
(A,A',B,B',x,x') in M_L^2 x M_R^2 x X^2
```

satisfying

```text
x E x'
and
[A,x,B]=[A',x',B'] in P_X.
```

Edges encode one-step compatibility of the left and right context recursions.

Then `E` fails to be `J`-separating iff there is an initial-to-terminal path
with a mismatch flag `x_i != x_i'` at some coordinate.  Since the graph is
finite, failure has a bounded witness.

## Minimal Counterexample Consequence

If `X` is a smallest finite counterexample and contextual rack completion
exists, then every nontrivial proper braided congruence must fail this
finite `J`-separation test.  Otherwise the quotient is smaller and dominated
by minimality, and the relative contextual theorem would dominate `X`.

Thus a minimal counterexample must be:

```text
1. a contextual rack-completion failure; or
2. braided-simple; or
3. quotient-rigid: every nontrivial proper quotient has a bounded
   contextual collision.
```

## Local Evidence

The generated contextual audits now enumerate nontrivial proper congruences
in the small corpora and apply the finite reachability test:

```text
proofs/size3_contextual_completion_audit.md
proofs/two_colour_fibre2_contextual_audit.md
```

Both currently report zero skips for the proper-congruence relative separation
checks.  This is finite small-corpus evidence only, not a proof of A.
