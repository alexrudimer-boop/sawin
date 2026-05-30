# Progress summary

Date: 2026-05-29

This file is the compact state of the Sawin finite-rack domination workspace.
It is a rigorous progress summary, not a final resolution.  As of this
snapshot, neither final outcome A nor final outcome B has been proved.

## Problem

For every finite bijective set-theoretic Yang-Baxter solution `X`, decide
whether there is a finite rack `Y`, independent of braid index `n`, such that

```text
ker rho_{Y,n} subset ker rho_{X,n}   for all n.
```

The permitted final answers are:

- A. a complete all-`n` proof of finite-rack domination; or
- B. an explicit finite bijective YBE counterexample together with a
  normalized-law obstruction sequence defeating every finite rack.

Finite search, bounded detector misses, and timeout evidence are guardrails
only.  They cannot close either outcome.

## Established reductions

The quotient/residual setup is fixed.  For a quotient `pi:X->Z`, if `Z` is
already dominated by a rack `Q`, set `N_n=ker rho_{Q,n}`.  For each
`z in Z^n`, the fibre product is `X_z=prod_i pi^{-1}(z_i)`, and the residual
action is

```text
delta_{n,z}: N_n -> Sym(X_z).
```

The bundled residual map is `Delta_n(beta)=(delta_{n,z}(beta))_z`.

The sharp obstruction theorem is now the central reduction.  For a finite
group `G`, the rack

```text
A_G = T_2 x (G x G),
(a,u) triangleright (b,v) = (aba^{-1}, av)
```

detects finite-`G` recursive Artin-longitude data
`Lambda_{G,n}(beta)`.  For an interval over `Q`, it is enough to find one
finite group `G=G(pi,Q)`, independent of `n`, such that for all `n` and
`beta in N_n`,

```text
Lambda_{G,n}(beta)=Lambda_{G,n}(1) => Delta_n(beta)=1.
```

Then `Q x A_G` dominates the interval.  The repository contains the executable
rack constructor `sharp_obstruction_rack(Q,G)`.

The congruence-chain induction is reduced to local-minimal intervals.  Given
a maximal congruence chain

```text
Delta_X=kappa_0 < ... < kappa_m=Nabla_X,
```

it is enough to prove the local theorem for every interval
`X/kappa_i -> X/kappa_{i+1}`.  If the local detector is `G_i`, the racks are
assembled by `Q_i=Q_{i+1} x A_{G_i}`.  The executable helper
`assemble_congruence_chain_rack(Q_m, groups)` now performs exactly this
iteration, where `groups` are the fixed finite local detector groups supplied
while descending the chain.  It records each factor size
`2*|G_i|^2`, the input and output rack sizes, and the final rack.  The helper
has no braid-index parameter; it preserves finiteness and independence from
`n` provided every `G_i` is fixed at the interval level.
The wrapper `closed_local_detector_chain(summaries)` now performs the audited
handoff from local bottleneck summaries to this construction: each closed
local row must supply one interval-level finite product group, and open
verdicts or delegated detector gaps are reported before any rack is assembled.
`assemble_closed_local_detector_chain_rack(Q_m,summaries)` then calls the
chain constructor only after this fixed-group check succeeds.

## Local-minimality and semisplit handling

The local table has colours `a,b`, fibres `A_a`, and bijections

```text
T_{a,b}: A_a x A_b -> A_{a dot b} x A_{a*b}
```

satisfying the coloured YBE.  Local-minimality means the only admissible
families of fibre congruences `theta_a` are all equality and all universal,
where

```text
T_{a,b}(theta_a x theta_b) =
theta_{a dot b} x theta_{a*b}.
```

The old full partition enumeration is no longer needed for this question.
The exact criterion is:

```text
the interval is local-minimal
iff every distinct pair p,q in every fibre A_a
generates the all-universal admissible congruence family.
```

The helper `LocalInterval.pair_generated_local_minimality_audits()` computes
the least admissible closure of each single pair by transporting product
relations through every local bijection and inverse.  This is an exact
finite certificate for the supplied interval and works for arbitrary finite
fibre sizes; it is not Bell-number partition enumeration.
The generated closure audit now records first-derivation rows for every
nontrivial relation edge, including the depth, seed/forward/inverse source,
crossing colour pair, and source product pairs.  Thus local-minimality rows
are no longer only Boolean or counter-based: a proof critic can inspect how
each universal fibre edge was forced, or where a proper mixed closure stops.

Semisplit families are fully visible.  For a subset of colours `S`, the
equality/universal family

```text
theta^S_a = universal on A_a if a in S,
theta^S_a = equality on A_a otherwise
```

