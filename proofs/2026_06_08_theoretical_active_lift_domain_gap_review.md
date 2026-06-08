# Theoretical Review: Active-Lift Domain Gap

Date: 2026-06-08.

## Verdict

Correction, 2026-06-08: this note used the earlier `C^(infty)` terminology.
That fixed-point formulation is superseded: the proposed pruning operator is
not monotone in the needed sense.  The correct statement is that active-lift
existence is a finite CSP; a singleton identity-extension active system is a
valid certificate when it exists.

This response does not prove A or B.  It restates the exact obstruction in
the active-lift route and the fixed-target obstruction in the negative route.

It is useful mainly as a guardrail: the next theoretical prompt should not ask
for another explanation of the virtual-domain gap.  It should ask for a proof
that the active-lift CSP is always satisfiable, or for an explicit finite
solution where it is unsatisfiable.

## Positive Route Gap

For the contextual quotient `P_X`, the forced partial left translations are

```text
lambda_p : D_p -> P_X.
```

The canonical multi-copy rack route requires nonempty active lift sets

```text
C_p subseteq Sym(P_X)
```

for every contextual class `p`, satisfying forced extension and forced-pair
closure.

The attempted direct closure proof would need:

```text
g extends lambda_p,
h extends lambda_q,
q in D_p
  => g h g^{-1} extends lambda_{lambda_p(q)}.
```

Let `r0=lambda_p(q)`.  To verify that `g h g^{-1}` extends
`lambda_{r0}`, one must check, for every `r in D_{r0}`, that

```text
g^{-1}(r) in D_q
and
h g^{-1}(r) in D_p.
```

These are domain or joint-fillability conditions.  YBE proves the corresponding
identity only when the triple `(p,q,g^{-1}(r))` is realized by an actual
three-strand contextual configuration.  It does not by itself prove the
conditions for virtual contextual states.

Thus the direct proof of active-lift CSP satisfiability is still missing.

## Negative Route Gap

The available detector-survival construction still varies the target with the
detector:

```text
X_Q = Conj(A_l), with l not dividing e(Q).
```

This does not give a fixed counterexample.  For a fixed finite target `X`, the
two-strand pure order

```text
d = ord(rho^X_2(sigma_1^2))
```

is fixed.  Rack prefixes can include detectors with pure orders divisible by
`d`, which neutralizes the powered-meridian Brunnian words on `X` as well.

No replacement fixed-target cofinal Brunnian witness family is supplied.

## Consequence

The next useful theoretical step is one of:

```text
1. prove a structural invariant that gives nonempty active-lift sets for every
   finite bijective YBE solution X;
2. find an explicit finite X and an unsatisfiability certificate for the
   active-lift CSP;
3. bypass local one-strand contextual readouts with a genuinely multi-strand
   finite rack detector and prove all-arity domination;
4. construct a fixed finite X with actual cofinal Brunnian detector-kernel
   witnesses.
```

Repeating that YBE only controls jointly realizable triples is not progress
unless it is converted into one of those four outcomes.
