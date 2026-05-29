# Bi-free corridor certificate audit

Date: 2026-05-28

This generated audit applies the bi-free corridor subgroup certificate
to the exhaustive size-2 and size-3 local-minimal congruence-cover
corpus.  It is finite diagnostic evidence only.  It does not prove the
Master Local-Minimal Residual Theorem and cannot serve as outcome B.

For every interval routed to the
`bi_free_universal_corridor_bottleneck` verdict, it checks all braid
words in the bounded ball below.  A listed-factor failure would be a
quotient-fixed residual mover whose recursive-longitude subgroup
profile is trivial for every listed two-sided Green detector factor.

## size_2_exhaustive

Local-minimal covers: `5`.
Verdict counts: `product_finite_g_branch`: `5`.
Target-shaped intervals: `0`.
Target tags: `{}`.
Bounded braid words checked per target interval: `160` on `B_3` through length `4`.
Listed-factor B-shaped failures: `0`.

Target detector rows:

- none

## size_3_exhaustive

Local-minimal covers: `134`.
Verdict counts: `known_total_branch`: `6`, `locally_nondegenerate_branch`: `12`, `product_finite_g_branch`: `116`.
Target-shaped intervals: `0`.
Target tags: `{}`.
Bounded braid words checked per target interval: `160` on `B_3` through length `4`.
Listed-factor B-shaped failures: `0`.

Target detector rows:

- none

## Consequence

No listed-factor B-shaped failure appears in this bounded audit.  In
the tiny local-minimal cover corpus, no interval now reaches the
`bi_free_universal_corridor_bottleneck` verdict after closed
product subbranches and known whole-solution branches are routed
first.  The size-`3` product rows route to
`product_finite_g_branch`, and the six rows that previously had
the corridor target shape are involutive and now route to
`known_total_branch`.

This narrows the search surface but does not close the theorem.  A
proof still has to show the all-`n` subgroup-factorization lemma for
arbitrary finite fibres and quotient colours.  A counterexample must
give a normalized-law sequence defeating every finite group, not only
this fixed listed factor set at bounded word length.
