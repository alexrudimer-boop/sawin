# Local master bottleneck ledger

Date: 2026-05-28

This note records the current exact routing of a finite local interval through
the reduction program.  It is a proof-audit ledger, not a proof of the Master
Local-Minimal Residual Theorem and not finite-search evidence for the global
problem.

## Executable summary

The helper

```text
local_master_bottleneck_summary(interval)
```

returns a `LocalMasterBottleneckSummary` with the following fields:

- whether the coloured Yang-Baxter equation holds;
- the number of admissible semisplit equality/universal families;
- the exact pair-closure local-minimality result, including the number of
  tested fibre pairs, the number of pair-closure failures, and the maximum
  closure depth;
- the two-sided retraction and coretraction kinds;
- whether the interval has a swapped or direct product-permutation witness;
- the product holonomy detail, when a product witness exists;
- the coordinate-kernel closure kind and stable depth;
- the elementary output coordinate-kernel pair-closure count, failure count,
  and maximum stable depth;
- the all-coordinate-kernel closure kind and stable depth;
- known whole-solution branch tags for the total interval table;
- for actual corridor-target rows, the orders of the current two-sided Green
  detector group factors;
- a verdict and the remaining proof obligation.

The verifier deliberately keeps semisplit congruences in front of the master
theorem.  If a semisplit family survives, the interval is not local-minimal
and must be refined before any local detector can be invoked.
The pair-closure counters give a concrete certificate behind the Boolean:
`local_minimal_pair_failure_count=0` means every distinct fibre pair generates
the universal admissible family, while a positive count points to explicit
generated proper congruence families.
The output-kernel pair counters are the elementary corridor counterpart:
`output_kernel_pair_failure_count=0` means every individual nontrivial
coordinate-kernel seed pair already generates the universal admissible
family.  This is stronger than merely saying the aggregate kernel closure is
universal, and it is the certificate required by
`proofs/universal_corridor_target.md`.

## Verdicts

The ledger routes local data as follows.

`invalid_colored_ybe`.
The local table is not a valid coloured YBE interval.

`semisplit_leak`.
An equality/universal mixed congruence family survives.  This fails the
required local-minimality audit before any hidden-holonomy argument begins.

`not_local_minimal`.
No semisplit leak is seen, but another proper admissible congruence family
exists.  The congruence chain must be refined.

`local_minimality_unchecked`.
This verdict is retained as a defensive state for externally supplied
local-minimality evidence, but the default finite-table router no longer
reaches it merely because fibres are large.  Local-minimality is now checked
by the exact single-pair closure criterion in
`proofs/local_minimality_gate.md`, not by Bell-number partition enumeration.

`product_finite_g_branch`.
The interval has a swapped or direct product-permutation witness and at least
one product normal form falls in a closed finite-G product subbranch.  The
closed cases currently recognized are: product-label coboundaries, handled by
the all-`n` coboundary telescope; one-colour swapped product holonomy, handled
by the cyclic pairwise-linking detector; identity-base swapped cyclic
holonomy, handled by the identity-base product lemma; fibre-size-two product
holonomy, handled by the affine `F_2` product reduction; and genuinely
coloured product holonomy whose total interval solution is already in a known
whole-solution finite-G branch.

`product_genuinely_coloured_bottleneck`.
The interval has a product-permutation witness, but every available product
normal form has genuinely coloured non-coboundary holonomy outside the current
known total branch tags.  This is the remaining product-label theorem target:
prove that its closed product labels are finite products of recursive
Artin-longitude evaluations in the fixed totalized product label group, or
realize the product-specific normalized-law obstruction.

`product_witness_missing`.
The two-sided retraction or coretraction audit reports a universal profile,
but the corresponding product witness was not recovered.  This flags an
internal audit failure in the symbolic dichotomy, because the universal
profile proof should produce the product normal form.

`locally_nondegenerate_branch`.
The coordinate-kernel closure is equality.  The kernel-closure dichotomy
then proves that the local coordinate maps are bijective, so the interval is
in the already bookkept nondegenerate/guitar finite-G-measurable branch.

`known_total_branch`.
After semisplit exclusion, full local-minimality, closed-product routing, and
the locally nondegenerate check, the total interval solution is already in a
known whole-solution finite-G branch such as involutive, permutation-form, or
rack-type.  In this case the local Green/corridor theorem is unnecessary:
the known branch detector can be multiplied with the upper quotient detector,
and the interval cannot be counted as a remaining corridor bottleneck.
Audit-only tags do not suffice for this verdict.  In particular,
`affine_cyclic` remains excluded from the known-total detector set unless the
same interval is also covered by one of the symbolic all-`n` detector branches
or by a closed product subbranch.