is tested at the relation level, not by a colour-graph shortcut.
`LocalInterval.semisplit_audits()` records every admissible semisplit family
or a concrete failed transport witness.  The Boolean-CSP view
`semisplit_constraint_rows()` and `semisplit_boolean_assignments()` is an
independent tabular presentation of the same exact relation test, including
singleton-fibre canonicalization.

Thus any final proof or counterexample must pass this gate: a semisplit leak
is simply non-local-minimal and must be refined before invoking the master
local theorem.

## Known closed branches

The following branches have finite-`G` measurable routes recorded in the
proof notes and tests:

- rack-type, involutive, permutation-form, and nondegenerate/guitar branches;
- affine and fibre-size-two affine over `F_2` branches in the audited form;
- pairwise-linking and one-colour product holonomy branches;
- coboundary/product-label telescope branches;
- finite semidirect affine and finite product detector branches already
  reduced to fixed finite groups;
- direct `Sym(X)` detection for the known symbolic subbranches.

The known-branch routing now has an explicit detector certificate.  The helper
`known_branch_detector_certificate(X)` returns `G=1` for involutive tables,
`G=C_ord(sigma tau)` for permutation-form tables, and the direct
`Sym(X)` detector for rack-type or nondegenerate/guitar tables.  It records
the detector group order and the sharp rack factor size `2*|G|^2`, with an
explicit marker that no braid index is used.

The product-branch routing now has the analogous local certificate layer.
`ProductFiniteGDetectorCertificate` records the detector order and
`2*|G|^2` factor size for closed product coboundary, one-colour pairwise,
identity-base cyclic, and known-total product rows.  Where the proof supplies
the detector, the certificate now also carries the actual finite group object:
`C_1`, `C_m`, or the reused known-branch group.  Fibre-size-two affine product
rows remain honest delegated closures: the summary records a certificate gap
pointing to the affine `F_2` branch note rather than silently assigning a
local cyclic detector that has not been proved in this wrapper.

The notes also close several false shortcuts:

- a direct rack cover of `X` exists only in the rack-type case;
- nondegenerate covers cannot solve arbitrary degenerate intervals by
  quotienting;
- fixed finite braid-action image laws vanish on that fixed image and do not
  produce B;
- pure two-strand crossing-order mismatch cannot be outcome B, since for
  `r=ord(R_X)` the cyclic group `C_r` detects the `B_2` action.

## Longitude subgroup calculus

The longitude-value subgroup

```text
V_beta(G) <= G
```

is now functorial under fixed finite group homomorphisms and multiplicative
over fixed direct products:

```text
V_beta(prod_i G_i) = prod_i V_beta(G_i).
```

The code includes explicit witness operations:

- `pushforward_longitude_subgroup_witness(...)`;
- `direct_product_longitude_subgroup_witness(...)`;
- product endpoint witnesses in `prod_i U(M_i)`.

This matters because a proof may use finitely many branch detector groups,
but the sharp obstruction theorem requires one finite product group
independent of `n`.  The witness calculus prevents an informal factor list
from hiding an `n`-dependent detector.

## Semigroup, unit, and endpoint progress

The semigroup holonomy layer has been sharpened to a group problem.  If a
word in total transformations of a finite set has a final residual action
that is a permutation, every total-transformation factor in that word is a
unit/permutation.  Reset-like nonunit labels cannot be the final B
obstruction.

For one finite transformation monoid `M`, the preferred A-side endpoint
certificate is:

```text
final residual unit composite lies in V_beta(U(M)).
```

It is enough to display this endpoint as a finite product of evaluated
recursive longitudes under an input-dependent assignment into the fixed unit
group `U(M)`.  For several fixed monoids, the product endpoint audit packages
the certificates into one direct product group.  The current code records
literal product witnesses and checks that their values match the residual
endpoint.

This is an important reduction but not the missing theorem.  The missing
theorem must produce these endpoint expressions uniformly for all braid
indices in the remaining branch.
The newest refinement is the Artin-defect longitudinalization sieve:
instead of searching for arbitrary endpoint-longitude expressions, it is
enough to display each remaining group-like endpoint as a product of values
`phi(beta(w)p_beta(w)^-1)` in fixed detector factors.  The normal-closure
lemma proves that all such values lie in `V_beta(G)` for every finite group
`G`, so this is a stricter symbolic certificate format rather than a finite
subgroup search.

## Green and corridor progress

The current final local branch is named
`bi_free_universal_corridor_bottleneck`.  An interval reaches it only after:

- coloured YBE holds;
- no semisplit family survives;
- pair-closure local-minimality is exact;
- no product-permutation witness routes it to a closed product branch;
- the local coordinate-kernel closure is universal rather than equality;
- every individual output coordinate-kernel seed pair separately generates
  the universal admissible family, not merely the aggregate seed set;
