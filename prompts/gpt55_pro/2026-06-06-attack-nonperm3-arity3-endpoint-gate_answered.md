# Attack the non-permutation |X|=3 arity-3 endpoint gate

The non-permutation \(|X|=3\), arity-2 endpoint gate is closed:

```text
non-permutation YBE tables: 55
arity-2 bad endpoint pairs: 2064
positive finite rack detectors: 2064
unresolved: 0
|M| = 5
|Q| <= 3
```

Do not re-open arity 2.

## Task

Move to the non-permutation \(|X|=3\), arity-3 endpoint gate.

Produce one of:

1. A complete arity-3 certificate batch.

   For every non-permutation-form \(|X|=3\) bijective YBE table, every
   rack-admissible partition \(P\), and every arity-3 principal bad endpoint
   pair, classify it as:

   - positive finite rack detector;
   - strong contextual rack collapse;
   - bounded no-detector with unsat certificates;
   - genuine residual collapse with a parametric proof.

2. A branch theorem for a large arity-3 subfamily.

   Include explicit detector/collapse mechanisms and verifier-level local
   checks.

3. A smallest obstruction candidate.

   This must include the YBE table, partition, endpoint pair, and values under
   all known detector schemas. Do not call it residual collapse without a
   parametric proof.

## Rules

- Use rack-valued detectors only; no associated-group shortcut.
- Keep positive detector, strong collapse, bounded negative, and residual
  collapse classifications separate.
- If using the universal 5-element monoid from arity 2, verify every
  contextual \(T/R\)-relation.
- If using left-cancellation collapse, give the actual \(R\)-relations and
  \(T\)-equivalences.

## Required output

A theorem, certificate batch, or smallest obstruction candidate that moves the
non-permutation \(|X|=3\), arity-3 frontier.
