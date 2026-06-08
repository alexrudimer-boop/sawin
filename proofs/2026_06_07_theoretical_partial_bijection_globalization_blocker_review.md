# Review: Partial-Bijection Globalization Blocker

Date: 2026-06-07

Verdict: no A/B.

This response did not prove Sawin's finite-rack domination statement and did
not construct a fixed finite counterexample.  It identified why the standard
finite globalization theorem for partial bijections does not immediately solve
the inverse-semigroup totalization blocker.

## Positive Blocker

The natural idea is to extend the finite contextual partial translations to
total permutations on a finite enlargement, then define a finite augmented rack
by

```text
(omega,g) * (eta,h) = (g eta, g h g^(-1)).
```

This would solve the current blocker if the forced contextual identities

```text
L_{a*b}=L_a L_b L_a^(-1)
```

could be preserved as total permutation identities while extending all
realizable partial translations.

The failure is that finite globalization theorems for partial bijections
preserve coherent partial compositions.  They do not automatically preserve
arbitrary quotient-group relations in the contextual Wirtinger group.
Non-fillable contextual states make the relation words partially undefined;
passing to total permutations erases the domain idempotents that record where
those words were valid.

Thus the missing theorem is still a finite quotient/separability assertion for
YBE-origin contextual data:

```text
the contextual Wirtinger relations must survive finite totalization of the
partial bijections without collapsing the realizable readout.
```

No proof was given.

## Negative Blocker

The four-point degenerate example gives real fiber monodromy and non-fillable
contextual pairs, but still no actual cofinal braid witnesses.  A negative
answer needs, for every finite rack detector `Q`, an actual braid

```text
beta in Brun_n cap ker rho^Q_n
```

with

```text
rho^X_n(beta) != 1.
```

The powered-meridian witnesses cannot be frozen to one finite target because
the target has fixed two-strand pure order, and rack prefixes with compatible
pure orders kill those witnesses on `X`.