- no known whole-solution finite-`G` branch applies.

The finite detector candidate for this branch is a product of:

- symmetric groups on left and right Green kernel-block quotients;
- left and right Schutzenberger action groups of regular Green classes;
- left and right atom quotient inner groups when the atom layer is rack-like;
- already proved quotient or branch detector factors.

This product is finite and depends only on the interval and the quotient
detector, not on `n`.
The executable factor helper now includes these atom inner groups directly,
with duplicate concrete group tables removed, so the code-level detector
candidate matches the atom-rack lift criterion.
The corridor helper also accepts fixed `extra_groups`, which are appended to
the Green factors as named factors before longitude profiles, exact-image
audits, and direct-product subgroup checks.  This is the executable slot for
the quotient detector `Q`, known branch factors, and endpoint/unit detector
groups in `H(pi,Q)`; the supplied list is still fixed at the interval level
and cannot depend on braid index.
For intervals routed to a known total branch before the corridor fork, the
local bottleneck summary now records the known-branch detector reason, group
order, and `A_G` factor size.  Thus a closed tag cannot silently stand in for
an unspecified finite detector.
For intervals routed to closed product branches, the same summary now records
closed product detector certificates, actual product detector groups when
available, and any delegated affine gaps.  The remaining corridor fork is
reached only after these explicit product/known detector records fail to
apply.
The merged accessors `closed_detector_groups`,
`closed_detector_group_orders`, `closed_detector_product_group`,
`closed_detector_product_group_order`, and `closed_detector_gaps` now expose
the actual finite local detector data for `product_finite_g_branch`,
`known_total_branch`, and `locally_nondegenerate_branch` verdicts whenever the
current proof ledger supplies it.  Multiple branch factors are combined into a
single interval-level product group `G_i`; delegated affine rows and open
product/corridor verdicts remain explicit gaps rather than silently entering
the congruence-chain rack assembly.
The new note `proofs/bifree_corridor_endpoint_factorization.md` performs the
proof-side product assembly for the remaining corridor branch.  It proves that
once each Green/corridor endpoint component has an endpoint-longitude
expression in one fixed factor of `H(pi,Q)`, all factor witnesses assemble into
the single product detector `H(pi,Q)`, and identity finite-`H` longitude data
kills the residual readout.  It does not prove the missing endpoint
longitudinalization lemma; it narrows the remaining all-`n` task to producing
those endpoint expressions uniformly for arbitrary finite fibres and quotient
colours.
The group-only executable helpers
`endpoint_longitude_expression_audit(...)` and
`endpoint_product_longitude_expression_audit(...)` now implement this
certificate layer directly.  They evaluate displayed endpoint expressions in
fixed finite factors, build the literal direct-product witness in
`V_beta(H(pi,Q))`, and record whether identity product-longitude data kills the
endpoint tuple.  This extends the existing unit-composite expression audit
from transformation monoid unit groups to arbitrary finite detector factors.
The companion readout helpers `endpoint_coordinate_readout_audit(...)` and
`endpoint_residual_readout_audit(...)` record the final faithful-readout gate:
an identity endpoint tuple must fix the corresponding residual coordinate, and
coordinate rows bundle into a residual-tuple implication.  They make the
endpoint-factorization proposition executable as a proof checklist once the
uniform endpoint expressions have been supplied.
`endpoint_residual_action_audit(...)` now bundles the supplied residual rows
for one braid word, checks braid-data consistency, and optionally checks a
claimed row count.  It separates "all displayed rows satisfy the endpoint
detector implication" from "the displayed table covers every relevant residual
input," keeping finite tables useful without turning them into theorem-level
evidence by accident.
The new note `proofs/artin_defect_longitudinalization_sieve.md` sharpens the
open endpoint target further.  It proves that the Artin permutation defect
`beta(w)p_beta(w)^-1` lies in the normal closure of the recursive longitudes
and that every finite-group value of such a defect belongs to `V_beta(G)` by
changing assignments to absorb the conjugators.  Therefore a displayed
endpoint product of Artin permutation defects is automatically a
longitude-subgroup witness.  The code exposes
`artin_permutation_defect_witness_audit(...)`,
`endpoint_artin_defect_audit(...)`, and
`endpoint_product_artin_defect_audit(...)` to verify supplied displays and
assemble them into one fixed product detector.  This still does not prove the
remaining local theorem; the missing statement is now that every elementary
Green/corridor endpoint generator has such an Artin-defect display in the
fixed factors of `H(pi,Q)`.
The detector-lift theorem
`proofs/artin_detector_lift_criterion.md` now isolates the unbounded
braid-word recursion behind these endpoint expressions.  If a fixed
Green/corridor observer factor carries live-strand labels `(m_k,u_k)` and its
positive and negative crossing rows agree with the active `U x U` Artin
detector update rules, then induction gives
`u_k(beta)=phi(L_k(beta))` for every braid word.  Hence a signed product of
terminal `u`-labels is automatically an endpoint-longitude expression.  The
new helpers `artin_detector_lift_transition_audit(...)` and
`artin_detector_lift_braid_audit(...)` check the finite row rule and the
global recursion convention.  The missing local theorem is now the finite
row-by-row verification of these detector-lift identities for the remaining
Green kernel-block, Schutzenberger, atom-inner, quotient, and endpoint-unit
observer rows.  The atom-inner part is now closed once atom descent and
totality are known: `proofs/atom_inner_detector_lift_rows.md` proves that
rack-like atom quotient inner groups satisfy the positive detector row by
rack self-distributivity, and the negative detector row is the inverse of the
positive row.  Thus the unresolved row identities are the Green kernel-block,
Schutzenberger, and lower endpoint/unit holonomy rows.
The Green kernel-block and Schutzenberger row identities have now been
replaced by a first-output defect criterion.  The note
`proofs/green_first_output_defect_criterion.md` proves that every such row is
determined by one defect `d_C(a,q)=g(q^a)g(q)^-1`; the second output follows
from `g(a)g(q)=g(q^a)g(a^q)`.  In the no-local-only case, kernel-block
defects are homomorphic images of Schutzenberger defects.  The remaining
Green target has now been sharpened again by
`proofs/green_defect_kernel_quotient_detection.md`: quotienting an observer
`U_C` by the normal closure `Def_C` of all first-output defects makes every
projected row exactly side-opposite rack-Artin, so `U_C/Def_C` is handled by
the detector-lift theorem.  The only remaining Green/Schutzenberger
obstruction has now been expressed as a finite potential problem:
`proofs/green_defect_potential_coboundary.md` proves that each elementary
defect is `eta(q^a)eta(q)^-1` for a `Def_C`-valued potential on the retained
edge-germ graph.  This made the intermediate Green target the
Artin-transport principalness of the potential, equivalently the transported
endpoint `D_C(beta) in V_beta(Def_C)`, plus the lower endpoint/unit holonomy
target.
The Artin-defect-only version of this target is now ruled too strong by
`proofs/artin_defect_abelianization_barrier.md`: Artin permutation defect
values have trivial image in every abelian target, but current Green defect
kernels can have nontrivial abelian row defects.
The correction is recorded in
`proofs/green_defect_abelianization_split.md`: first project the defect
endpoint to `Def_C/[Def_C,Def_C]` and prove that finite abelian endpoint is
ordinary longitude-visible; after that, the remaining endpoint lies in
`[Def_C,Def_C]`, where Artin-defect or detector-lift methods can be applied
without losing abelian data.
The abelian visibility phrase is now exact rather than schematic:
`proofs/abelian_longitude_image_criterion.md` proves that for a finite
abelian group `A`, the subgroup `V_beta(A)` is generated by all `a^{m_ij}`,
where `m_ij` ranges over the abelianized recursive-longitude exponent matrix.
Thus the projected `AbDef_C` endpoint has a precise finite matrix-subgroup
target before the residual commutator endpoint is considered.
The Green row obstruction has also been split more sharply by
`proofs/green_balanced_defect_gauge_decomposition.md`: if
`A=g(a)`, `Q=g(q)`, `B=g(q^a)`, and `C=g(a^q)`, then
`B Q^-1 = [A,Q] Q(CA^-1)^-1Q^-1`.  The commutator is an Artin permutation
defect value, so the raw Green/Schutzenberger row mismatch reduces to the
terminal second-output gauge holonomy `CA^-1`.  Thus Green kernel-block and
Schutzenberger rows should no longer be listed as independent open rows; the
remaining row burden is lower endpoint/unit gauge holonomy, plus the separate
atom descent/totality issue.
The certificate format for that burden is now recorded in
`proofs/terminal_gauge_longitudinalization_criterion.md`: gauge increments
`s_k=g_k g_{k-1}^-1` telescope as `s_t...s_1=g_t g_0^-1`, and it is enough to
give the terminal endpoint an ordinary longitude expression, literal
subgroup witness, Artin-defect display, or abelian matrix witness in fixed
gauge factors.  The new terminal-gauge audits reuse the existing endpoint
product-witness machinery.
The principal lower-gauge subcase is closed by
`proofs/principal_gauge_extension_detector.md`: if the lower row is
`(a,r)*(b,s)=(a*b,c(a,b)s)`, then the row-level YBE is exactly the
nonabelian rack-cocycle law for `c`, the extension `A x U` is a finite rack,
and the fixed group `Inn(A x U)` supplies the detector-lift rows.  The
make-or-break structural target is therefore principal-gauge normal form, or
else a nonprincipal row must become the seed for a normalized-law B route.
This has now been sharpened again by
`proofs/transport_state_rackification_detector.md`: principality is not needed
for strand-continuing lower gauge rows.  A row
`((a,r),(b,s))->((a*b,F_{a,b,r}(s)),(a,r))` defines a finite rack on `A x E`
whenever the completed row is bijective YBE, and its inner group detects the
transport state by the same rack-inner detector-lift theorem.  The remaining
structural burden is descent separation: non-strand-continuing lower motion
must be completely visible in Green kernel-block or Schutzenberger factors.
The new continuation gate
`proofs/continuation_congruence_descent_gate.md` makes that burden exact:
generate the least admissible congruence from all continuation changes
`x~v`.  Equality is precisely the strand-continuing case, proper mixed closure
contradicts local-minimality, and the only surviving nontrivial case is an
all-universal continuation corridor.  The next theorem target is therefore
universal continuation visibility in the fixed Green/Schutzenberger readouts,
or a normalized-law B construction from that universal corridor.
The elementary continuation refinement
`proofs/elementary_continuation_closure.md` removes collective-only
continuation as a possible loophole: in a local-minimal interval, each single
nontrivial seed `x~v` already has universal admissible closure.  The helper
`continuation_seed_pair_closure_audits(...)` exposes the seed-by-seed closure,
and failures certify that the interval was not a valid local-minimal target.
The universal-continuation derivation certificate
`proofs/universal_continuation_derivation_certificate.md` exposes the finite
transport ledger inside each universal single-seed closure.  The helper
`continuation_seed_universal_derivation_audits(...)` checks that every
nontrivial fibre edge in the universal closure has a recorded derivation row.
The remaining descent-separation proof can now be stated edge-by-edge: route
each derived edge through fixed Green/Schutzenberger/atom readouts, or extract
B from one derived edge.
The readout-propagation criterion
`proofs/continuation_readout_propagation.md` compresses that edge-by-edge
burden once a fixed readout relation is identified.  If the relation is
admissible and contains a representative continuation seed, it contains the
whole generated closure.  The helper
`continuation_seed_readout_propagation_audits(...)` records admissibility,
seed containment, generated-edge containment, and missing edges.
The readout-kernel admissibility criterion
`proofs/readout_kernel_admissibility.md` turns finite detector labels into
that fixed readout relation.  `readout_kernel_audit(...)` builds the kernel
partition family and runs the exact local congruence transport test, exposing
the first failed row if the proposed labels do not descend.
The readout descent-separation certificate
`proofs/readout_descent_separation_certificate.md` now packages the finite
criterion needed by transport-state rackification.  The helper
`readout_descent_separation_audit(...)` combines the readout kernel,
continuation propagation, and surviving seed rows; when it passes, the quotient
row is strand-continuing.
The readout-kernel quotient interval note
`proofs/readout_kernel_quotient_interval.md` makes the quotient row an
executable object.  The helpers `quotient_interval_by_family(...)` and
`readout_kernel_quotient_interval(...)` construct the descended local table on
readout blocks, and the descent-separation audit now stores the quotient and
its continuation audit.
The product readout-kernel assembly note
`proofs/product_readout_kernel_assembly.md` gives the fixed-factor product
step.  Tuple-valued product labels have kernel equal to the meet of the factor
kernels, and `product_readout_kernel_audit(...)` records factor admissibility,
the product kernel, and the meet identity.
The product descent-separation note
`proofs/product_readout_descent_separation.md` records the seed-level
consequence of that meet identity.  A tuple-valued product readout kills a
continuation seed exactly when every factor kills it, and
`product_readout_descent_separation_audit(...)` exposes factor seed survival
alongside the product quotient certificate.
The readout seed-saturation note `proofs/readout_seed_saturation.md` computes
the least admissible coarsening of one factor kernel that also kills all
continuation seeds.  The local-minimal corollary says that a non-killing
admissible equality factor has universal seed-saturation, so lost information
must be carried by another fixed factor or by the transport-state rack
quotient.
The local-minimal seed-saturation dichotomy note
`proofs/local_minimal_seed_saturation_dichotomy.md` exposes that corollary as
an executable audit.  It rejects non-local-minimal intervals, checks that
kernel and saturation kinds are equality/universal, and flags forced universal
collapse as an external-routing obligation.
The lost-edge external routing note `proofs/lost_edge_external_routing.md`
turns that obligation into a finite ledger.  It distinguishes descent quotient
labels from external endpoint routing labels and records which
seed-saturation edges are lost, routed, or still unrouted.
The routed lost-edge endpoint witness note
`proofs/routed_lost_edge_endpoint_witness.md` then attaches the all-`n`
obligation to that ledger: every routed lost edge must have a product
endpoint-longitude certificate in fixed detector factors.  The helper
`routed_lost_edge_endpoint_witness_audit(...)` records missing, extra, and bad
witnesses without adding the routing labels back into the descent quotient.
The chart-transport collapse
`proofs/chart_transport_collapse.md` removes another source of proof noise:
because `V_beta(G)` is normal for every finite group `G`, one
endpoint-longitude witness for a representative elementary generator gives
witnesses for all finite chart-conjugate transports.  The code-level helper
`conjugate_longitude_subgroup_witness(...)` records this at certificate level.
At this stage the final A-route theorem was stated in
`proofs/descent_separation_transport_rack_closure.md`: transport-rack closure
was already proved, while descent separation remained to be routed.  The later
unit-continuation, two-sided unit, mixed-unit, triangular, one-colour,
kink-predecessor, and master-local notes now record that route: the remaining
motion is either visible to fixed Green/Schutzenberger/atom/unit factors,
rackified on a finite transport state, routed to a closed product/permutation
branch, or forced to singleton fibres.
The final constant-observer universal-continuation case has now been split by
`proofs/unit_continuation_final_obstruction.md`.  In the case
`Theta^cont=Nabla` and `K^O=Nabla`, a completed-context continuation branch
that contributes to a residual braid action has a permutation composite, so
the unit-factorization lemma forces every transition factor in that branch to
be a unit.  Thus nonunit/reset continuation labels cannot be the moving
obstruction.  What was then the unit-continuation longitude target is consumed
by the later lower-row classification and master-local assembly.
The two-sided unit-collapse note `proofs/two_sided_unit_collapse.md` sharpens
this last case again.  If all remaining lower coordinate sections are
bijective on both sides, the row is locally nondegenerate and belongs to the
closed nondegenerate/guitar branch; if the row is strand-continuing, it is
already handled by transport-state rackification.  Thus the only continuation
shape left after the fixed readouts is mixed-unit context recovery: some
one-sided nonunit information is lost locally but recovered by context before
endpoint readout.  The helper `two_sided_unit_collapse_audit(...)` records the
section-unit split and lists the non-two-sided rows that remain.
The companion-separation note `proofs/mixed_unit_companion_separation.md`
makes the mixed-unit seed sharper.  In any bijective local row, if a
coordinate section collapses two inputs, the companion output coordinate must
separate them.  Thus mixed-unit context recovery is a finite shuttle of
section-kernel distinctions through companion outputs.  The helper
`section_kernel_companion_audit(...)` records every such collision and its
companion outputs.  A positive proof must route these shuttle edges through
fixed readouts or transport-rack quotients; a negative proof must upgrade a
shuttle cycle to the normalized-law B sequence.
The rank-profile collapse
`proofs/rank_profile_collapse_mixed_unit.md` sharpens the shuttle seed again.
Proper nontrivial section-kernel profiles are Green/Schutzenberger-visible,
so after those fixed observers are constant the only hidden rank-losing
section has universal kernel and is constant.  The helper
`section_rank_profile_collapse_audit(...)` records rank, kernel kind, image,
and injective non-surjective side cases.  The remaining make-or-break local
classification is constant-section triangular YBE rows in the local-minimal
bottleneck branch.
The triangular bundle partition note
`proofs/constant_section_triangular_bundle_partition.md` records the structure
forced by bijectivity in that residue.  If
`T(x,y)=(alpha(x),beta_x(y))`, then `alpha` is surjective, every `beta_x` is
injective, and for each output `u`, the images `beta_x(A_b)` for
`x in alpha^{-1}(u)` partition the companion codomain.  The side-dual
statement holds for rows `T(x,y)=(lambda_y(x),gamma(y))`.  The helper
`triangular_bundle_audit(...)` exposes the constant-map fibres and companion
image blocks.  Thus the remaining local classification is triangular bundle
holonomy, not an arbitrary constant-section triangular map.
The recovery inverse note `proofs/triangular_bundle_recovery_inverse.md`
computes the inverse of a triangular bundle row.  Given an output `(u,v)`,
the partition first recovers the unique block label `x=r_u(v)` and then the
within-block input `y=beta_x^{-1}(v)`.  The side-dual version recovers `y`
first and then `x`.  The helper `triangular_recovery_audit(...)` records the
output-to-source table and checks that the recovery formula is bijective.  The
remaining obstruction is therefore triangular recovery holonomy in these
finite labels and inverse companion coordinates.
The constant-column collapse note
`proofs/constant_column_collapse_triangular.md` then removes the non-Latin
half of that triangular residue.  In a hidden constant-section triangular row,
any non-bijective opposite column `C_y(x)=beta_x(y)` cannot have a proper
kernel profile without being seen by the fixed Green/Schutzenberger observers,
so it is constant.  If one such column is constant, bijectivity of the
companion maps forces every opposite column to be constant; the row is
therefore product/permutation holonomy and routes to a closed branch.  The
helper `triangular_column_collapse_audit(...)` records this product-collapse
case and isolates the only remaining triangular case: Latin-unit triangular
rows, where `alpha`, every `y -> beta_x(y)`, and every
`x -> beta_x(y)` are bijections.  The next theorem target is the Latin-unit
triangular longitude theorem for the fixed group `U_triangle`.
The Latin triangular YBE split note `proofs/latin_triangular_ybe_split.md`
then separates the Latin-unit target into alpha transport and companion shear.
Expanding the coloured YBE in triangular form gives the alpha cocycle
`alpha_{a.b,(a*b).c} alpha_{a,b}=alpha_{a,b.c}`, independent of the companion
variables, so alpha is product/permutation holonomy and is already in a closed
route.  The helper `latin_triangular_ybe_audit(...)` records that equation
together with the middle-companion and endpoint-shear equations.  The final
triangular obstruction is therefore companion-shear longitude visibility in a
fixed group `U_shear`, not alpha transport.
The one-colour collapse note
`proofs/one_colour_latin_triangular_collapse.md` removes the one-colour shear
case.  With one colour, the alpha equation is `alpha^2=alpha`, hence
`alpha=id`; the middle equation then forces every companion map `beta_x` to be
the identity, so opposite columns are constant and cannot be Latin unless the
fibre is singleton.  The helper
`one_color_latin_triangular_collapse_audit(...)` records this split and shows
that the tempting row `T(x,y)=(x,x+y mod 2)` is Latin as a bijection but not a
YBE row.  Any remaining companion-shear obstruction must be genuinely
multi-colour.
The kink-predecessor cancellation note
`proofs/kink_predecessor_latin_triangular_cancellation.md` removes the
rack-base multi-colour shear too.  For a rack base, the kink map
`kappa(b)=b*b` satisfies `L_{kappa(b)}=L_b`; using
`c=kappa^{-1}(b)` gives `b*c=b` and the alpha cocycle gives
`alpha_{b,c}=id`.  The third-output shear equation then forces
`y -> y circ_{b,c} z` to be constant, while Latin-unit says it is bijective,
so `|X_b|=1`.  The helper
`rack_kink_latin_triangular_collapse_audit(...)` records rack form, kink
predecessors, alpha identities, predecessor-column constancy, and the absence
of non-singleton Latin fibres under the theorem hypotheses.  Conditional on
the preceding reductions, this eliminates the final lower-row obstruction in
the bi-free universal-corridor branch.
The follow-up abelian-kernel lift note
`proofs/unit_continuation_abelian_kernel_lift.md` splits this endpoint target
through the finite abelianization of the fixed unit group.  It is enough to
prove the abelianized endpoint with the existing matrix-longitude criterion,
lift that quotient witness to `U(M_cont)`, and prove the correction
`S_beta*v_beta^-1` by a witness using assignments in the commutator subgroup.
The helper `normal_quotient_longitude_lift_audit(...)` records this
certificate-level quotient-plus-kernel proof.
The derived-series reduction
`proofs/unit_continuation_derived_series_reduction.md` iterates the same
quotient-plus-kernel step down the finite derived series.  For solvable
unit-continuation groups, the endpoint theorem is reduced to abelian
matrix-longitude witnesses in the derived quotients.  For nonsolvable unit
groups, the remaining nonabelian endpoint must live in the stable perfect
residual.  The helpers `derived_series_audit(...)` and
`subgroup_as_group(...)` make the finite stages explicit.

