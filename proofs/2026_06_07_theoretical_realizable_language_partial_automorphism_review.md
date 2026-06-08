# Theoretical Review: Realizable Contextual Language and Partial Automorphisms

Date: 2026-06-07.

## Verdict

This is theorem-level progress in locating the active-lift obstruction.  It
does not prove A or B.  It explains why a direct finite partial-automorphism
extension on the full graph of forced contextual products is too strong, and
identifies the correct object: the realizable contextual language.

## Naive Partial-Automorphism Attempt

Let `P=P_X` be the two-sided contextual quotient.  For each `p in P`, the
forced products define

```text
lambda_p:D_p -> P.
```

Build a two-sorted finite structure

```text
A_X = P union {ell_p : p in P}
```

with ternary relation

```text
G(ell_p,q,r)  iff  q in D_p and lambda_p(q)=r.
```

Define a partial map

```text
theta_p(q)=lambda_p(q)              for q in D_p,
theta_p(ell_q)=ell_{lambda_p(q)}    for q in D_p.
```

If each `theta_p` were a partial automorphism of this finite structure, then
finite partial-automorphism extension machinery could be used to produce a
finite augmented-rack style completion.

## Where YBE Helps

Preservation of `G` asks for

```text
lambda_p(lambda_q(a)) =
lambda_{lambda_p(q)}(lambda_p(a)).
```

This is exactly the rack/YBE conjugacy identity

```text
p*(q*a) = (p*q)*(p*a)
```

on a jointly realizable contextual triple.  For actual local braid diagrams,
YBE proves the required identity.

## Where the Naive Structure Fails

The relation `G` contains every forced pair, including virtual products that
are pairwise forced but not jointly fillable inside a single `X`-colored word.
YBE does not control these arbitrary virtual triples, because they are not
actual local diagrams.

Thus the proof that `theta_p` is a partial automorphism of the full finite
graph `G` breaks exactly on non-fillable triples.

## Correct Object

The correct object is the realizable contextual language

```text
W_X = union_{n>=1} J_n(X^n) subseteq P^*.
```

A word `(p_1,...,p_n)` lies in `W_X` iff it is actually realized as the
contextual readout of an `X`-word.

This language is finite-state/regular because realization is witnessed by
finite monoid context data:

```text
A_{i+1}=A_i m_{x_i},
B_i=B_{i+1} r_{x_{i+1}},
p_i=[A_i,x_i,B_i].
```

On `W_X`, the local maps `theta_p` only touch realizable configurations, so
the needed identities are actual YBE diagrams.

## Current Target

The positive route now asks:

```text
Can W_X be compressed to a finite relational structure whose partial
automorphisms theta_p encode all braid-relevant contexts?
```

If yes, finite partial-automorphism extension can provide finite augmented
rack completion, after which orbit separation remains.

The negative route asks for an unbounded realizability obstruction:

```text
a virtual contextual pattern locally compatible at every bounded finite level
but not globally realizable, causing finite compression or active-lift
construction to fail.
```

This is sharper than the naive virtual-state blocker because it identifies
which language must be represented: not all forced products in `P`, only the
regular language of actually realized contextual readouts.
