# Bi-free universal-corridor factorization target

Date: 2026-05-28

This note pins down the last named branch in the local-minimal reduction.  It
is not a proof of the Master Local-Minimal Residual Theorem.  Its purpose is
to make the remaining A-route lemma and the corresponding B-route certificate
use the same hypotheses.

## Interval Hypotheses

Let `pi : X -> Z` be a finite local-minimal interval over a quotient solution
`Z` dominated by a finite rack `Q`.  Let `N_n = ker rho_{Q,n}`.  For
`z in Z^n`, write `X_z = product_i pi^{-1}(z_i)` and
`delta_{n,z}:N_n -> Sym(X_z)` for the residual action.

The interval is in the bi-free universal-corridor target only if all of the
following hold.

- The coloured local table satisfies the Yang-Baxter equation.
- No semisplit equality/universal congruence family is admissible.
- No other proper admissible congruence family is present; equivalently, the
  interval is genuinely local-minimal.  The archive now checks this by the
  exact single-pair closure criterion: every distinct fibre pair must generate
  the all-universal admissible family.
- The two-sided retraction and coretraction families are both equality.  If
  either is universal, the interval must first be routed to the product
  normal form.
- There is no swapped or direct product-permutation witness.
- The output coordinate-kernel closure is universal.  If it is equality, the
  interval is locally nondegenerate and belongs to the known guitar/rack
  measurable branch.
- The interval is not already in a known finite-G-measurable branch:
  involutive/permutation, affine, pairwise-linking, finite semidirect affine,
  coboundary, product-label, rack-type, or nondegenerate.

These are exactly the semantic contents of the current
`bi_free_universal_corridor_bottleneck` verdict, not an additional search
condition.

## Fixed Detector Candidate

For such an interval, form the full finite solution attached to the local
table and take the following finite group factors.

- The full symmetric groups on every left Green kernel-block quotient.
- The full symmetric groups on every right Green kernel-block quotient,
  computed from the opposite solution.
- The left and right Schutzenberger action groups of regular Green classes.
- The left and right atom-quotient inner groups for every Green audit whose
  saturated atom layer is proved to be a total right-rack-like YBE layer.
- Any already proved finite detector factors for branch components that the
  interval still carries after quotienting, including quotient detector data
  from `Q`.

Let `H(pi,Q)` be the direct product of these finite groups, with duplicate
concrete tables removed only when they are literally the same table.  This
group is finite and depends only on the interval and the quotient detector,
not on `n`.

The sharp rack detector that would close this interval is

```text
Q x A_{H(pi,Q)}.
```

## A-Route Statement

The exact theorem needed in this branch is:

> For every `n`, every `beta in N_n`, and every `z in Z^n`,
>
> ```text
> Lambda_{H(pi,Q),n}(beta)=Lambda_{H(pi,Q),n}(1)
>     => delta_{n,z}(beta)=1.
> ```

Equivalently, for every input tuple `x in X_z` and every output coordinate
`j`, the residual coordinate motion must be expressible by a finite
expression in evaluations of recursive Artin longitudes in `H(pi,Q)`.  The
homomorphisms `F_n -> H(pi,Q)` used in those evaluations may depend on
`(n,z,x,j,beta)` and on finite corridor/Green states canonically attached to
these data.  They may not depend on an unbounded group, on a braid-index
specific detector, or on finite search over `B_n`.

This is the all-`n` bridge missing from the current archive.  The finite
semigroup holonomy lemma reduces purely aperiodic residue after these group
coordinates are killed, but it does not by itself prove that all residual
branch choices factor through the group coordinates above.

## B-Route Certificate

A counterexample to the master theorem can be certified through this branch
only by giving all of the following data.

1. An explicit finite local table in the hypotheses above, or a full finite
   YBE solution whose maximal congruence-chain interval has this table.
2. A symbolic proof of the coloured YBE, bijectivity, and local-minimality,
   including exclusion of semisplit families.
3. A normalized-law sequence `beta_j in B_{q_j}`, with `q_j -> infinity`,
   such that for every finite group `G`,
   `Lambda_{G,q_j}(beta_j)=Lambda_{G,q_j}(1)` eventually.
4. Base-kernel membership `beta_j in N_{q_j}` for the quotient detector `Q`.
5. Explicit base tuples `z_j` and fibre tuples `x_j in X_{z_j}` with
   `delta_{q_j,z_j}(beta_j)(x_j) != x_j`.
6. A proof that the moved residual holonomy is not in the subgroup generated
   by all recursive-longitude values in any fixed finite detector group.

Items 3 and 6 are the normalized-law obstruction.  A bounded detector miss, a
timeout, or a fixed-degree collision is not enough.

## False Shortcuts Excluded

Three tempting shortcuts do not close this target.

- A direct rack cover of `X` exists only in the rack-type case.
- A literal coordinate formula
  `rho_X(beta)(x)_j = phi_x(L_j(beta))(x_{p(j)})` would force the second
  coordinate of one positive crossing to be the incoming first coordinate, so
  it is again rack-type.
