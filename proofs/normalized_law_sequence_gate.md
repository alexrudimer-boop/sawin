# Normalized-law sequence gate

Date: 2026-05-29

This note records the precise all-finite-group law condition needed on the
B side.  It is not a counterexample: it supplies only the invisibility half of
the normalized-law obstruction.  A final B proof must also provide a fixed
finite YBE solution, base-kernel membership, and explicit moved tuples.

## Prefix Law Condition

Let `w_j` be a sequence of free-group words.  A convenient sufficient
condition for eventual laws on every finite group is:

```text
w_j is a law on every finite group of order at most j.
```

Then every fixed finite group `G` eventually satisfies the sequence.  Indeed,
if `|G|=m`, then for every `j >= m`, the group `G` is among the groups of
order at most `j`, so `w_j` is a law on `G`.

This is the exact quantifier needed in the normalized-law B route:

```text
for every finite group G, w_j is eventually a law on G.
```

The condition is stronger than necessary, but it is easy to audit and is
stable under replacing a finite list of test groups by a complete symbolic
argument for all groups of bounded order.

## Pure-Braid Consequence

Embed `w_j` into a pure braid by

```text
beta_j = w_j(A_{1,k+1},...,A_{k,k+1}),
```

as in `proofs/pure_braid_law_embedding.md`.  If `w_j` is eventually a law on
`G`, then the law-longitude lemma gives

```text
Lambda_{G,k+1}(beta_j)=Lambda_{G,k+1}(1)
```

eventually.  If the arity or braid degree is also made to grow, the
right-stabilization lemma from `proofs/diagonal_normalized_obstruction.md`
keeps the old longitude data intact while forcing `q_j -> infinity`.

Thus a B construction may use this pattern for the finite-group invisibility
side, but it still must prove nontrivial motion in the fixed finite YBE
action after the same embedding.

## Executable Prefix Audit

The helper

```text
law_sequence_prefix_audit(groups, words, arity, start_index=1)
```

checks a supplied finite prefix.  For the word at index `j`, it tests only the
listed groups whose order is at most `j`.  It records one row per checked
pair:

- index `j`;
- group name;
- group order;
- whether the word is a law on that group.

The flag

```text
all_required_prefix_laws_hold
```

means the supplied finite prefix passes against the supplied finite group
list.  This remains a diagnostic; an actual B proof needs an infinite
symbolic construction of `w_j` satisfying the prefix law condition for all
finite groups of order at most `j`.

## Guardrail

Exponent words

```text
x^{lcm(1,...,j)}
```

satisfy the prefix law condition, because every element order in a group of
order at most `j` divides `lcm(1,...,j)`.  The existing
`proofs/normalized_law_attempts.md` explains why that alone is not a
counterexample: pure powers also become trivial on any fixed finite braid
action image.  A successful B route needs non-power or moving-image laws that
pass this prefix gate while still moving explicit tuples.