The Green atom layer is now explicit.  Retained edge-germs in a regular Green
`R`-class have a saturated atom relation generated by `q^a ~ q`.  The helper
`atom_action_summary(...)` checks whether completed rows descend to

```text
p(a) triangleright p(q) = p(a^q)
p(a^q) triangleleft p(q) = p(a).
```

If total and well-defined, `atom_quotient_solution(...)` constructs a finite
right-rack-like YBE layer, and `atom_quotient_rack_audit(...)` checks
bijective right translations and right self-distributivity directly.

The descent-closure helper `atom_descent_closure_summary(...)` records the
least coarsening needed for descent.  In all current tiny exhaustive audits
and named stress rows this closure is trivial, but this is diagnostic only.
The new `atom_descent_quotient_rack_audit(...)` checks whether a nontrivial
closed quotient is nevertheless a total finite rack layer.  The later
descent-separation, transport-rack, triangular, and kink-predecessor notes now
route the lost lower information to fixed endpoint/unit or transport-state
factors; a non-rack atom quotient is no longer treated as a standalone final
B seed without the normalized-law upgrade.

## Counterexample route status

The B route has been reduced to normalized-law behavior.  It is not enough to
miss one finite detector group.  To defeat every finite rack, a candidate must
provide:

- an explicit finite bijective YBE solution `X`;
- a symbolic YBE proof;
- braid words `beta_j in B_{q_j}` with `q_j -> infinity`;
- eventual finite-`G` longitude invisibility for every finite group `G`;
- explicit moved tuples under `rho_{X,q_j}`;
- a proof that the sharp obstruction theorem converts this into failure
  against every finite rack.

