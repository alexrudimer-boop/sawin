# Attack the non-permutation |X|=3 endpoint gate

The permutation-form \(|X|=3\) branch is closed:

```text
n >= 4: separated by D_{sigma,tau}
n = 2: positive finite rack detectors with |M|=5 and |Q|<=3
n = 3: strong left-cancellation collapse
unresolved: 0
```

Do not re-open the permutation-form branch.

## Task

Move to the non-permutation \(|X|=3\) finite-rack endpoint gate.

Produce one of the following:

1. A branch theorem closing a named non-permutation family.

   The theorem must specify the family, the detector/collapse mechanism, and
   the exact arity range. It should include verifier-level local checks.

2. A bounded finite-rack SAT certificate run.

   Include explicit bounds:

   ```text
   |X| = 3
   non-permutation-form tables only
   arity n <= N
   |M| <= K
   |Q| <= qmax
   ```

   Positive detector records must include the YBE table, partition, endpoint
   pair, monoid quotient, rack table, alpha assignment, and endpoint values.

3. A strong-collapse theorem or family of witnesses.

   If a pair is collapsed, give the actual contextual relations and
   \(T\)-equivalences reducing to rack injectivity/cancellation.

4. A genuine obstruction candidate.

   This must not be merely "no detector found up to bounds" unless it includes
   catalog hashes and unsat certificates. Do not call bounded no-detector
   residual collapse.

## Rules

- Do not use associated groups as a primary detector.
- Do not claim global Sawin.
- Keep positive detectors rack-valued and verify contextual T/R relations.
- Separate positive detector, strong collapse, bounded negative, and true
  residual collapse classifications cleanly.

## Required output

A theorem, certificate batch, or smallest obstruction candidate for the
non-permutation \(|X|=3\) frontier.
