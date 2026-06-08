# Theoretical Review: Binary Skew-Over-Flip Family Completion

Date: 2026-06-07.

## Verdict

This is positive finite evidence, not a proof of A or B.  It stress-tests the
four-point contextual completion against the whole nearest family containing
that example, and the same completion pattern persists throughout the
degenerate non-involutive part of the family.

The result was locally audited by:

```text
tools/run_binary_skew_flip_contextual_family_audit.py
proofs/binary_skew_flip_contextual_family_audit.json
proofs/binary_skew_flip_contextual_family_audit.md
```

## Family

The audit enumerates all binary skew-over-flip four-point maps

```text
X = {0,1} x {0,1}
R((a,i),(b,j)) = ((b,I_ab(i,j)), (a,J_ab(i,j)))
```

where each fibre map

```text
(i,j) -> (I_ab(i,j), J_ab(i,j))
```

is an arbitrary permutation of `{0,1}^2`.  There are

```text
24^4 = 331776
```

such bijective maps.

## Local Classification

The exhaustive audit gives:

```text
YBE solutions: 520
nondegenerate: 384
degenerate involutive: 64
degenerate non-involutive: 72
```

The 72 degenerate non-involutive rows are the relevant stress test for the
current contextual route.

## Contextual Completion Result

For every one of the 72 degenerate non-involutive solutions:

```text
M_L and M_R have the same underlying maps;
|M_L|=|M_R| is in {3,4,5,6};
|P| is in {10,14,16,20};
forced compatible products have no representative-independence conflicts;
every forced partial left translation is injective;
the identity fill is a rack.
```

The contextual summary is:

```text
36 cases: |M|=6, |P|=20, forced products=72, domains={2,3,8}
12 cases: |M|=5, |P|=16, forced products=60, domains={2,3,7}
 6 cases: |M|=3, |P|=10, forced products=36, domains={2,3,8}
 6 cases: |M|=5, |P|=16, forced products=60, domains={2,3,6,8}
 6 cases: |M|=4, |P|=14, forced products=48, domains={2,3,10}
 6 cases: |M|=6, |P|=20, forced products=72, domains={2,3,6,10}
```

For each row, extending a forced partial translation by closing its nontrivial
partial two-cycles and fixing all other points gives total permutations `L_p`
with:

```text
L_p^2 = 1,
L_p L_q = L_q L_p,
L_{L_p(q)} = L_q.
```

Thus

```text
p*q = L_p(q)
```

defines a finite rack on the same contextual quotient `P`.  No extra points
are needed.

## Consequence

The feared finite-totalization obstruction does not occur anywhere in this
whole four-point skew-over-flip family.  The four-point non-fillable pair is
not an accidental positive case; it belongs to a family where all genuinely
degenerate non-involutive rows admit finite contextual rack completions of
size at most 20.

The next theoretical target is sharper:

```text
Either prove that YBE-origin contextual partial translations always admit this
commuting-involution finite completion, or find a larger finite YBE solution
whose contextual partial translations cannot be completed in this way and turn
that failure into an actual Brunnian detector-kernel witness.
```
