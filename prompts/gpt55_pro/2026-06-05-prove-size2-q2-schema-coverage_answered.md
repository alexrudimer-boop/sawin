# Prove or refute unbounded q=2 schema coverage for |X|=2

We now have a bounded finite rack SAT result, not just an audit:

```text
|X| <= 2, 2 <= n <= 5, |M| <= 4, |Q| <= 4
OK 6 solutions, 18544 bad endpoint pairs, 9 detectors
certificate SHA256:
59bf0bf2957d57ff2d231bc31c799ebb9d50182d833190b3c1a4c9a8e808b3cf
```

Every bad endpoint pair found in the bound is separated by a rack of size 2.
No q=3 or q=4 rack is needed.

The two q=2 rack schemas are:

1. Identity-action rack: `T[a,b]=b`.
2. Flip-action rack: `T[a,b]=1-b`.

The bounded run found 9 concrete detector schemas using these q=2 racks and
monoids of size 1, 2, or 4.

## Task

Close the |X|=2 case, or produce the first obstruction.

Do not return another general discussion of Target A. Work directly with the
five labeled |X|=2 YBE tables:

```text
[0, 1, 2, 3]
[0, 2, 1, 3]
[1, 3, 0, 2]
[2, 0, 3, 1]
[3, 1, 2, 0]
```

and the corrected endpoint T-closure:

```text
if i < j or i > j+1:  (word,i) ~ (word',i)
if i == j:            (word,j) ~ (word',j+1)
if i == j+1:          no direct edge
```

## Required output

Give one of the following.

1. An unbounded theorem:

   For every |X|=2 bijective YBE solution, every rack-admissible partition P,
   every arity n>=2, and every principal bad endpoint pair, one of the 9 q=2
   detector schemas separates it.

   The proof must identify the invariant that reduces all arities to the
   finite schemas. It should be checkable without rerunning unbounded search.

2. A counterexample:

   Produce the first arity n>=6, YBE table, partition, paired-action element,
   start/end words and endpoint positions such that the endpoint pair is bad
   and invisible to all 9 q=2 schemas. Include detector values under all 9
   schemas.

3. A finite-state reduction:

   If a full proof is too hard, build a finite automaton/monoid-recognizer
   whose accepted language is exactly the bad endpoint pairs invisible to the
   9 schemas. Then either prove the language empty or emit the shortest word.

Rules:

- Do not use associated groups.
- Do not claim "no bad triples"; bad triples exist already in arity 2.
- Do not treat bounded no-detector as true residual collapse.
- Use the corrected endpoint T-closure with context-only moves.
