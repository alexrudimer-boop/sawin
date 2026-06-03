# Degenerate preimage memory gate

Date: 2026-06-03

This note is the next pressure test after
`proofs/finite_derived_hurwitz_envelope.md`.  The nondegenerate guitar route
uses the derived operation

```text
a*b = lambda_a(rho_y(b)),        where lambda_b(y)=a.
```

For genuinely left-degenerate finite bijective YBE tables, the hidden
preimage `y` may be missing or nonunique.  Thus the derived rack operation is
not automatically a total function of the visible labels `(a,b)`.

## Visible fibre

For a visible pair `(a,b)`, define

```text
P(a,b) = { y in X : lambda_b(y)=a }.
```

If every `P(a,b)` is a singleton, the ordinary derived operation is defined
on visible labels.  This is the left-nondegenerate case.

If a fibre is empty, visible labels do not describe an actual pair.  If a
fibre has more than one element, the visible label has forgotten hidden
neighbour data.  For each hidden preimage `y`, the candidate output is

```text
c_y = lambda_a(rho_y(b)).
```

There are three nonsingleton statuses:

```text
missing
multiple_same_candidate
ambiguous_candidates
```

The last status is the strongest two-strand obstruction: the visible pair
`(a,b)` has two hidden neighbours producing different derived outputs.

## Finite edge-memory repair

The canonical local repair is finite:

```text
E_X = { (a,b,y) : lambda_b(y)=a }.
```

Equivalently, `E_X` is just the graph of the map

```text
(b,y) |-> (lambda_b(y), b).
```

It has exactly `|X|^2` states.  On this edge-memory state the local derived
candidate

```text
(a,b,y) |-> lambda_a(rho_y(b))
```

is a function.  Therefore preimage ambiguity is not by itself an infinite
object.  The remaining question is whether this finite local edge memory can
be propagated coherently through YBE triples and Fadell-Neuwirth
point-forgetting.

## Route consequence

The finite augmented Artin-envelope lemma would need to prove that the edge
memories form a compatible finite tower:

```text
edge-memory Hurwitz-like motion
+ coordinatewise maps in one fixed finite group
+ bounded-exponent vertical kernel.
```

A negative route should therefore look for a failure of triple or quadruple
memory consistency, not for unbounded order in `Q_X(n)`.

The first finite computations are:

```text
n=3: test whether edge memories over X^4 are stable under
     alpha_{1,4}, alpha_{2,4}, alpha_{3,4};

n=4: test whether the arity-5 edge memories forget to the arity-4
     memories compatibly with alpha_{1,5},...,alpha_{4,5}.
```

## Generated audit

The executable helper is

```text
degenerate_preimage_memory_audit(X)
```

and the generated report is

```text
proofs/degenerate_preimage_memory_audit.md
```

The report records one nondegenerate singleton-fibre witness and the
two-point identity row, where the visible derived operation is not safe but
the finite edge-memory graph still has `|X|^2` states.  This isolates the
next exact obstruction target: triple/quadruple compatibility of the finite
edge memory.
