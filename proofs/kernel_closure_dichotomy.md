# Coordinate-kernel closure dichotomy

Date: 2026-05-28

This note records a symbolic refinement of the bi-free branch.  It is not the
Master Local-Minimal Residual Theorem, but it turns the rank diagnostic into
an actual admissible-family dichotomy.

## Coordinate kernels

For a local interval with

```text
T_{a,b}(x,y) = (u,v),       R_Z(a,b)=(c,d),
```

define the nondegeneracy coordinate kernels to be all pairs in the same
kernel of one of the maps

```text
y in A_b -> pr_1 T_{a,b}(x,y) in A_c       for fixed a,b,x,
x in A_a -> pr_2 T_{a,b}(x,y) in A_d       for fixed a,b,y.
```

Let `theta^ker` be the least admissible congruence family containing these
kernel pairs.  The implementation constructs it by starting from equality
plus the seed kernel pairs, then repeatedly closing under all local bijections
`T_{a,b}` and under their inverses.  Finiteness makes the process stabilize.
At the stable point, forward closure gives

```text
T_{a,b}(theta_a x theta_b) subset theta_c x theta_d,
```

and inverse closure gives the reverse inclusion.  Hence `theta^ker` is an
admissible local congruence family.

## Dichotomy

If the interval is local-minimal, then `theta^ker` is either equality on every
fibre or universal on every fibre.

The equality case is exactly the local nondegenerate branch.  Indeed, equality
means there are no nontrivial coordinate-kernel seed pairs, so each map

```text
y -> pr_1 T_{a,b}(x,y)
x -> pr_2 T_{a,b}(x,y)
```

is injective.  Since `T_{a,b}` is a bijection

```text
|A_a| |A_b| = |A_c| |A_d|.
```

Injectivity gives `|A_b| <= |A_c|` and `|A_a| <= |A_d|`; multiplying and using
the product equality forces both inequalities to be equalities.  Therefore
the coordinate maps are bijections, which is precisely the local
nondegenerate case.

If there is any nontrivial coordinate-kernel seed pair, then `theta^ker` is
not equality.  Local-minimality therefore forces `theta^ker` to be universal.
This is the universal coordinate-kernel-closure branch.

## Consequence

After the two-sided retraction/coretraction dichotomies, the bi-free branch
has a sharper symbolic fork:

- `theta^ker = equality`: the interval is locally nondegenerate and belongs to
  the already bookkept nondegenerate/guitar finite-G-measurable branch.
- `theta^ker = universal`: all fibre points are connected by coordinate-kernel
  degeneracies and their YBE transports.  This branch remains to be controlled
  symbolically, either by proving that the symmetric Green kernel-block and
  Schutzenberger detector sees every residual braid action, or by realizing a
  normalized-law counterexample.

The generated audit `proofs/bifree_rank_audit.md` checks this fork in the
exhaustive size-2 and size-3 local-minimal cover corpus.  Those rows are
candidate-search evidence only; the dichotomy above is the theorem-level
content supplied by this note.

## Corridor certificate

The implementation also records a finite corridor graph for the generated
closure.  Its vertices are fibre points, and an edge is added whenever a
nontrivial coordinate-kernel seed pair is present or whenever such an edge is
transported by a local table or inverse local table during closure.  If
`theta^ker` is universal, this graph is connected on every fibre.  Hence every
pair of fibre points is connected by a finite chain of elementary
coordinate-kernel degeneracies and YBE transports.

This corridor graph does not prove residual detection.  Its purpose is to
make the remaining universal branch precise: an all-`n` proof must show that
finite-G longitude data, presumably via the symmetric Green kernel-block and
Schutzenberger detectors, kills braid motion along every such corridor; a B
construction must build nontrivial residual holonomy that survives all of
these finite corridor constraints.

In the exhaustive size-3 bi-free corpus, the only universal
coordinate-kernel-closure rows are already involutive.  Their corridor closure
has depth `0`, generated edge counts `[0,1]`, and diameters `[0,1]` over the
two quotient colours.  This is not theorem evidence, but it is a useful
stress signal: the first remaining branch to prove symbolically is the
depth-zero universal corridor case, while deeper transported
kernel-corridor phenomena need separate stress tests.

The broader generated audit `proofs/kernel_corridor_audit.md` repeats this
measurement over every size-2 and size-3 local-minimal congruence-cover
interval.  In that finite corpus there are no semisplit leaks and every
output-kernel universal closure again has depth `0`.  This strengthens the
diagnostic target but does not change the theorem burden: the universal
coordinate-kernel branch still needs an all-`n` finite-G detector proof or an
explicit normalized-law escape.

The affine `F_2^2` audit shows that transported universal corridors can occur:
among the `84` local-minimal translated affine four-point intervals, `12`
have universal output-kernel closure of stable depth `1`.  All `12` are
involutive, hence already in a known finite-G-measurable branch.  Thus a B
candidate cannot merely exhibit transported corridor depth; it must exhibit
transported residual holonomy outside the known involutive, nondegenerate,
rack-type, affine, product, and coboundary measurable branches.

## Elementary kernel-pair closures

The corridor certificate can now be made one step sharper.  Instead of closing
all coordinate-kernel seed pairs at once, the helper

```text
coordinate_kernel_pair_closure_audits(interval)
```

closes each distinct elementary coordinate-kernel pair separately under every
local table and inverse local table.  The companion

```text
coordinate_kernel_pair_closure_failures(interval)
```

returns the elementary kernel pairs whose least admissible closure is not
universal.

In a local-minimal interval, every elementary coordinate-kernel pair has only
two possibilities.  If no such pair exists, the interval is locally
nondegenerate.  If such a pair exists, its least admissible closure is not
equality, so local-minimality forces that single pair to generate the
all-universal family.  Thus the universal corridor branch is not merely an
aggregate phenomenon: every individual coordinate-kernel degeneracy must
already open a universal admissible corridor.

This gives a useful B-side audit.  A proposed universal-corridor
counterexample must exhibit residual holonomy along elementary kernel-pair
corridors whose pair closures are universal.  If an elementary coordinate
kernel closes to a proper family, the interval was not local-minimal and the
congruence chain must be refined before applying the master theorem.