`bi_free_universal_corridor_bottleneck`.
This is the genuine remaining master branch.  The interval has passed the
semisplit audit, is not routed to a product witness, is not locally
nondegenerate, has no known whole-solution branch tag, and has universal
coordinate-kernel closure.  The audit also records the elementary
coordinate-kernel pair closures; in a legitimate local-minimal corridor row,
each nontrivial seed pair must separately have universal closure.  A proof of
A must show that input-dependent
Artin-longitude evaluations in fixed finite Green/corridor detector groups
kill all residual braid motion here.  A proof of B must construct an explicit
interval or full solution in this verdict and a normalized-law sequence whose
residual holonomy survives every finite group detector.

`proper_mixed_kernel_closure`.
If the interval is truly local-minimal, this should not occur: the generated
coordinate-kernel closure is an admissible family and must be equality or
universal.  This verdict means the local-minimality evidence is incomplete or
the interval is not a maximal-chain interval.

## Why this helps

The ledger consolidates three symbolic reductions that were previously spread
across the notes:

1. Local-minimality is certified exactly by single-pair admissible closures:
   every distinct fibre pair must generate the all-universal family.
   Semisplit families are ordinary admissible congruence families and remain
   a separately visible first failure mode.
2. Universal two-sided retraction or coretraction gives a product-permutation
   normal form, not a hidden Green/corridor branch.  Product normal forms are
   immediately split into closed coboundary/pairwise/known-total subbranches
   versus genuinely coloured product holonomy.
3. Equality coordinate-kernel closure is exactly local nondegeneracy; the
   only rank-collapsed local-minimal remainder is universal coordinate-kernel
   closure outside known whole-solution finite-G branches.  The elementary
   coordinate-kernel pair counters prevent an aggregate-only shortcut: every
   individual kernel degeneracy must already open the same universal
   corridor.

Thus a future candidate counterexample cannot be advertised merely as
degenerate, product-like, semisplit-free, or high-corridor-depth.  It must
land either in the genuinely coloured product bottleneck or in the bi-free
universal-corridor verdict, and then defeat the corresponding fixed detector
groups by a normalized-law sequence.

Conversely, a future proof of A can now cite a single remaining theorem after
the known branches:

> Bi-free universal-corridor factorization lemma.  For every local-minimal
> interval with verdict `bi_free_universal_corridor_bottleneck`, the residual
> braid action factors, for all braid indices, through input-dependent
> evaluations of recursive Artin longitudes in the fixed finite product of
> two-sided symmetric kernel-block groups, Schutzenberger groups, and known
> branch factors attached to the interval and quotient detector.

The Green holonomy gate sharpens the last phrase: it is not enough to count
raw atom-trivial completed-context loops.  Only the total bijective
atom-trivial loops form possible finite-stage residual motion, and these are
now extracted as finite permutation groups by
`bounded_atom_trivial_loop_group_summaries()`.  Reset-like atom-trivial loops
remain useful warning signs, but they are not B certificates.

This is still the unproved step.  The ledger makes it explicit enough that a
purported final proof or counterexample can be audited against one line:
does it prove this lemma, or does it construct a normalized-law escape from
this exact verdict?

## Guardrail tests

`tests/test_local_bottleneck.py` checks three basic routing cases:

- a two-colour identity interval is rejected as a semisplit leak;
- a one-colour flip interval is routed to the closed product finite-G branch;
- a six-point one-colour flip interval is rejected as `not_local_minimal` by
  `15` failed pair closures, even though its product witness is visible;
- the three-point dihedral rack interval is routed to the locally
  nondegenerate branch, not to the corridor bottleneck.
- the exhaustive size-three congruence-cover corpus has no remaining
  `product_genuinely_coloured_bottleneck` or
  `bi_free_universal_corridor_bottleneck` rows after product rows split into
  coboundary, one-colour pairwise, and known-total subbranches.
- `affine_cyclic` alone is not a known-total detector tag; if it appears
  without an actual all-`n` detector branch, the interval remains in the open
  product/corridor target.

These tests are guardrails for the reduction ledger only.  They do not prove
the global theorem and they do not certify the master local theorem.
