# Theoretical Review: Four-Point Contextual Completion

Date: 2026-06-07.

## Verdict

This response gives genuine positive progress on the contextual route.  It
does not prove A for all finite bijective YBE solutions, and it does not give
B.  But it removes the checked four-point degenerate example as a candidate
obstruction to finite contextual totalization.

The result was locally audited by
`tools/run_four_point_contextual_completion_audit.py`, which generated:

```text
proofs/four_point_contextual_completion_audit.json
proofs/four_point_contextual_completion_audit.md
```

The audit reconstructs the contextual quotient, the rack completion, and the
contextual readout checks.

## Four-Point Result

For the four-point degenerate solution on

```text
00, 01, 10, 11
```

with

```text
R((a,i),(b,j))=((b,I),(a,J))
```

where

```text
(I,J)=(i,j)       if (a,b)=(0,0),
(I,J)=(j,i)       if (a,b)=(0,1) or (1,0),
(I,J)=(j,1-i)     if (a,b)=(1,1),
```

the two-sided contextual quotient

```text
P = (M x X x M) / ~
```

has 20 classes.  The forced compatible products extend to a total rack on
these 20 classes.

The local audit verifies:

```text
source YBE: true
contextual monoid size: 6
contextual quotient classes: 20
forced product conflicts: 0
rack size: 20
rack YBE: true
rack-form check: true
forced partial translations extend to permutations: true
equivariance checked arities: 1..8
orbit-injectivity checked arities: 1..8
```

The deterministic class labels in the audit differ from the labels in the
response, but the structure matches: the nontrivial left translations are only
paired transpositions, and every forced partial translation is preserved.

## Consequence

The earlier non-fillable contextual pair in this four-point example is not an
obstruction.  It is a virtual state issue that can be filled harmlessly in this
case: no new classes are needed, and no two contextual classes are collapsed.

The contextual readout

```text
J_n(x_1,...,x_n)=([A_i,x_i,B_i])_i
```

is braid-equivariant.  The response also gives an all-arity orbit-separation
argument for this particular example by classifying braid orbits:

1. no base-`1` entries gives singleton orbits;
2. exactly one base-`1` entry preserves the ordered zero-fibre string and the
   one-fibre;
3. at least two base-`1` entries preserves the ordered zero-fibre string and
   makes one-fibres transitive.

Together with the readout's base and one-fibre separation properties, this
proves that the 20-element rack dominates this particular four-point `X`.

## Remaining Gap

The all-arity problem is now more pointed:

```text
Does every finite bijective YBE solution have a finite contextual quotient
whose forced partial translations admit a finite total rack completion
preserving orbit-injectivity of the contextual readout?
```

The four-point example supports this positive route.  It does not prove the
general finite totalization/separability theorem, and it does not produce a
fixed finite counterexample.

Future prompts should stop treating the four-point non-fillable pair as a
candidate obstruction.  Instead, they should ask either to generalize this
20-class completion mechanism, or to find a new finite YBE-origin contextual
partial rack where no finite orbit-separating rack completion exists.
