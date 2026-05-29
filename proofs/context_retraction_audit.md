# Context retraction audit

## Purpose

This note records an exact finite audit of the two-sided context retraction
relation attached to a local interval, together with its dual two-sided
coretraction relation.  It is not a proof of Sawin finite-rack domination by
itself; it isolates the primitive/local-minimal dichotomy that a proof of the
master local theorem must exploit.

For a local interval with coloured maps

```text
T_{a,b}(x,y) = (lambda_x(y), rho_y(x)),
```

the retraction profile of a fibre point `x in A_a` consists of:

- all first-output maps `y -> pr_1 T_{a,b}(x,y)`;
- all second-output maps `y -> pr_2 T_{b,a}(y,x)`.

The forward initial relation identifies two points when these indexed maps
agree exactly.  For nondegenerate global solutions this is the usual
retraction relation `x ~ x'` iff `lambda_x=lambda_x'` and
`rho_x=rho_x'`.  For arbitrary bijective local tables the implementation uses
the meet of this forward relation with the analogous relation for the inverse
local table, then applies closure steps in both orientations.  The forward
closure keeps a related pair `x ~ x'` only when every
opposite unary context also sends them to related outputs:

```text
pr_1 T_{b,a}(y,x) ~ pr_1 T_{b,a}(y,x'),
pr_2 T_{a,b}(x,y) ~ pr_2 T_{a,b}(x',y).
```

The inverse table imposes the same condition on inverse contexts.  Iterating
this finite refinement gives the largest two-sided stable family below
two-sided context-profile equality.  The triangle argument for the forward
table gives transport into the target relation; the same argument for the
inverse table gives the reverse inclusion.  Thus the stable family is an exact
admissible local congruence without assuming one-sided nondegeneracy.

The dual coretraction profile views the point as an input coordinate instead
of as a parameter.  It records:

- all first-output maps `y -> pr_1 T_{b,a}(y,x)`, where `x` is the right input;
- all second-output maps `y -> pr_2 T_{a,b}(x,y)`, where `x` is the left input.

The same two-sided inverse-closure argument makes its stable family an exact
admissible local congruence.  If this dual relation is universal, then
`T_{a,b}(x,y)=(L_{a,b}(x),R_{a,b}(y))`, the direct product-permutation branch.

## Exact tiny-corpus results

The script `tools/run_context_retraction_audit.py` exhaustively scans the
size-2 and size-3 bijective YBE tables, extracts congruence-cover intervals,
keeps the local-minimal intervals, and computes the stable two-sided
context-retraction family.

The current exhaustive results are:

```text
size 2 local-minimal covers: 5
  initial two-sided family admissible: 5
  equality stable family: 1
  universal stable family: 4
  coretraction equality stable family: 4
  coretraction universal stable family: 1
  combined split: equality/universal 1, universal/equality 4
  universal product-permutation witnesses: 4
  universal direct-product witnesses: 1
  non-admissible stable families: 0
  mixed stable families: 0

size 3 local-minimal covers: 134
  initial two-sided family admissible: 134
  equality stable family: 24
  universal stable family: 110
  coretraction equality stable family: 128
  coretraction universal stable family: 6
  combined split: equality/equality 18, equality/universal 6, universal/equality 110
  universal product-permutation witnesses: 110
  universal direct-product witnesses: 6
  non-admissible stable families: 0
  mixed stable families: 0
```

This matches the expected primitive split:

- equality means the interval is two-sided-retraction-free.  In the tiny
  local-minimal corpus, every equality case lies in the already measurable
  involutive, rack-type, or nondegenerate branch: for size `3`, the `24`
  equality cases split as `6` involutive, `6` involutive identity-table, `11`
  nondegenerate, and `1` rack-type nondegenerate;
- universal means all points in every fibre have the same degenerate-retract
  profile.  In that case the table splits as
  `T_{a,b}(x,y)=(L_{a,b}(y),R_{a,b}(x))`, where `L_{a,b}` and `R_{a,b}` are
  fibre bijections, so the interval is in the coloured product-permutation
  branch;
- universal coretraction gives the direct product-permutation branch
  `T_{a,b}(x,y)=(L_{a,b}(x),R_{a,b}(y))`.  The six size-3 equality/universal
  intervals are all involutive identity-table cases.  The remaining
  equality/equality, or bi-free, size-3 intervals are all already measurable:
  `6` involutive, `11` nondegenerate, and `1` rack-type nondegenerate.

The follow-up rank/kernel audit `proofs/bifree_rank_audit.md` records
coordinate-map ranks, kernel-partition shapes, and the number of distinct
kernels for these bi-free rows.  In the size-3 local-minimal cover corpus it
finds no untagged intermediate-rank or intermediate-kernel bi-free profile:
the bi-free rows are either involutive with collapsed kernel shapes
`[1]`, `[2]`, and `[1,1]`, or nondegenerate/rack-type with singleton kernels
`[1,1,1]` in the left and right output directions.  This is still finite
candidate search, but it sharpens the symbolic target to a rank/Green
dichotomy rather than a broad bi-free search.

The theorem-level part of this sharpening is recorded separately in
`proofs/kernel_closure_dichotomy.md`.  The least admissible family generated
by kernels of the nondegeneracy coordinate maps is equality exactly in the
local nondegenerate branch; otherwise local-minimality forces it to be
universal.  Thus the bi-free residual gap has been narrowed to the universal
coordinate-kernel-closure branch.

## Proof obligation exposed

The A-route master lemma can now be stated more sharply.

For every finite local bijection, both the stable two-sided context relation
and its dual coretraction relation are admissible congruence families.  Hence,
for a local-minimal interval, each is either equality or universal.  The two
universal cases are product-permutation branches, one swapped and one direct.
The needed symbolic step is now sharper: reduce finite local-minimal intervals
that are both two-sided-retraction-free and two-sided-coretraction-free to
already measurable branches (nondegenerate/guitar, involutive/permutation,
affine/coboundary, or finite semidirect affine) or to the symmetric
kernel-block detector.  After the coordinate-kernel closure dichotomy, the
new primitive subcase is universal coordinate-kernel closure inside the
bi-free branch.

The remaining non-search step is to prove the braid-action implication:

```text
Lambda_{G,n}(beta) = Lambda_{G,n}(1)
and beta in ker rho_{Q,n}
    => every finite context profile of every strand is fixed
    => Delta_n(beta) = 1.
```

The audit verifies the implementation and the tiny-corpus split.  The
admissibility of the stable two-sided relation is the symbolic argument in
`proofs/retraction_dichotomy.md`, and the dual argument is recorded in
`proofs/coretraction_dichotomy.md`; the remaining all-`n` braid-action
implication must still not be replaced by finite-search evidence.