- Ordinary group Hurwitz conjugation gives the nondegenerate/guitar branch,
  not the arbitrary degenerate local interval.

Thus the missing proof must be a global finite-longitude factorization
through the fixed group `H(pi,Q)`, or the missing counterexample must escape
that exact factorization by normalized laws.

## Executable Certificate Layer

The companion note
`proofs/bifree_corridor_subgroup_certificate.md` records the finite diagnostic
helpers attached to this target:

```text
bifree_corridor_detector_target(interval)
bifree_corridor_detector_groups(interval)
bifree_corridor_word_certificate(interval,n,beta)
bifree_corridor_exact_image_audit(interval,n)
bifree_corridor_product_subgroup_audit(interval,n,beta)
exact_detector_readout_audit(qmap,Q,groups,n)
exact_detector_product_readout_audit(qmap,Q,groups,n)
```

These helpers build the listed finite detector factors, profile
`V_beta(H_i)` for each factor, and attach moved residual tuples to finite
words.  The exact-image helper closes the finite joint image for one braid
index using the same factor list.  These helpers are useful for auditing
proposed proof steps or counterexample stages, but they do not replace the
all-`n` theorem or the normalized-law diagonalization required for outcome B.

The readout audit is the fixed-index form of the A-route target: when it is
nontruncated and well-defined, it displays a finite table from reachable
base-kernel detector states to residual permutations, with an explicit check
that each row preserves quotient fibres and hence restricts to the maps
`delta_{n,z}`.  The missing theorem is the symbolic construction of these
readouts uniformly in `n`, not the existence of more fixed-index tables.
When the proposed factor product is small enough, the product-readout audit
also checks that the displayed two-sided Green factor list is behaving as one
single finite detector group, as required by the sharp obstruction theorem.

The product-subgroup helper checks, when the product is small enough to
enumerate, that the listed detector factors are equivalent to one direct
product detector at the longitude-subgroup level.  The symbolic justification
is `proofs/longitude_subgroup_products.md`; hence a factorwise corridor proof
still yields one finite `H(pi,Q)`, independent of `n`.
The listed-factor helper now includes atom-quotient inner groups as
executable detector data, not merely as prose in the atom-rack lift
criterion.  This synchronizes the candidate `H(pi,Q)` with
`proofs/green_atom_rack_lift_criterion.md`: the atom rack layer is killed by
its finite inner group, while lower endpoint holonomy is killed by the fixed
unit, Schutzenberger, and kernel-block factors.

The additional gate `proofs/green_holonomy_factorization_gate.md` separates
raw bounded atom-trivial context collapse from group-like atom-trivial
holonomy.  In this target branch, a future B certificate must move through
the group-like part; a reset-like or non-bijective bounded corridor loop is
not enough, because residual braid actions are permutations.  Conversely, a
future A proof may close the branch by proving that these group-like loops
factor, uniformly in `n`, through input-dependent recursive Artin-longitude
evaluations in the fixed group `H(pi,Q)`.

The criterion `proofs/unit_section_detection_criterion.md` is the reusable
form of this last sentence for semigroup observers.  Once a residual
coordinate branch is written as a word in one fixed finite transformation
monoid, the proof need only show that its unit section labels lie in
`V_beta(U(M))`; the unit-factorization lemma then removes all nonunit
ambiguity, and the finite unit group becomes a valid sharp-obstruction
detector factor.  The remaining open work is to prove that such section words
exist uniformly in `n` for every interval in this bi-free corridor verdict,
or to construct a normalized-law escape in the corresponding unit groups.
If several fixed monoids are needed, `proofs/unit_section_product_detector.md`
multiplies their unit groups into one detector group.  Thus the final
candidate `H(pi,Q)` may be displayed as factors, but it is mathematically a
single finite product group independent of the braid index.
The endpoint criterion `proofs/unit_composite_longitude_criterion.md` gives
the preferred target when corridor transports telescope: prove that the final
residual unit/composite lies in `V_beta(U(M))`, not necessarily that every
intermediate section label does.
The note `proofs/endpoint_unit_dichotomy.md` packages the corresponding
counterexample warning: an endpoint unit outside the relevant subgroup is
only a finite detector failure until it is upgraded to a normalized-law
sequence defeating every finite group.
The executable endpoint-product audit
`unit_composite_product_detection_audit(...)` is the matching finite
guardrail for a list of such monoids; it records the endpoint tuple in the
direct product and checks membership in the product longitude subgroup when
the product is small enough to enumerate.
The expression certificate in
`proofs/endpoint_longitude_expression_certificate.md` gives the symbolic
version of this endpoint target: instead of enumerating `V_beta(U(M))`, a
future proof may display the endpoint as a finite product of evaluated
recursive longitudes under an input-dependent assignment to the fixed unit
group.  This is the preferred all-`n` certificate format for corridor
endpoints because it keeps the detector group fixed while allowing the
assignment and expression to depend on the residual tuple being evaluated.
