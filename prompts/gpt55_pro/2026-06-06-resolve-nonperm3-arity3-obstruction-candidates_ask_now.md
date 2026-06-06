# Resolve the non-permutation |X|=3 arity-3 obstruction candidates

The non-permutation \(|X|=3\), arity-3 endpoint-gate checkpoint produced:

```text
non-permutation YBE tables:        55
arity-3 bad endpoint pairs:     37692
positive finite rack detectors: 37476
unresolved candidates:            216
```

Do not rerun the whole survey unless needed. The next move is to close the
216-candidate frontier.

## First target

Start with the smallest unresolved candidate:

```text
ybe_table = [0,3,6,1,4,7,5,2,8]
partition = [0,0,0]
arity = 3
braid_word = [1,0]
e  = word [0,0,2], position 2 = [00,2,epsilon]
e' = word [2,0,0], position 0 = [epsilon,2,00]
```

The table is rack-form:

```text
r(x,y)=(x ▷ y,x)
0 ▷ y = y
1 ▷ y = y
2 ▷ 0 = 1
2 ▷ 1 = 0
2 ▷ 2 = 2
```

The braid path is:

```text
(0,0,2) --sigma_1--> (0,2,0) --sigma_0--> (2,0,0)
```

The indiscrete quotient makes the endpoints quotient-equivalent, while the
corrected endpoint T-closure in X does not identify them.

Known detector schemas for this YBE table are all invisible:

```text
D4: q=3, M=truncated length 1, endpoint values [2,2]
D5: q=2, M=truncated length 1, endpoint values [1,1]
D6: q=3, M=truncated length 2, endpoint values [0,0]
D7: q=3, M=truncated length 2, endpoint values [1,1]
```

## Required outcome

Produce one of the following, in this order of preference:

1. A positive finite rack detector for the displayed candidate.

   It may use a new finite quotient \(M\), a larger rack \(Q\), or a detector
   schema not present in the q<=4 checkpoint. Give the full monoid table, rack
   table, alpha assignment or formula, and check every contextual T/R relation.

2. A parametric strong-collapse proof for the displayed candidate.

   Give the actual rack equations, T-equivalences, and cancellation/self-
   distributivity steps. This must prove equality in every rack-valued detector,
   not merely in the current bounded catalog.

3. A batch theorem resolving all 216 unresolved candidates.

   This may classify them into positive detectors and strong collapses, but it
   must keep the classifications separate.

4. A real bounded negative certificate.

   This requires exhaustive monoid/rack catalogs for stated bounds and attached
   unsat proofs. Do not call a candidate residual collapse without a parametric
   proof over all finite racks.

## Rules

- Use rack-valued detectors only; no associated-group shortcut.
- Do not promote "not found by q<=4" to a negative theorem.
- If using the truncated length-2 monoid, verify associativity and every
  structure relation.
- If using a new monoid quotient, prove it is a quotient of the structure
  monoid for the displayed table.
- If the first candidate resolves by symmetry into the other 215 candidates,
  state the symmetry action and give verifier-level representatives.

## Desired output

A theorem/certificate that actually closes at least the displayed candidate,
and preferably the full 216-candidate frontier.