The diagonal product lemma says that if one explicit local residual interval
has no finite detector group at all, then products of the first `j` finite
groups and right-strand stabilization yield the required normalized-law
sequence.  No such explicit interval has been found.

The normalized-law prefix gate is now explicit.  A sequence of free words
`w_j` that is a law on every finite group of order at most `j` is eventually
a law on every fixed finite group.  The helper
`law_sequence_prefix_audit(...)` checks finite prefixes of this condition
against listed groups.  This supplies only the finite-group invisibility side
of B; a counterexample still needs a fixed finite YBE solution and moved
tuples for the corresponding law braids.

## Proof-Critic Gap

The candidate Master Local-Minimal Residual Theorem assembly in
`proofs/master_local_residual_positive_closure.md` was reviewed by a proof
critic.  The critic found a fatal gap recorded in
`proofs/proof_critic_gap_audit.md`.

The proposed finite interval-level product group is

```text
H(pi,Q)
```

from Green, Schutzenberger, atom, known-branch, endpoint/unit, and
transport-state factors, with no braid-index parameter.  However, the branch
does not yet prove the required implication

```text
Lambda_{H(pi,Q),n}(beta)=Lambda_{H(pi,Q),n}(1)
    => Delta_n(beta)=1.
```

The issue is not the sharp obstruction theorem or the congruence-chain kernel
direction.  The gap is that
`proofs/bifree_corridor_endpoint_factorization.md` supplies a conditional
assembly lemma, not the missing endpoint expressions or the faithful residual
decomposition, and
`proofs/descent_separation_transport_rack_closure.md` still states descent
separation as a theorem target rather than proving it.

