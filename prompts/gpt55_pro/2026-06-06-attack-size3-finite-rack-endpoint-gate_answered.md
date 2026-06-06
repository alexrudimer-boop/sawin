# Attack the size-three finite-rack endpoint gate

The \(|X|=2\) endpoint-gate problem is closed:

- all five labeled two-point bijective YBE tables are classified;
- each is finite-rack dominated;
- the nine q=2 endpoint detector schemas from the bounded search cover all
  arities;
- there is no arity \(n\ge6\) obstruction.

Do not re-audit \(|X|=2\). Move to \(|X|=3\).

## Task

Produce one of the following concrete outputs for \(|X|=3\).

1. A theorem closing a substantial branch.

   Examples:
   - all permutation-form solutions on three points are finite-rack dominated;
   - all rack or involutive branches have endpoint-gate coverage by explicit
     detector schemas;
   - a complete finite-rack domination proof for a named nonrack family.

2. A bounded finite-rack SAT run with verifier-level certificate fields.

   Use explicit bounds:

   ```text
   |X| = 3
   arity n <= N
   |M| <= K
   |Q| <= qmax
   ```

   The output must include the YBE table, partition, endpoint pair, monoid,
   rack table, assignment, and a clear unresolved/resolved classification.

3. A genuine obstruction candidate.

   This must not be "no detector found up to bounds" unless it includes
   monoid/rack catalog hashes and unsat certificates. Prefer a smallest
   endpoint pair invisible to all detected schemas, with values under every
   known detector.

4. A finite-state reduction.

   Build a finite automaton/monoid recognizer for a nontrivial \(|X|=3\)
   family whose accepted language is exactly the bad endpoint pairs invisible
   to a proposed finite detector family. Then prove the language empty or emit
   the shortest accepted word.

## Rules

- Do not use associated groups as a primary detector.
- Do not return a general Target A/Target B audit.
- Do not claim global Sawin.
- Every positive detector must be rack-valued and check the contextual T/R
  relations.
- Every negative result must distinguish bounded no-detector from true
  residual collapse.

## Required output

A theorem, counterexample, or finite certificate program that moves the
\(|X|=3\) frontier. The answer should be usable directly as a new proof-log
checkpoint or implementation target.
