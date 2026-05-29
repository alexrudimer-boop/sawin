# Semisplit congruence families

Date: 2026-05-28

This note records the exact local condition checked by
`LocalInterval.semisplit_families()`.  It is not a proof of the Master
Local-Minimal Residual Theorem, but it prevents a common invalid shortcut:
discarding semisplit families by looking only at the quotient colours.

## Setup

Let

```text
R_Z(a,b) = (c,d)
T_{a,b}: A_a x A_b -> A_c x A_d
```

be one local table entry.  For a subset `S` of colours, define the semisplit
family

```text
theta^S_t = universal on A_t   if t in S,
theta^S_t = equality on A_t    if t notin S.
```

The family is admissible exactly when, for every colour pair `(a,b)`, the
bijection `T_{a,b}` transports the product relation
`theta^S_a x theta^S_b` onto `theta^S_c x theta^S_d`.

Equivalently, writing

```text
T_{a,b}(x,y) = (U(x,y), V(x,y)),
```

the following dependency constraints hold for every `(a,b)`.

## Local dependency criterion

Case 1: `a notin S` and `b notin S`.

The source product relation is equality on `A_a x A_b`.  Therefore the target
relation must also be equality on the image.  Unless a target fibre is a
singleton, this forces `c notin S` and `d notin S`.  In general the exact
condition is:

```text
(U(x,y),V(x,y)) ~ (U(x',y'),V(x',y')) in theta^S_c x theta^S_d
iff
(x,y) = (x',y').
```

Case 2: `a in S` and `b notin S`.

The source identifies all pairs with the same second coordinate `y`.  Thus
the target relation must identify exactly the images of such fibres.  For
example, if `c in S` and `d notin S`, then `V(x,y)` must depend only on `y`,
and the induced map on the quotient coordinate must be bijective in the exact
relation-size sense.  The other placements of `c,d` are analogous.

Case 3: `a notin S` and `b in S`.

This is the left/right analogue of Case 2: the source identifies all pairs
with the same first coordinate `x`, so the target must identify exactly the
corresponding images.

Case 4: `a in S` and `b in S`.

The source relation is universal on `A_a x A_b`.  The target relation must be
universal on `A_c x A_d`.  With non-singleton fibres this typically forces
`c in S` and `d in S`; with singleton degeneracies the exact relation equality
above is the safe formulation.

## Boolean constraint form

The same relation-level condition can be written as an exact finite Boolean
CSP over the quotient colours.  Assign each colour a bit

```text
epsilon_t = 0  means equality on A_t,
epsilon_t = 1  means universal on A_t.
```

For every coloured crossing `(a,b) -> (c,d)`, define the allowed-pattern set

```text
C_{a,b} subset {0,1}^4
```

by including exactly those tuples

```text
(epsilon_a, epsilon_b, epsilon_c, epsilon_d)
```

for which `T_{a,b}` transports
`theta_a^{epsilon_a} x theta_b^{epsilon_b}` onto
`theta_c^{epsilon_c} x theta_d^{epsilon_d}`.  A semisplit family is
admissible exactly when its colour-bit assignment satisfies every row
constraint `C_{a,b}`, after translating the bits back to actual fibre
partitions and discarding the all-equality and all-universal relation
families.

This formulation is exact even with singleton fibres.  It is not a graph
connectivity shortcut: each row is computed by comparing product relations
through the actual local bijection `T_{a,b}`.

## Consequence for local minimality

A local interval is not local-minimal if any proper nonempty `S` satisfies the
criterion for all colour pairs.  This includes cases where the quotient colour
graph looks connected: a fibre-coordinate dependency in `T_{a,b}` can still
transport an equality/universal mixture correctly.

Therefore any proof of the master theorem must either:

- use local-minimality after explicitly excluding all semisplit `S`; or
- prove that its construction remains valid even when such an `S` exists.

The current reduction program requires the first route.

## Exact lemma used by the reduction

The semisplit check is not a separate hypothesis and not a finite-search
shortcut.  It is a finite subfamily of the same admissible-congruence-family
condition that defines local-minimality.

For each subset `S` of colours, the equality/universal family `theta^S` is a
legitimate congruence family.  If it is admissible and is not equal, as a
family of relations, to the all-equality or all-universal family, then the
interval is not local-minimal by definition.  Conversely, when an interval is
proved local-minimal, every semisplit `theta^S` has already been excluded,
because every admissible family has to be one of the two extremes.

Singleton fibres require this relation-level formulation.  On a singleton
fibre, equality and universal partitions coincide, so a subset `S` can look
proper at the colour level while producing exactly the all-equality or
all-universal relation family.  Such a subset is not a genuine semisplit
obstruction.  The implementation canonicalizes partitions and excludes the
two extreme relation families after deduplicating them, so singleton
degeneracies do not create false semisplit failures.

## Executable witness audit

`LocalInterval.semisplit_audits()` enumerates every equality/universal mixture
except the all-equality and all-universal extremes.  For each mixture it
records either:

- `admissible = true`; or
- a concrete colour pair `(a,b)`, target pair `(c,d)`, side of the failed
  relation comparison, and witness relation element showing that
  `T_{a,b}(theta_a x theta_b)` is not `theta_c x theta_d`.

Thus a local-minimality audit can report not only that no semisplit family is
admissible, but also that each candidate mixture has an explicit failed
transport witness.

`LocalInterval.semisplit_constraint_rows()` records the Boolean CSP row
`C_{a,b}` for every coloured crossing, and
`LocalInterval.semisplit_boolean_assignments()` returns exactly the satisfying
non-extreme assignments after canonicalizing the corresponding relation
families.  This gives an independent, table-shaped view of the same semisplit
gate used by `semisplit_audits()`.

The tests now also check that admissible semisplit families are contained in
the full `admissible_congruence_families()` enumeration, and that singleton
fibres do not create fake semisplit families.  This keeps the semisplit audit
locked to the actual local-minimality definition rather than to a colour-level
shortcut.