The current missing theorem package is uniform descent-separation and
endpoint-longitudinalization for every local-minimal
`bi_free_universal_corridor_bottleneck` interval.  It must prove fixed-factor
faithful readouts and `V_beta` membership for all residual
Green/Schutzenberger/atom/lower endpoint components, uniformly in `n`.

`proofs/descent_endpoint_repair_contract.md` now states this as an exact
repair contract.  If every bottleneck interval admits a fixed
descent-separating readout, fixed external endpoint groups, a faithful
reconstruction rule, and all-`n` `V_beta` witnesses for routed endpoints, then
the local finite detector implication follows.  A failure of any item is not
yet outcome B, but it is the finite seed that must be upgraded to a
normalized-law obstruction.

## Verification snapshot

At the latest verified snapshot:

- `python -m unittest discover -s tests` passed with 380 tests;
- `python -m compileall -q src tests tools` passed;
- `node --check tools/build_reduction_audit_workbook.mjs` passed;
- the proof log DOCX and reduction audit workbook were regenerated, and the
  workbook preview/OOXML marker checks included the routed-edge witness,
  unit-continuation, derived-series, two-sided unit-collapse, and
  mixed-unit companion-separation, rank-profile collapse, triangular
  bundle-partition, triangular recovery-inverse, constant-column collapse,
  Latin triangular YBE-split, one-colour Latin-collapse, and kink-predecessor
  Latin-cancellation rows, plus the master local positive-closure assembly
  and final completion audit;
- LibreOffice/`soffice` was unavailable, so DOCX visual render QA could not
  be completed;
- the Desktop zip was overwritten rather than versioned separately.

## Superseded Final Completion Audit

`proofs/final_completion_audit.md` records the final checklist after the
master local positive closure assembly.  It audits the required reductions:
quotient/residual setup, sharp obstruction theorem, congruence-chain
induction, semisplit local-minimality, known branches, fixed detector
independence from `n`, and the non-use of finite search as the all-`n` proof.
That optimistic conclusion is now superseded by
`proofs/proof_critic_gap_audit.md`.

The requested GPT-5.5 Pro proof critic could not be reached from this local
session.  Chrome and in-app Browser control both failed before tab discovery
with the browser bridge diagnostic

```text
windows sandbox failed: spawn setup refresh
```

so the repository records an internal completion audit rather than an external
model review.
