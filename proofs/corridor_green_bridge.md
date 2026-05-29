# Corridor-Green bridge target

Date: 2026-05-28

This note cross-references two diagnostics that were previously separate:

- the universal coordinate-kernel corridor branch, and
- the finite Green kernel-block / Schutzenberger branch-choice detector.

It is not a proof of the Master Local-Minimal Residual Theorem.

## Diagnostic Overlap

The local-minimal Green audit now records the output coordinate-kernel closure
for each local-minimal congruence-cover interval and cross-tabs it with
bounded completed-context Green loops.

In the exhaustive size-2 cover corpus:

```text
local-minimal covers: 5
output-kernel closures: equality 4, universal 1
universal-output hidden atom-trivial loops: 1
universal-output hidden bijective loops: 0
universal-output mixed atom projections: 0
universal-output untagged intervals: 0
universal-output tags: involutive + identity_table
```

In the exhaustive size-3 cover corpus:

```text
local-minimal covers: 134
output-kernel closures: equality 122, universal 12
universal-output hidden atom-trivial loops: 12
universal-output hidden bijective loops: 3
universal-output mixed atom projections: 6
universal-output untagged intervals: 0
universal-output tags: involutive 12, identity_table 6
```

Thus the smallest universal output-kernel corridor rows are exactly where the
bounded Green observer sees hidden completed-context loops, but every such
overlap in the audited local-minimal cover corpus is already in the
involutive/identity branch.

The affine `F_2^2` audit adds a complementary warning: positive corridor
transport depth can occur, but the first such local-minimal examples are also
involutive.  Therefore the proof cannot rely on "no transported corridors";
it must explain why transported corridor holonomy is finite-G measurable.

## Symbolic Bridge Needed

The desired theorem-level bridge is:

> If a local-minimal interval has universal output coordinate-kernel closure,
> then corridor transports either force a known finite-G-measurable branch
> (involutive/permutation, affine, product/coboundary, rack-type, or
> nondegenerate after quotient refinement), or all residual branch choices
> along the corridor are detected by the finite two-sided symmetric
> kernel-block and Schutzenberger detector.

This bridge would close the current A-route when combined with the sharp
finite-G obstruction theorem.  Its detector group is finite because it is
constructed from the finite local interval: take the relevant symmetric
groups on Green kernel-block quotients and the finite Schutzenberger
permutation groups, with duplicate factors removed.  What remains unproved is
the all-`n` braid-action implication from equality of finite-G longitudes to
trivial residual action.

Equivalently, using `proofs/label_longitude_factorization.md`, one must prove
that every corridor transport and completed-context Green branch choice is an
evaluation, or a finite product of evaluations, of recursive Artin longitudes
inside that fixed finite detector group.  This phrasing separates the finite
group construction from the all-`n` braid-action factorization.

The new `proofs/green_holonomy_factorization_gate.md` inserts one finite-depth
filter before this bridge is invoked.  A raw hidden atom-trivial completed
context loop matters only if it is a total bijection of the finite context
word set, hence an element of the bounded atom-trivial loop group.  Non-bijective
atom-trivial loops are reset-like observer collapse, not residual
permutation motion.  Therefore the bridge needs to factor the group-like
loop part through the fixed detector groups; it need not treat every raw
context collapse as a possible counterexample.

## Counterexample Shape

A B candidate should now be sought at the intersection of the two diagnostics.
It must have:

- universal output coordinate-kernel closure;
- hidden Green completed-context holonomy not falling into the known branches;
- no semisplit admissible congruence family;
- a normalized-law sequence invisible to every finite group detector but
  moving an explicit residual tuple.

The current audits show no such example in the size-2/3 local-minimal cover
corpus, no such example in arbitrary two-colour/fibre-2 local tables over all
two-point bases, and no such example in translated affine `F_2^2`.
