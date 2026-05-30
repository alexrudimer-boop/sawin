# Two-sided unit collapse

Date: 2026-05-29

This note refines the last constant-observer universal-continuation case.  It
does not prove the Master Local-Minimal Residual Theorem.  It removes the
two-sided unit half of the remaining lower-row obstruction and isolates the
only surviving shape as mixed-unit context recovery.

## Current final case

The constant-observer continuation corridor is the case

```text
Theta^cont = Nabla
K^O = Nabla.
```

Continuation changes generate the universal local congruence, while every
currently certified Green, Schutzenberger, atom, quotient, known-branch, or
unit observer is fibrewise constant.  The local target is still to construct
one finite interval-level group `G(pi,Q)`, independent of braid index, such
that

```text
Lambda_{G(pi,Q),n}(beta)=Lambda_{G(pi,Q),n}(1)
  => Delta_n(beta)=1.
```

The prior continuation notes closed strand-continuing lower gauge by
transport-state rackification and ruled out nonunit/reset-like continuation
words as the final moving residual permutation branch.  This note splits the
remaining lower rows by coordinate-section units.

## Coordinate sections

For one remaining lower local row

```text
R_{a,b}(x,y) = (u,v),
```

write the two coordinate sections as

```text
L_x^{a,b}: y |-> u,
R_y^{a,b}: x |-> v.
```

The row is **two-sided unit** if every section `L_x^{a,b}` and every section
`R_y^{a,b}` is a bijection between the corresponding finite source and target
fibres.

## Lemma: two-sided unit rows are closed by the known nondegenerate branch

If every row in the remaining lower interval is two-sided unit, then the lower
interval is locally nondegenerate and is already in a closed branch.

Proof.  Two-sided unit means exactly that both coordinate actions are
bijective in the usual finite nondegenerate set-theoretic YBE sense:

```text
for all x,  y |-> pr_1 R(x,y) is bijective,
for all y,  x |-> pr_2 R(x,y) is bijective.
```

The local table is already a finite bijective coloured YBE row.  Adding
two-sided coordinate bijectivity makes the lower residual layer locally
nondegenerate.  The nondegenerate/guitar branch is one of the already closed
finite-`G` measurable branches in this workspace.  Hence a genuine
`bi_free_universal_corridor_bottleneck` interval cannot have all remaining
lower rows two-sided unit as its unresolved obstruction.  QED.

## Consequence for the final continuation case

The constant-observer universal-continuation case now splits into three
possibilities.

1. **Strand-continuing.**  If the lower row has rack form

```text
R(x,y)=(x hat-triangleright y, x),
```

then YBE gives self-distributivity and bijectivity gives bijective left
translations.  The finite transport state is a rack, so its inner group is a
fixed Artin-longitude detector.

2. **Two-sided unit but not strand-continuing.**  This is locally
nondegenerate by the lemma above, hence routed to the known
nondegenerate/guitar branch rather than remaining in the bottleneck.

3. **One-sided or mixed-unit.**  This is the only remaining case.  Some
coordinate section required by the universal continuation corridor is nonunit,
but nonunit sections cannot themselves be the final moving residual
permutation by the rank/unit-factorization gate.

Thus a genuine residual movement in the last case must have a subtler form:
local information is lost in one coordinate section and recovered by another
coordinate before the endpoint readout.  This is the **mixed-unit
context-recovery corridor**.

## Updated final theorem target

The positive route is reduced to the following statement.

```text
No mixed-unit universal-continuation theorem.
```

In a local-minimal interval reaching the
`bi_free_universal_corridor_bottleneck`, after the fixed Green,
Schutzenberger, atom, known-branch, quotient, and endpoint/unit readouts have
been applied, exactly one of the following must happen:

1. the lower row is strand-continuing, hence transport-rackified;
2. the lower row is two-sided unit, hence locally nondegenerate and closed;
3. the interval is not a legitimate local-minimal bottleneck.

If this theorem is proved, the local detector implication follows:

```text
Lambda_{H(pi,Q),n}(beta)=Lambda_{H(pi,Q),n}(1)
  => Delta_n(beta)=1.
```

Then the sharp obstruction theorem supplies `Q x A_H`, and
congruence-chain induction gives a finite rack independent of braid index.

## Exact remaining B seed

A counterexample can no longer use:

- a non-strand-continuing row by itself;
- a nonunit or reset continuation label;
- a two-sided unit lower row;
- a raw Green or Schutzenberger defect;
- a bounded detector miss.

It must exhibit a mixed-unit context-recovery corridor and upgrade it to braid
words

```text
beta_j in B_{q_j},  q_j -> infinity,
```

with eventual invisibility to every finite group detector while still moving
an explicit residual tuple.  Without this normalized-law upgrade, the data is
only a finite local obstruction seed, not outcome B.

## Executable audit

The local helper

```text
section_unit_row_audits(interval)
```

records, for every coloured row, which left and right coordinate sections are
bijective and which are nonunit.

The summary helper

```text
two_sided_unit_collapse_audit(interval)
```

records:

- whether the coloured YBE holds;
- the continuation-congruence audit;
- whether all rows are two-sided unit;
- whether the row is already the strand-continuing transport-rack case;
- whether the two-sided unit nondegenerate branch closes the row;
- which rows are non-two-sided and which of those have both unit and nonunit
  sections, hence are mixed-unit context-recovery candidates.

These executable checks do not replace the all-`n` theorem.  They make the
last obstruction precise: prove that mixed-unit context recovery cannot occur
in a local-minimal bottleneck, or turn one such corridor into the required
normalized-law B sequence.
