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

- rack-type, involutive, permutation-form, and left-nondegenerate/guitar
  branches;
- affine and fibre-size-two affine over `F_2` branches in the audited form;
- pairwise-linking and one-colour product holonomy branches;
- coboundary/product-label telescope branches;
- finite semidirect affine and finite product detector branches already
  reduced to fixed finite groups;
- direct `Sym(X)` detection for the known symbolic subbranches.

The known-branch routing now has an explicit detector certificate.  The helper
`known_branch_detector_certificate(X)` returns `G=1` for involutive tables,
`G=C_ord(sigma tau)` for permutation-form tables, and the direct
`Sym(X)` detector for rack-type or left-nondegenerate/guitar tables.  It
records the detector group order and the sharp rack factor size `2*|G|^2`,
with an explicit marker that no braid index is used.  The note
`proofs/left_nondegenerate_guitar_branch.md` records the known guitar-map
theorem in this detector language: the left-nondegenerate solution is
conjugate in every braid degree to its derived rack, so `Inn(D_X)` and hence
`Sym(X)` detect it.

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

The larger affine-linear direct-symmetric stress note
`proofs/affine_linear_direct_symmetric_stress.md` records reported scans on
`F_2^3` and `F_3^2` with no two-strand direct-`Sym(X)` gate failures.  This is
guardrail evidence only: the actual unresolved obstruction is all-`n`
terminal gauge/unit longitudinalization, not a two-strand crossing-order
miss.

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
The generated exact-image audit now records this at the fixed detector-state
level as well: adding a fixed `C5` extra factor to the affine stress row raises
the exact `n=2` reachable detector state count from `12` to `60`, with no
kernel or collision failure.
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
closed left-nondegenerate/guitar branch; if the row is strand-continuing, it is
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
The helper `unit_composite_derived_series_lift_audit(...)` now checks a
supplied endpoint lift through those stages: each stage witness must use
assignments in the current derived subgroup and must push the correction into
the next derived subgroup; the final witness handles the stable perfect
residual.  A successful audit evaluates the combined witness back in the
original unit group and proves the supplied terminal unit composite lies in
`V_beta(U(M))`.
The companion `proofs/unit_continuation_perfect_residual_audit.md` isolates
the final nonsolvable checkpoint.  The helper
`unit_perfect_residual_longitude_audit(...)` restricts the finite unit group
to its stable perfect residual `P` and checks whether the final derived
residual endpoint lies in `V_beta(P)`.  Thus every terminal-unit obstruction
after the abelian quotient stages is now explicitly located in a fixed
perfect group.
The product assembly note
`proofs/unit_continuation_derived_product_detector.md` then packages multiple
terminal-unit monoids into one fixed product detector.  The helper
`unit_composite_product_derived_series_lift_audit(...)` takes the combined
witness from each derived-series factor audit, embeds those witnesses into
the direct product of the unit groups, and verifies the product endpoint
inside `V_beta(prod_i U(M_i))`.
The current sharpest positive statement is
`proofs/terminal_gauge_artin_defect_target.md`: every remaining terminal
gauge endpoint `S_beta=g_terminal g_initial^-1` in a fixed interval-level
unit or Schutzenberger factor should be a product of evaluated Artin
permutation defects `beta(w)p_beta(w)^-1`.  The Artin-defect sieve would then
put `S_beta` in `V_beta(U)`, and product assembly would give the fixed
detector implication.  This identity is not yet proved; if it fails, the
failure still has to be upgraded to a normalized-law sequence before it is
outcome B.
The new guardrail `proofs/terminal_gauge_abelianization_barrier.md` refines
this statement: Artin permutation-defect values always lie in `[U,U]`, so a
terminal gauge endpoint with nontrivial image in `U/[U,U]` cannot have a
pure Artin-defect display.  Such endpoints are not counterexamples by
themselves; they must first be tested by the abelian longitude matrix
criterion and then lifted through the normal quotient-plus-kernel certificate.
Accordingly, the honest final terminal-gauge target is now abelian quotient
visibility plus a commutator/perfect-residual correction, with the pure
Artin-defect display reserved for the commutator-level endpoint.
The executable companion
`proofs/unit_continuation_abelian_quotient_audit.md` adds the first finite
checkpoint for this route.  The helper
`unit_composite_abelianization_audit(...)` projects the final unit composite
to `U(M)/[U(M),U(M)]`, computes `V_beta` in that finite abelian quotient, and
records whether the abelian endpoint is already closed by the matrix route.
When it is closed, the remaining endpoint is exactly a commutator correction;
when it is not closed, the failure is a precise abelian quotient seed that
still has to be upgraded to normalized laws before it can be outcome B.

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
The helper `descent_endpoint_repair_contract_audit(...)` now bundles supplied
descent, endpoint-action, and routed-edge certificates and reports which part
of a proposed repair package fails.  Routed lost-edge ledgers must match the
same saturated descent quotient as the supplied descent certificate, so valid
endpoint witnesses cannot be imported from a different local repair package.
`proofs/local_minimal_descent_readout_collapse.md` now records the
local-minimal consequence for the combined descent readout itself.  If its
kernel is admissible and contains every continuation seed, then equality means
there were no nontrivial seeds and the row was already strand-continuing;
otherwise any nontrivial seed forces the readout kernel to be universal.  Thus
no proper partial descent quotient can be the hidden final layer in a genuine
local-minimal bottleneck; the lost information must be recovered by fixed
external endpoint factors or by a normalized-law escape.
The helper `local_minimal_descent_readout_collapse_audit(...)` records the
same split in executable form for supplied interval/readout data.

`proofs/normalized_law_domination_dichotomy.md` now proves that the
normalized-law obstruction format is forced, not optional.  For a finite
solution `X`, finite-rack domination is equivalent to the existence of one
finite group `G` whose identity Artin-longitude kernel lies in
`ker rho_X` for every braid index.  Failure of such a group diagonalizes over
finite groups and right-stabilizes to braid indices `q_j -> infinity`, giving
eventual identity finite-`G` longitude data for every finite group while still
moving `X`.  The same dichotomy is stated for a fixed quotient/residual
interval with `beta_j in N_{q_j}`.  This does not construct outcome B, but it
proves that a normalized-law sequence is the forced shape of any negative
resolution.
`proofs/global_local_normalized_fork.md` now removes the remaining global
ambiguity.  Maximal congruence-chain intervals are local-minimal, local fixed
group detectors descend by `Q_i=Q_{i+1} x A_{G_i}` to a global finite rack, and
failure of one local detector diagonalizes to a local normalized-law residual
obstruction.  Thus the whole Sawin problem is equivalent to the Master
Local-Minimal Detector Theorem; if one interval fails it, the total solution of
that interval is already a finite YBE counterexample.  The helper
`local_normalized_law_prefix_witness_audit(...)` checks one supplied local
product-prefix row, including quotient/base kernel membership, finite-product
longitude invisibility, right stabilization, and residual tuple movement.
`proofs/symmetric_detector_reduction.md` now shows that arbitrary finite group
detectors may be replaced by symmetric group detectors.  The left regular
embedding `G -> S_m` gives `K_{S_m}(n) subset K_G(n)`, so a positive local
detector may be taken to be `S_m`, and a negative normalized-law construction
may diagonalize against `S_j` only.  The helper
`symmetric_detector_reduction_audit(...)` records this containment at the
finite-signature level.
`proofs/symmetric_tower_monotonicity.md` records the descending tower
`K_{S_M}(n) subset K_{S_m}(n)` for `M>=m`, using the fixed-point inclusion
`S_m -> S_M`.  Thus positive detector degrees are upward closed, and a
sequence invisible to `S_j` is eventually invisible to every fixed `S_m`.  The
helper `symmetric_tower_monotonicity_audit(...)` checks this inclusion at the
finite-signature level.
`proofs/local_symmetric_detector_dichotomy.md` now packages the final local
fork as a symmetric-degree dichotomy: either some fixed `S_m` detects the
interval for all braid indices, or for every `j` there is a local residual
mover invisible to `S_j`.  The helper
`local_symmetric_tower_prefix_sequence_audit(...)` checks supplied finite
prefixes of the second alternative.
`proofs/sawin_last_strand_law_reduction.md` now records only the safe
last-strand law direction.  On the last-strand point-pushing subgroup,
identity finite-`G` longitude data implies the pushed word is an ordinary law
on `G`; the converse is false.  Fadell-Neuwirth layer extraction still shows
that any moving braid in `K_G(n)` has a moving point-pushing layer
`iota_r(w)` which remains in `K_G(r)`, and hence whose word is necessarily a
law on `G`.  The helper `last_strand_law_exactness_audit(...)` compares
ordinary law identity with actual finite-longitude identity and flags gaps.
`proofs/point_pushing_action_image_variety.md` is therefore a superseded
moving-variety diagnostic rather than an equivalent reformulation.  For
`P_k(X)=<rho_{X,k+1}(A_{1,k+1}),...,rho_{X,k+1}(A_{k,k+1})>`, variety escapes
produce candidate point-pushing movers, but they become B evidence only after
the corresponding point-pushed words are also proved to lie in the actual
finite-longitude kernels.  The helper `point_pushing_variety_escape_audit(...)`
computes bounded action-image escape rows with generator-word representatives,
while `point_pushing_variety_prefix_audit(...)` scans finite arity prefixes as
finite evidence only.
`proofs/point_pushing_fixed_variety_domination.md` is likewise retained as a
sufficient positive route and search heuristic, not as a proved equivalence:
if one fixed finite variety contains all point-pushing action images, then the
actual `K_G` point-pushing layers are killed; fixed-variety failure alone does
not give a normalized-law counterexample.
`proofs/fadell_neuwirth_layer_extraction_guardrail.md` now isolates the
convention-sensitive bridge behind that equivalence.  It records that deleting
the last strand and adding an unused right strand preserve `K_G`, decomposes a
pure braid recursively into standard right-stabilized point-pushing layers,
and proves that if each layer is trivial on its own `X^r`, then its
right-stabilized extension is trivial on `X^n`.  Hence a moving `K_G` braid
does force a moving actual point-pushing `K_G` layer; its word is an ordinary
law only as a necessary condition.  The note is also a guardrail: conjugated
layers or non-right embeddings require their own triviality proof.
`proofs/rack_point_pushing_operator_label_invariant.md` now records the
correct rack-only point-pushing structure.  For a finite rack `Y`, the
last-strand point-pushing image `Q_Y(n)` maps to the finite group-Hurwitz
operator-label image on tuples `(L_y)` in `Inn(Y)`, and the vertical kernel
has exponent dividing `exp Inn(Y)` uniformly in `n`.  The whole image
`Q_Y(n)` need not have bounded exponent; the generated audit
`proofs/rack_point_pushing_operator_label_audit.md` records the warning row
for the three-element dihedral rack where `exp Inn(Y)=6` but the checked
arity-`3` point-pushing image exponent is `36`, while the vertical exponent is
`1`.  The resulting point-pushing theorem target is the finite augmented
Artin-envelope lemma: every finite bijective YBE point-pushing tower should
have a finite operator-label Hurwitz model up to uniformly bounded-exponent
vertical noise.
`proofs/last_strand_law_gap_audit.md` now corrects the strongest
point-pushing reformulation.  The implication
`w in Law_k(G) => iota_{k+1}(w) in K_G(k+1)` is false for `k>=2`: the
three-element dihedral rack and the word `(x_1 x_2^{-1})^6`, a law on `S_3`,
give a last-strand point-pushing braid that moves `X^3`, while the streamed
Artin-longitude check shows nonidentity `S_3` longitude data.  Thus ordinary
law identity is only a necessary-condition filter for last-strand
finite-longitude identity, not a replacement for it.  The helper
`point_pushing_exponent_escape_audit(...)` now records this finite guardrail
row and flags `exposes_naive_law_gap`.
`proofs/point_pushing_kernel_layer_criterion.md` records the repaired exact
form.  For a fixed finite group `G`, `K_G(n) <= ker rho_X,n` for all `n` iff
every last-strand point-pushing braid `iota_r(w)` that actually lies in
`K_G(r)` acts trivially on `X^r`.  The proof uses the Fadell-Neuwirth layer
extraction: any moving braid in `K_G` has a moving right-stabilized
point-pushing layer, and that layer remains in `K_G`.  Thus ordinary laws are
only a necessary filter; the B route must produce moving point-pushing layers
with genuine finite-longitude invisibility.  The same note records the
derivative-detector sufficient condition: laws on the finite Artin detector
permutation group `D_k(G)` force point-pushed membership in `K_G`, while the
exact condition is fixation of all endpoint-identity detector states.
`proofs/point_pushing_product_prefix_obstruction.md` now diagonalizes the
repaired criterion.  If finite-rack domination fails, then for each
product-prefix detector `P_j=G_1 x ... x G_j` there is a moving last-strand
point-pushing layer `lambda_j=iota_{r_j}(w_j)` which genuinely lies in
`K_{P_j}(r_j)`.  Right-stabilizing `lambda_j` by `j` unused strands gives a
normalized-law sequence eventually invisible to every finite group.  This
preserves the useful "point-pushing only" B format without relying on the
false ordinary-law implication.
`proofs/point_pushing_product_prefix_first_failure_stratification.md` makes
that product-prefix route canonical.  For
`eta_X(k)=min{j:D_k(P_j)->P_k(X)}`, fixed-arity cofinality and derivative
functoriality show that `eta_X(k)` is finite and weakly increasing, and that
boundedness of `eta_X(k)` is equivalent to finite-rack domination.  If it is
unbounded, the first failure for `P_j` occurs at arity `k_j->infinity` and,
by jump normalization, may be chosen as a one-new-strand Brunnian word in the
relative deletion kernel.  The helper
`point_pushing_product_prefix_first_failure_audit(...)` records finite
product-prefix first-failure rows.
`proofs/point_pushing_action_quotient_separation.md` sharpens what such a
tail must do inside the action images.  If a product-prefix relation is
trivial in `D_k(Pi_j)` but moves an element `g` of `P_k(X)`, then `g` cannot
be separated from the identity in any quotient of `P_k(X)` of order at most
`b(j)`, where `b(j)` is the largest order bound fully represented among the
first `j` finite groups.  Therefore a B tail must have unbounded
quotient-separation depth inside `P_k(X)`.  Conversely, a uniform bound on
the element-separating quotient sizes of all `P_k(X)` gives one product-prefix
detector and hence finite-rack domination.  The helper
`point_pushing_action_quotient_separation_audit(...)` records bounded
finite-prefix residual-depth diagnostics.
`proofs/point_pushing_monolithic_compression.md` compresses the same
obstruction to a critical quotient.  For any product-prefix relation trivial
in `D_k(Pi_j)` but nontrivial in `P_k(X)`, choose a smallest quotient of
`P_k(X)` that separates the moved element.  That quotient is monolithic, the
moved element lands in its unique minimal nontrivial normal subgroup, and the
quotient order is greater than `b(j)`.  Thus a genuine B tail must be an
unbounded sequence of Brunnian first-failure monolithic quotients.  The helper
`point_pushing_monolithic_compression_audit(...)` checks one finite row.
`proofs/point_pushing_chief_layer_tail_split.md` now splits those minimal
quotients by escape mechanism.  If the monolith `M` is nonabelian, then
`H` embeds in `Aut(M)`.  If `M` is abelian but not contained in `Phi(H)`, then
`H=M semidirect L` with `L<=Aut(M)`.  Thus bounded nonabelian and bounded
complemented abelian chief layers cannot escape product-prefix detectors; a
tail is either large-chief with `|M_j|->infinity` or abelian Frattini-depth
with `M_j<=Phi(H_j)`.
`proofs/point_pushing_monolith_type_split.md` records the forced finite-group
type split for those critical quotients: a finite monolith is
characteristically simple, so it is either elementary abelian `(C_p)^r` or a
product `S^r` of isomorphic nonabelian finite simple groups, with the ambient
quotient acting transitively on the simple factors in the second case.  Thus
the B tail has only two broad regimes: abelian affine-type monoliths or
nonabelian simple-product monoliths.  The monolithic compression helper now
records the finite row's `monolith_type`, prime, and element orders.
`proofs/point_pushing_marked_quotient_criterion.md` gives the exact finite
image formulation behind this repair.  For a fixed finite group `G`, let
`D_k(G)` be the marked Artin-derivative detector image generated by the
actions of `A_{i,k+1}` on `(G x G)^{k+1}`, and let `P_k(X)` be the marked
YBE point-pushing image.  Then `A_G` dominates `X` iff, for every `k`,
`P_k(X)` is a marked quotient of `D_k(G)` sending detector generator `d_i` to
YBE generator `h_i`.  The helper `point_pushing_marked_quotient_audit(...)`
checks finite arity instances by searching the paired subgroup for
`(1,nonidentity)` kernel movers.
`proofs/point_pushing_paired_graph_criterion.md` now records the exact paired
subgroup form of the same criterion.  Let
`M_k(G,X)=< (d_i,h_i) > <= D_k(G) x P_k(X)`.  The marked quotient
`D_k(G)->P_k(X)` exists iff the vertical kernel
`M_k(G,X) cap ({1} x P_k(X))` is trivial, equivalently iff `M_k(G,X)` is the
graph of the quotient homomorphism.  A nontrivial vertical element `(1,p)` is
precisely a word trivial in the derivative detector but moving `X`, hence a
genuine point-pushing `K_G` mover.  The audit helper now exposes this as
`vertical_kernel_trivial` when the subgroup enumeration is not truncated.
`proofs/point_pushing_vertical_witness_certificate.md` now spells out the
finite B-seed certificate extracted from such a vertical element.  A row must
give a word `w`, verify `w(d_i)=1`, verify that `w(h_i)` agrees with the
direct point-pushed braid action, and exhibit a moved tuple
`x -> rho_X(iota(w))(x)`.  The helper
`point_pushing_vertical_witness_certificate(...)` checks one such row and
reports `valid_vertical_witness`.  This remains a finite-row certificate only;
outcome B still requires an infinite product-prefix or symmetric-tail family.
`proofs/point_pushing_fixed_arity_cofinality.md` now proves that no fixed
point-pushing arity can supply a B obstruction.  For fixed `k`, the last
recursive longitude of `iota_{k+1}(w)` is `Theta_k(w)` for a triangular
Nielsen automorphism `Theta_k`.  Given any finite-index normal subgroup
`N normal F_k`, the finite quotient `G_N=F_k/Theta_k(N)` separates every
`w notin N` through the last longitude, so
`ker(F_k->D_k(G_N)) <= N`; after left-regular embedding,
`D_k(S_m)` maps onto the quotient as a marked group.  Hence every finite
arity prefix is detected by some symmetric group.  The remaining point-pushing
problem is exactly whether `mu_X(k)=min{m:D_k(S_m)->P_k(X)}` is bounded in
`k`.
`proofs/point_pushing_mu_boundedness_dichotomy.md` now packages this as an
exact A/B fork.  For a finite solution `X`, `X` is finite-rack dominated iff
`sup_k mu_X(k)<infinity`; if `mu_X` is unbounded, choose `k_j` with
`mu_X(k_j)>j`, use the paired graph criterion to obtain a vertical witness
word for `D_{k_j}(S_j)->P_{k_j}(X)`, and right-stabilize to get the
normalized-law obstruction sequence.  The helper
`point_pushing_mu_prefix_audit(...)` checks bounded rectangles in `(k,m)` and
records first detected symmetric degrees or first vertical witnesses, but it
is only finite diagnostic evidence.
`proofs/point_pushing_mu_functoriality.md` records structural rules for the
same growth invariant: surjective YBE quotients and domination can only lower
`mu`, while finite products satisfy
`mu_{X x Y}(k)=max(mu_X(k),mu_Y(k))`.  Hence unbounded `mu` cannot be created
by quotient shadows or finite products of bounded factors; a B seed must live
in a primitive component with genuinely unbounded detector degree.
`proofs/point_pushing_suffix_shuttle_normal_form.md` now records the exact
finite-state form of the point-pushing generators: `A_{i,n}` acts as a left
suffix scan using `R`, then a local `sigma_i^2`, then a right inverse scan
using `R^{-1}`.  The helpers `point_pushing_suffix_shuttle_action(...)` and
`point_pushing_suffix_shuttle_audit(...)` check this convention on finite
tuples.  Thus any unbounded `mu` obstruction must arise from the group
generated by one fixed reversible two-pass suffix-shuttle transducer family.
`proofs/point_pushing_recursive_conjugacy.md` strengthens this by showing that
all point-pushing generators are suffix shifts of one recursively defined
family: if `a_n=rho_X(A_{1,n})`, then
`a_n=s_{n-1}(a_{n-1} x id)s_{n-1}^{-1}` and
`rho_X(A_{i,n})=id^{i-1} x a_{n-i+1}`.  The helper
`point_pushing_recursive_conjugacy_audit(...)` checks the convention in finite
degree.  Thus the unbounded-`mu` target is now the suffix-shift group of a
single recursive finite-state family.
`proofs/point_pushing_jump_normalization.md` sharpens the unbounded-`mu`
target again.  In right-based coordinates, if `S_m` detects arity `k` but
fails at arity `k+1`, the failure can be replaced by a word in the relative
kernel `ker(F_{k+1}->F_k)` that kills the newly added far-left stationary
strand.  Thus any B tail can be chosen as one-new-strand Brunnian
point-pushing movers, and the A-side extension target is exactly
`R_{m,k+1} cap ker(r_k) <= N_{X,k+1}` for one fixed `m`.  The helper
`point_pushing_brunnian_witness_certificate(...)` checks supplied right-based
candidate words by conversion to the existing left-based derivative detector,
deletion of the new strand, and vertical-kernel action verification.
`proofs/point_pushing_brunnian_orbit_criterion.md` then makes that extension
target finite and exact at each arity: the Brunnian obstruction subgroup is
the normal closure of the new-generator pair under the old suffix paired
subgroup.  A one-new-strand jump exists exactly when this finite
orbit-normal-closure subgroup contains a nontrivial vertical element.  The
helper `point_pushing_brunnian_orbit_audit(...)` enumerates that subgroup in
finite rows and returns a right-based Brunnian witness when one appears.
`proofs/point_pushing_brunnian_relation_lift.md` splits this finite subgroup
criterion into the exact relation package for a positive proof: the
transported action label on the detector conjugacy orbit of the new generator
must be well-defined, and every relation among detector orbit generators must
lift to the transported action labels.  The same audit helper now records
`detector_orbit_size`, `action_orbit_size`, and
`orbit_map_well_defined`, so finite B seeds can be classified as either orbit
ambiguities or later relation-lift failures.
`proofs/point_pushing_brunnian_stabilizer_gate.md` identifies the first of
these two failures with a stabilizer-centralizer inclusion:
`q(Stab(d)) <= Cent(h)`.  When this fails, the commutator
`u a_{k+1} u^{-1} a_{k+1}^{-1}` is already a right-based Brunnian vertical
witness.  The orbit audit now records `detector_stabilizer_size` and
`stabilizer_centralizes_new_action`, isolating the remaining relation-lift
burden to relations among well-defined detector-orbit labels.
`proofs/point_pushing_brunnian_orbit_quotient_certificate.md` packages that
remaining burden as a finite graph criterion: after the stabilizer gate, the
paired orbit subgroup `B` must project injectively to its detector projection
`B_D`, equivalently `|B|=|B_D|`.  The audit exposes this by recording
`failure_kind`, `relative_subgroup_size`, `relative_detector_projection_size`,
and `relative_action_projection_size`.  Thus every finite Brunnian row is now
classified as `stabilizer`, `orbit_label`, `orbit_relation`, `none`, or a
truncation diagnostic.
`proofs/point_pushing_brunnian_gate_induction.md` assembles these finite gates
back into the exact all-arity criterion: for fixed `G`, the rack `A_G`
dominates `X` iff arity `1` satisfies the marked quotient criterion and every
successive Brunnian extension row has `failure_kind="none"`.  The helper
`point_pushing_brunnian_gate_prefix_audit(...)` checks finite prefixes
sequentially and stops at the first base or extension failure.  Its prefix
result now explicitly reports that it does not prove the all-arity marked
quotient tower: a passing finite prefix leaves
`remaining_all_arity_obligation="symbolic_all_arity_argument"`.
`proofs/point_pushing_base_arity_gate.md` closes the base gate explicitly.
At arity `1`, the point-pushing image is generated by `A_{1,2}=sigma_1^2`;
if `s_X=ord(rho_X(A_{1,2}))`, then any group whose exponent is divisible by
`s_X` detects the base gate.  The helper
`point_pushing_base_arity_certificate(...)` records the sharper symmetric
cutoff `b_X=min{m: s_X divides lcm(1,...,m)}`.  Thus
asymptotic B tails cannot consist of base failures.
`proofs/point_pushing_base_free_brunnian_tail.md` folds that cutoff into the
tail fork.  After symmetric degree `j>=b_X`, every symbolic first failure must
be one of the non-base Brunnian kinds (`stabilizer`, `orbit_label`, or
`orbit_relation`).  The helper
`point_pushing_base_free_brunnian_tail_prefix(...)` skips degrees below the
cutoff and reports only the base-free finite prefix.
`proofs/point_pushing_base_free_thresholds.md` packages the same reduction as
a growth invariant `epsilon_X(K)`: the least `m>=b_X` whose `S_m` detector
passes all Brunnian extension rows up to arity `K`.  Boundedness of this
sequence is equivalent to the positive symmetric-detector route, while
unboundedness is exactly the certified base-free non-base tail route.  The
helper `point_pushing_base_free_threshold_audit(...)` records finite
approximations to these thresholds.
`proofs/point_pushing_base_free_threshold_sequence.md` records finite prefixes
of the threshold sequence.  The sequence is weakly increasing in `K`, and
`point_pushing_base_free_threshold_prefix_audit(...)` records the detected and
unresolved arities inside a bounded rectangle.  These tables remain
diagnostic: the theorem target is still all-`K` boundedness, not a finite
prefix.
`proofs/point_pushing_brunnian_first_failure_stratification.md` sharpens the
negative route: if no fixed symmetric detector works, first failing arities
tend to infinity, base failures occur only below a finite cutoff, and an
infinite subsequence has one stable non-base failure kind (`stabilizer`,
`orbit_label`, or `orbit_relation`).  The helper
`point_pushing_brunnian_tail_prefix_audit(...)` records finite symmetric-degree
prefixes of this first-failure tail.
`proofs/point_pushing_brunnian_failure_certificate.md` turns one non-base row
of that tail into a braid-action certificate: a right-based Brunnian word,
identity in the derivative detector, and an explicit moved tuple of `X`.  The
helper `point_pushing_brunnian_failure_certificate(...)` wraps the orbit audit
and rechecks the returned witness with
`point_pushing_brunnian_witness_certificate(...)`.  This does not build the
infinite tail required for outcome B, but it makes each finite non-base row
self-certifying.
`proofs/point_pushing_brunnian_tail_certificate_prefix.md` packages finite
symmetric first-failure prefixes around those row certificates.  The helper
`point_pushing_brunnian_tail_certificate_prefix(...)` separates detected
degrees, base/truncated finite failures, and certified non-base rows.  It is
still finite-prefix infrastructure: a B proof needs an infinite family of
certified rows, and an A proof needs a uniform reason no such family exists.
`proofs/point_pushing_brunnian_normalized_prefix_bridge.md` connects each
certified non-base row to the existing symmetric normalized-law prefix audit:
after right-stabilizing by `j` strands, a valid `S_j` Brunnian row remains in
`K_{S_j}` and keeps its moved tuple.  The helper
`point_pushing_brunnian_normalized_prefix_audit(...)` performs that row-level
bridge, so an infinite family of certified rows would immediately have the
standard normalized-law certificate format.
`proofs/point_pushing_derivative_functoriality.md` records the compatibility
of this exact criterion with detector changes.  A finite group homomorphism
`G->H` induces coordinate equivariance on detector states.  Surjections give
marked quotients `D_k(G)->D_k(H)`, embeddings give restriction quotients
`D_k(H)->D_k(G)`, symmetric groups are cofinal by the left-regular embedding,
and direct products give the marked subdirect product generated by the
coordinatewise detector generators.  The helper
`point_pushing_derivative_functoriality_audit(...)` checks finite instances of
the equivariance identity.
`proofs/symmetric_derivative_quotient_fork.md` packages the corrected global
fork.  A finite solution `X` is finitely rack-dominated iff some symmetric
group `S_m` supplies marked quotients `D_k(S_m)->P_k(X)` for every `k`.  If no
such `m` exists, then for every `j` there is a derivative relation in
`D_{k_j}(S_j)` which fails in `P_{k_j}(X)`; the corresponding point-pushing
braid lies in `K_{S_j}`, and right stabilization gives the normalized-law
obstruction sequence.  This is the exact replacement for the false ordinary
`S_j`-law point-pushing route.
`proofs/symmetric_repair_contract_bridge.md` now connects this symmetric fork
back to the proof-critic repair contract.  If a supplied repair package proves
the local implication using a fixed product detector `H(pi,Q)`, then the left
regular embedding gives the same implication for `S_m` with
`m>=|H(pi,Q)|`.  The helper
`symmetric_repair_contract_bridge_audit(...)` records the degree, the
left-regular embedding condition, and the corresponding sharp detector rack
size.  This is only a detector-format bridge: it does not construct the
missing descent readout, faithful decomposition, or all-`n` endpoint
witnesses.
`proofs/endpoint_family_symmetric_fork.md` now gives the matching endpoint
family fork.  For any finite family of fixed endpoint groups `H_s`, all-`n`
endpoint-longitude witnesses give one common symmetric cutoff
`S_m`, while failure of every such cutoff gives a symmetric-tail endpoint seed
which becomes normalized-law movement once the endpoint family is faithful.
This keeps the positive and negative endpoint requirements in the same
symmetric-detector language.  The helper
`endpoint_family_symmetric_fork_audit(...)` records the finite factor orders,
the cutoff degree, witness and faithfulness flags, and finite tail-prefix
degrees for supplied endpoint-family rows.  The helper
`endpoint_family_symmetric_seed_audit(...)` additionally attaches one
nonidentity endpoint channel to a local symmetric normalized-law prefix row,
requiring the same symmetric degree, right stabilization by that degree,
endpoint-family faithfulness, and an explicit same-motion assertion.
The triangular recovery endpoint layer now has the keyed specialization
`triangular_recovery_symmetric_endpoint_fork_audit(...)`: it accepts only the
single fixed group `U_tri`, requires exact coverage of the routed System U
endpoint keys, and lets the post-linear classifier close U by a symmetric
cutoff without hiding any still-unclosed continuation or mixed-unit endpoint
families.
The same post-linear classifier now keeps the K-stage local-minimality
contradiction separate from endpoint routing: if the triangular-Latin defect
closure supplies a proper generated congruence row, it reports
`closed_by_triangular_latin_proper_closure` and creates no U/C/M endpoint
obligation from that row.  Only universal closure rows may feed a routed
endpoint family.  The same terminal treatment now applies to proper
generated closures in the partial-constant no-triangular ledger, reported as
`closed_by_missing_triangular_partial_constant_proper_closure`.
Partial-constant continuation routing is now also universal-gated: a
nonuniversal partial-constant closure row, a closure-kind mismatch, or a
nonuniversal continuation seed closure no longer creates a System C endpoint
obligation.
The universal-continuation lost-edge ledger is now exact and non-vacuous: it
must match the seed-saturation lost edges, partition them into routed and
unrouted tuples, distinguish exactly the routed tuple with the supplied
routing labels, and contain at least one lost edge when universal collapse is
forced.  Consequently a System C endpoint witness or symmetric cutoff cannot
close a live continuation route with an empty edge certificate.
The same supplied-certificate pattern now covers the routed continuation and
mixed-unit endpoint families.  The helper
`universal_continuation_identity_symmetric_endpoint_fork_audit(...)` attaches
a faithful symmetric cutoff to exactly the identity-routed System C lost
edges, while `mixed_unit_context_symmetric_endpoint_fork_audit(...)` attaches
one to exactly the System M mixed-context keys.  In a routed endpoint product,
each fork removes only its own family from `unclosed_routed_endpoint_systems`.
Coordinate-unit routing is now side-exact as well: the listed
coordinate-unit side must carry the coordinate-unit profile explanation and
must actually be unit in the supplied section data before it can remove a K
row or create a System M obligation.  The coordinate-unit routing ledger is
also non-vacuous; an empty row tuple does not prove the route.
The living handoff prompt
`proofs/gpt55_pro_remaining_issues_prompt.md` records the current K/U/C/M
remaining obligations as a model-independent, attachment-free prompt for a
future proof pass.
`proofs/symmetric_tower_counterexample_certificate.md` now records the
corresponding simplified B certificate: for every `j`, produce a braid
`alpha_j` with identity `S_j` longitude data and a moved global or residual
tuple, then right-stabilize.  The helpers
`symmetric_normalized_law_prefix_witness_audit(...)` and
`local_symmetric_normalized_law_prefix_witness_audit(...)` check one supplied
global or local row of this symmetric-tower certificate.
`proofs/normalized_law_counterexample_certificate.md` now records the
constructive B data format: for every product prefix
`P_j=G_1 x ... x G_j`, give an explicit braid `alpha_j`, moved tuple, and
identity `P_j` longitude signature, then right-stabilize.  The helper
`normalized_law_prefix_witness_audit(...)` checks one supplied prefix record,
including product invisibility, factor projection invisibility, stabilization,
and movement before and after stabilization.  It is a certificate-shape check,
not an all-`j` proof.
`proofs/unit_perfect_residual_normalized_seed.md` now connects the last
nonsolvable terminal-unit checkpoint to that local B certificate format.  The
helper `unit_perfect_residual_normalized_seed_audit(...)` pairs one
`local_normalized_law_prefix_witness_audit(...)` row with one
`unit_perfect_residual_longitude_audit(...)` finite miss, and it requires
explicit same-braid and same-readout assertions before marking the row as a
perfect-residual normalized seed.  This is still only one row of a possible
B construction; an all-`j` family is still required.
`proofs/unit_perfect_residual_symmetric_seed.md` gives the symmetric-tower
version of the same seed.  If the row is invisible to `S_j` and
`j >= |P|` for the fixed perfect residual `P`, then left-regular embedding and
the symmetric tower imply invisibility in `P`.  The helper
`unit_perfect_residual_symmetric_seed_audit(...)` checks the declared
`S_j` row, `j`-strand stabilization, the `j >= |P|` guardrail, and the same
perfect-residual miss/readout attachment.  This removes finite-group
enumeration from nonsolvable terminal-unit B attempts but still does not
construct the required all-`j` sequence.
The same note now records a tail-prefix check:
`unit_perfect_residual_symmetric_tower_prefix_audit(...)` requires a supplied
finite prefix of rows to start at degree `|P|`, continue without gaps, and pass
the one-row symmetric seed audit at every degree.  This is only the finite
shadow of the required infinite tail construction.
`proofs/unit_perfect_residual_symmetric_dichotomy.md` now states the matching
all-`n` fork for one faithful terminal perfect-residual readout channel: either
some fixed `S_m` with `m>=|P|` kills that channel uniformly, or every
`j>=|P|` supplies a symmetric-tail seed.  This is still channel-local; A needs
all channels and faithful decomposition, while B needs an explicit interval and
all-tail moved rows.
`proofs/unit_perfect_residual_finite_channel_fork.md` now assembles the finite
family of terminal perfect-residual channels: either one symmetric degree
`S_M` kills all channels simultaneously, or the family supplies an unbounded
symmetric-tail normalized-law seed.  Since there are only finitely many
channels, there is no additional global obstruction inside the nonsolvable
terminal-unit family.

`proofs/point_pushing_abelian_monolith_split.md` now sharpens the latest
product-prefix monolithic obstruction.  Once a first-failure row is compressed
to a smallest monolithic quotient `H` with elementary-abelian monolith `M`, the
commutator subgroup `[H,M]` is forced by minimality to be either `1` or `M`.
Thus the abelian tail is no longer a single vague case: it is either a central
monolithic depth obstruction, where the moved element lies in `Z(H)` and is not
seen by conjugation-linear data, or a noncentral irreducible `F_p` module
obstruction, where `H/C_H(M)` acts faithfully and irreducibly on `M` and the
moved monolith value is generated by conjugation differences.  The finite
audit helper now records centralizer order, conjugation-action quotient order,
commutator order, and whether the monolith is central.
`proofs/point_pushing_central_monolith_depth.md` then splits the central
elementary-abelian branch again.  If the monolith is not contained in
`[H,H]`, abelianization separates the moved monolith value, so the
smallest-quotient choice forces `H` itself to be abelian; a finite abelian
monolithic group is cyclic of prime-power order.  Otherwise the monolith lies
inside `Z(H) cap [H,H]`, a genuine stem central-extension obstruction.  The
audit helper now records derived-subgroup order, whether the monolith and
projected value lie in the derived subgroup, and a central-depth regime label.
`proofs/point_pushing_cyclic_p_power_tail.md` refines the cyclic side.  A
cyclic `C_{p^e}` first failure has `p^e>b(j)`.  Hence either `p>b(j)`, a prime
escape, or `p<=b(j)<p^e`, a genuine p-power depth escape.  Proper quotients of
`C_{p^e}` kill the bottom order-`p` monolith element, so the latter case is not
detected merely because `C_p` lies in the product prefix.  The audit helper now
records the cyclic prime, p-power exponent, and prefix escape regime.
`proofs/point_pushing_noncentral_module_tail.md` now performs the matching
split on the noncentral elementary-abelian side.  For monolith
`M ~= F_p^r`, the compressed quotient satisfies
`|H|=p^r |H/C_H(M)| |C_H(M)/M|`.  Hence an infinite noncentral tail has a
subsequence with module prime escape, fixed-prime module-dimension escape, or
bounded-module centralizer-layer escape.  The audit helper now records the
module dimension, centralizer-layer size, whether the size factorization
matches the quotient, and a finite row parameter regime.
`proofs/point_pushing_nonabelian_monolith_tail.md` now closes the structural
bookkeeping for the nonabelian monolith branch.  If `M=S^r` is the nonabelian
monolith, then `C_H(M)=1`; hence the compressed quotient embeds into
`Aut(M) ~= Aut(S) wr Sym(r)`.  An infinite nonabelian tail therefore has a
subsequence with unbounded simple factor size or fixed simple factor and
unbounded multiplicity.  The finite audit helper records centralizer
triviality, the quotient-over-monolith order, and a row prefix regime.
`proofs/point_pushing_cyclic_tail_closure.md` now eliminates the cyclic branch
entirely.  Every point-pushing generator `A_{i,k+1}` is braid-conjugate to
`sigma_i^2`, so its action order divides the fixed integer
`B_X=ord(rho_{X,2}(sigma_1^2))`.  Therefore every cyclic quotient of every
`P_k(X)` has order dividing `B_X`, and a product-prefix cyclic failure
`p^e>b(j)` is impossible once `b(j)>=B_X`.  The helper
`point_pushing_cyclic_tail_bound_audit(...)` records this bound and finite
prefix convention checks.
`proofs/point_pushing_bounded_normal_generator_tail.md` now adds the
first-failure normal-generator constraint.  In any Brunnian first-failure
monolithic quotient, if `t` is the image of the newest point-pushing generator,
then `ord(t)` divides the same fixed integer `B_X`, and the critical monolith
`M` lies in `<<t>>`.  Thus every remaining monolithic tail must be built from
one transported endpoint generator of bounded order, not from an arbitrary
large quotient of the action image.  The helper
`point_pushing_bounded_normal_generator_audit(...)` records the convention
guardrail for this bound.
`proofs/point_pushing_abelian_chief_relation_module.md` now linearizes the
abelian-chief side of the Brunnian fork.  For the detector orbit generators
`o_c=c d c^{-1}`, let `R` be the relation subgroup of their detector orbit
group `N_D`.  In any minimal abelian-chief first failure, the vertical relation
image `R -> M` lands in the unique elementary-abelian monolith and induces a
nonzero, hence surjective, `F_p[N_D]`-module quotient
`R/[R,R] tensor F_p -> M`.  Thus the abelian B-side is now a relation-module
tail, while the other side is a nonabelian simple-power relation-lift tail.
The helper `point_pushing_abelian_chief_relation_module_audit(...)` records
finite chief-layer bookkeeping.
`proofs/point_pushing_abelian_relation_action_split.md` now splits that
abelian chief layer by action type.  If the `N_D` action is trivial, the
unique minimal normal condition forces `M ~= F_p`, and the relation quotient
factors through the coinvariants `(Rel_D tensor F_p)_{N_D}`.  If the action is
nontrivial, then `M` is a nontrivial irreducible module and `[N_D,M]=M`.  The
helper `point_pushing_abelian_relation_action_split_audit(...)` records the
finite row regimes `central_trivial_coinvariant` and
`noncentral_irreducible_module`.
`proofs/point_pushing_central_stem_relation_tail.md` now identifies the
central trivial branch as a stem central-extension tail.  After cyclic closure,
a central first-failure monolith must satisfy `F_p<=Z(H) cap [H,H]`; with
`Q=H/F_p`, it is a nonzero `p`-quotient of the Schur multiplier of a finite
detector-orbit quotient `Q` and the actual relation lift factors through the
coinvariants `R/[F_C,R] tensor F_p`.  The helper
`point_pushing_central_stem_relation_audit(...)` records the finite row shape.
`proofs/point_pushing_module_prime_characteristic_split.md` now sharpens the
noncentral module prime branch.  Since the newest point-pushing normal
generator has order dividing the fixed integer `B_X`, only finitely many
module primes can divide `B_X`; hence every true `p_j->infinity` module-prime
tail is eventually cross-characteristic.  The helper
`point_pushing_module_prime_characteristic_audit(...)` records the finite
same/cross-characteristic label.
`proofs/point_pushing_active_module_generator_split.md` now splits the
noncentral module branch by the image of that bounded generator in the action
shadow `H/C_H(M)`.  If the image is trivial, the row is a centralizer-layer
generator tail.  If it is nontrivial, a bounded-order linear operator has
conjugate commutator images whose sum is the irreducible module `M`; in a
prime-escape tail this is cross-characteristic.  The helper
`point_pushing_active_module_generator_audit(...)` records the finite row
label.
`proofs/point_pushing_centralizer_layer_commutator_split.md` now sharpens the
centralizer-layer generator tail.  If `N=<<t>>_H` lies in `C_H(M)` and
contains `M`, then minimality leaves only two forms: `[N,N]=1`, an abelian
centralizer layer, or `M<=Z(N) cap [N,N]`, a centralizer stem layer.  The
helper `point_pushing_centralizer_layer_commutator_audit(...)` records the
finite row labels `abelian_centralizer_layer` and `centralizer_stem_layer`.
`proofs/point_pushing_abelian_centralizer_layer_prime_bound.md` now removes
prime escape from the abelian centralizer-layer form.  In that case
`N=<<t>>_H` is a finite abelian `p`-group and `exp(N)|ord(t)|B_X`, so the
prime is one of the finitely many divisors of `B_X` and the layer exponent is
bounded.  The helper
`point_pushing_abelian_centralizer_layer_prime_audit(...)` records finite
prime-support and exponent labels.
`proofs/point_pushing_centralizer_stem_multiplier_tail.md` now identifies the
stem side of the same centralizer-layer split.  If `M<=Z(N) cap [N,N]` for
`N=<<t>>_H`, then `1->M->N->N/M->1` is a stem central extension, so `M` is a
Schur-multiplier quotient of `N/M`; the quotient is ambient-normally generated
by the bounded-order image of `t`.  The helper
`point_pushing_centralizer_stem_multiplier_audit(...)` records finite quotient
and generator-image data.
`proofs/point_pushing_centralizer_stem_noncyclic_quotient.md` now removes the
cyclic quotient subcase of that stem branch.  If `N/M` were cyclic, then the
centrality of `M` in `N` would force `N` abelian, contradicting
`M<=[N,N]`.  The helper records `quotient_is_cyclic` and only accepts
noncyclic stem quotient rows.
`proofs/point_pushing_centralizer_stem_transport_split.md` now splits those
noncyclic stem quotient rows by generation mechanism.  Either the bounded
generator image internally normally generates `Q=N/M`, or its internal normal
closure is proper and the quotient is generated only by the ambient
transported orbit of that closure.  The helper records the internal normal
closure order and the regime label.
`proofs/point_pushing_internal_stem_abelianization_bound.md` now sharpens the
internal-generation side: if the bounded generator image internally normally
generates `Q`, then `Q_ab` is cyclic, generated by that image, and has order
and exponent dividing `B_X`.  The helper records quotient abelianization
orders and whether the generator image generates the abelianization.
`proofs/point_pushing_transport_residual_quotient_split.md` now sharpens the
transport-orbit side by forming `E=Q/<<q>>_Q`.  If `E_ab` is nontrivial, the
missing transport generation is abelian-visible; otherwise `E` is a perfect
transport residual.  The helper records the residual quotient and
abelianization orders.
`proofs/point_pushing_transport_residual_abelianization_bound.md` now bounds
the abelian-visible side of that split.  Since `E_ab` is generated by ambient
transported images of the bounded-order generator image `q`, its exponent
divides `B_X` and its prime support is contained in the fixed set of primes
dividing `B_X`.  The helper records the residual abelianization exponent,
prime set, and bounded-support flags.
`proofs/point_pushing_nonabelian_chief_relation_quotient.md` now gives the
parallel nonabelian-chief compression.  If `R` is the same detector orbit
relation group and the chief layer is `M=S^r`, then the minimal vertical
failure has `mu_H(R)=M`.  The conjugation action of the detector orbit on `M`
is well defined in `Out(M)`, because two lifts of the same detector element
differ by an element of `M`.  Thus the nonabelian B-side is a simple-power
relation-group quotient tail.  The helper
`point_pushing_nonabelian_chief_relation_quotient_audit(...)` records the
finite chief-layer bookkeeping.
`proofs/point_pushing_nonabelian_wreath_coordinate_lift.md` now puts that
nonabelian branch in coordinate normal form.  In a minimal quotient,
`C_H(S^r)=1`, so `H` embeds in `Aut(S) wr Omega` for a transitive factor
action `Omega`; the row succeeds modulo `S^r`, and failure is exactly a
detector-orbit relation whose lift has a nontrivial `S`-coordinate.  The
helper `point_pushing_nonabelian_wreath_coordinate_audit(...)` records the
finite row shape.
The U/C/M endpoint-observer product residual gate has been tightened again.
For a multi-family product endpoint row, the product residual-faithfulness
theorem must now match the per-family residual theorem not only on active
families and routed seed states, but also on the exact endpoint-channel
reason ledger by family.  A product theorem that proves residual faithfulness
for placeholder channel names, while the observers actually kill different
U/C/M channels, is rejected with
`endpoint_observer_product_residual_faithfulness_channel_scope_mismatch`.
This has been sharpened one step further: the product theorem must also match
the full well-formed endpoint-channel key ledger by family, including any
optional local channel data after the channel name.  A product theorem that
keeps the same reason string but changes the concrete local channel key is
rejected with
`endpoint_observer_product_residual_faithfulness_channel_key_scope_mismatch`.
The retained family-observer build gate has also been made non-opaque.  A
proving `UniversalKEndpointObserverBuild` can no longer close with stale
top-level auxiliary rows: the advertised word-potential certificate,
detector-track initialization rows, endpoint-target audit, C/M cutoff-readout
audit, and residual-faithfulness theorem rows must match the actual objects
inside the retained build.  Mismatches are exposed through the
`endpoint_observer_family_*_rows_match_builds` diagnostics and keep the family
observer open.
The same anti-staleness rule now applies to the raw monodromy front door when
it is attached to a retained family build.  The raw endpoint group, templates,
positive monodromy state rows, restricted detector-domain assignments, and
soundness-witness maps must match the retained build internals; an internally
exact monodromy input package for a different observer is rejected with
`endpoint_observer_monodromy_input_rows_do_not_match_builds`.
This anti-staleness gate now also covers the raw monodromy package's
seed-classifier ledger.  The attached raw package must use the current
`K_nabla`/`kappa` entries, not merely the same routed endpoint seed states; a
stale descriptor ledger is rejected with
`endpoint_observer_monodromy_input_seed_classifier_scope_mismatch`.  The
family observer layer also rejects duplicate classifier entries, duplicate row
descriptors, and conflicting descriptor targets before using the ledger as
active endpoint seed evidence.
The raw monodromy input audit now rejects the same duplicate and conflicting
seed-classifier ledgers before declaring `input_rows_exact`, so an ambiguous
front-door package cannot appear internally exact while the family wrapper is
the only layer that notices the classifier defect.
The direct signed-endpoint proof gate has also been tightened to require an
explicit finite monodromy representation audit.  A signed table with manually
asserted state/coordinate braid booleans but no attached representation audit
now fails with `explicit_endpoint_monodromy_representation_missing`; the
factory path still derives the representation audit automatically from the
current interval, reachable seed states, and signed rows.  This prevents the
old signed-table path from bypassing the reduced monodromy-coboundary
observer certificate.
The constructed endpoint-observer build now also checks internal ledger
identity.  A proving `UniversalKEndpointObserverBuild` requires its advertised
positive rows to be exactly the positive subset of its signed rows, its stored
monodromy presentation to be the one used by the monodromy representation
audit, its reachable-state and row ledgers to match both the monodromy audit
and the signed endpoint audit, and its telescoping detector audit to match the
signed audit.  A stale but separately valid monodromy representation can no
longer be spliced into an otherwise complete observer build; the wrapper now
exposes per-family internal reasons through
`endpoint_observer_family_build_internal_failure_reasons`.
The word-potential detector-domain gate has also been made non-tautological.
Restricted detector-domain assignments with allow-listed witness names are no
longer decisive.  If a certificate supplies an explicit detector-domain
assignment ledger for a positive row, that ledger must enumerate the full
finite variable domain for the row's coboundary-defect support; otherwise the
certificate fails with `detector_domain_subset_not_full_finite_domain`.
Proper restricted subsets remain diagnostic row data only until a stronger
machine-checkable all-`n` soundness certificate is implemented.
The automatic residual-faithfulness helpers now preserve malformed and
duplicate routed seed-state ledgers as theorem data instead of deduplicating
or crashing before audit construction.  A strict-identity, singleton-fibre,
coordinate-identity, or fibre-label residual helper can use only well-formed
seed states to emit schematic rows, but duplicate seed-state entries still
trigger `residual_faithfulness_duplicate_seed_states`, and non-sequence or
otherwise malformed ledgers trigger
`residual_faithfulness_malformed_seed_states`; either case keeps the observer
open.
The positive local-context monodromy presentation constructor now has the
same anti-normalization guard for endpoint-family ledgers.  It preserves a
non-sequence family ledger or duplicate family entries for the presentation
audit while deriving context rows only from valid unique families, so duplicate
families and malformed family scope remain explicit monodromy-presentation
failures.
The direct signed endpoint audit, raw monodromy input audit, and family
observer audit now normalize malformed top-level `kappa` ledgers through the
common row-input gate.  Non-sequence seed-classifier input is retained as
malformed seed-classifier data instead of crashing or being interpreted as an
empty active endpoint seed set.
The direct signed endpoint audit and monodromy representation audit now apply
the same guard to reachable endpoint-state ledgers.  Non-sequence reachable
ledgers and unhashable reachable seed states remain malformed reachable-state
data instead of crashing required-entry, YBE, or far-commutativity derivation.
The direct signed endpoint audit now applies the same policy to the signed
row ledger itself.  It filters valid signed endpoint generator rows into the
finite checker pipeline and retains `None`, non-row placeholders, or other
malformed entries as `malformed_signed_generator_rows`, so a malformed row
ledger cannot masquerade as an empty or partial proof.
The standalone monodromy representation audit now uses the same row filter:
valid signed rows define the endpoint-state permutations, while malformed
entries are retained as `endpoint_monodromy_representation_malformed_rows`.
It also has an explicit far-relation regression: if two disjoint positive
local-context permutations fail to commute on the exact reachable seed states,
the representation audit reports `monodromy_far_relation_mismatch` even when
each individual context map is a valid permutation.  This protects the
full-braid coherence gate at the finite monodromy layer, alongside the
adjacent YBE relation check.
The positive monodromy-coboundary route has also been audited for internal
viability.  With the current full-domain checker and templates that contain
only current longitude variables, every constant coboundary defect is forced
to be the identity because the all-identity `U`/`A` assignment lies in the
full domain.  A regression test now records that derived full-domain
no-constant emissions are either nonconstant failures or identity labels, and
that a forged nonidentity label fails the word-potential identity.  Thus
nontrivial endpoint observers require a fixed-carrier lift, an all-`n`
restricted reachable-domain soundness theorem, or a structural proof that the
remaining U/C/M endpoint systems are residual-trivial.
The repaired fixed-carrier target is now explicit: each positive row key must
carry a finite sound carrier domain for the initialized detector-track pairs,
and the word-potential defect must be constant over the full longitude
variable domain and that carrier domain.  A constant carrier track gives a
singleton sound domain and can produce nonidentity emissions; the test suite
records the abelian `C2` normal form where `W_s=U_1U_0^{-1}`,
`W_{s'}=U_0U_1^{-1}`, and a fixed carrier emits the nonidentity element.
The carrier-domain soundness condition is now reduced to a finite local
strand-carrier audit.  Carrier maps `ell_c:A_c->L_E` must satisfy the swapped
row equations `ell_c(u)=ell_b(y)` and `ell_d(v)=ell_a(x)` for every local row.
The new audit distinguishes this from coordinate-label identity, exports a
residual-faithfulness helper when the carrier maps are fibrewise injective,
and can be consumed by the identity/monodromy observer helper selectors.
The fixed-carrier coboundary route is now implemented as concrete finite
certificate infrastructure rather than just a hand calculation.  The new
`UniversalKFixedCarrierWordPotentialCertificate` and
`UniversalKFixedCarrierCoboundaryRow` check positive row keys with a finite
carrier-domain ledger, recognized carrier-soundness witnesses, templates that
use only current longitude variables, and constant coboundary defects over all
longitude-variable assignments while carrier values remain fixed.  The helper
`universal_k_fixed_carrier_word_potential_certificate_from_monodromy(...)`
derives endpoint emissions from positive monodromy rows, and
`universal_k_endpoint_observer_positive_rows_from_fixed_carrier_word_potential(...)`
turns those constants into positive endpoint rows.  Regression tests now show
that the `C2` fixed-carrier normal form emits a nonidentity element, that
forged endpoint values fail, and that empty, malformed, or unwitnessed carrier
domains are rejected.
The endpoint-observer builder and family observer audit now accept this
fixed-carrier certificate class alongside the original raw-variable
word-potential certificate.  A nonidentity `C2` fixed-carrier certificate can
therefore generate positive rows, derive inverse signed rows, pass the
telescoping detector audit, and close a family observer when the endpoint
target and residual-faithfulness theorem are supplied.  This is an integration
step only: it does not construct the required U/C/M observers for arbitrary
surviving intervals.  The top-level
`post_linear_remaining_finite_system_audit(...)` can also consume a
fixed-carrier certificate through its existing word-potential certificate
parameters, so a proposed fixed-carrier observer now reaches the same
post-linear audit surface as the raw-variable certificate path.
The family monodromy constructor now has a fixed-carrier companion,
`universal_k_endpoint_observer_builds_from_fixed_carrier_monodromy_by_family(...)`,
which derives fixed-carrier certificates directly from endpoint groups,
word-potential templates, positive state rows, carrier-domain ledgers, and
carrier-soundness witness ledgers.  The top-level post-linear audit exposes
matching `universal_k_monodromy_fixed_carrier_domains_by_family` and
`universal_k_monodromy_fixed_carrier_soundness_witnesses_by_family`
parameters; when these are present, the monodromy path derives fixed-carrier
certificates instead of raw-variable certificates.
The strand-carrier local invariant is now connected to this constructor.  The
helper
`universal_k_fixed_carrier_domain_ledger_from_strand_carriers(...)` derives
the exact singleton fixed-carrier domains and the `strand_carrier_equations`
witness ledger from a sound finite `ell_c(x)` table.  The family constructor
and top-level audit can consume `universal_k_monodromy_strand_carrier_rows_by_family`
and optional `universal_k_monodromy_strand_carrier_track_counts_by_family`
inputs, so a proposed observer no longer has to hand-materialize the
per-positive-row carrier-domain table when the strand-carrier equations prove
it.
The strand-carrier ledger itself can now be derived canonically from the
interval.  The helper `universal_k_canonical_strand_carrier_rows(...)` builds
the least finite component relation generated by the swapped row equations
`ell_c(u)=ell_b(y)` and `ell_d(v)=ell_a(x)`.  When that canonical quotient is
fibrewise injective, `universal_k_canonical_strand_carrier_residual_faithfulness_audit(...)`
closes the residual action symbolically, and the automatic residual selector
tries this canonical strand-carrier theorem before falling back to the
canonical coordinate-label theorem.  The top-level post-linear audit also
exposes the explicit
`universal_k_identity_canonical_strand_carrier_residual_faithfulness` flag.
The canonical carrier relation is now also classified as an admissible kernel
by `universal_k_canonical_strand_carrier_congruence_audit(...)`.  Its finite
trichotomy is: equality, which is the residual-faithful subcase above;
proper, which is a local-minimal contradiction; or universal, which is the
only canonical-carrier branch left for nontrivial U/C/M endpoint observers.
The post-linear wrapper now consumes the proper case as a terminal System K
exit: when the attached interval has an admissible proper canonical
strand-carrier kernel, it reports
`closed_by_canonical_strand_carrier_proper_congruence`, leaves no live K rows,
and creates no U/C/M endpoint obligation.
For the universal branch, the fixed-carrier monodromy constructor can now
consume a finite canonical-component value ledger.  The helper
`universal_k_canonical_strand_carrier_rows_with_values(...)` maps the abstract
canonical components into endpoint-group elements and then lets the existing
strand-carrier domain audit derive the singleton fixed-carrier domains.  This
does not close a U/C/M endpoint family by itself; the resulting observer still
has to prove monodromy, fixed-carrier coboundary constancy, target matching,
and residual faithfulness.
A new guardrail regression checks this explicitly: canonical component values
without endpoint-target and residual-faithfulness rows do not prove a family
observer, even though they can derive the strand-carrier singleton domains.
The fixed-carrier soundness witness list has also been tightened: opaque
`reachable_carrier_domain_invariant` assertions are rejected until backed by
an implemented finite invariant checker, leaving only locally verified
constant-track, singleton-domain, and strand-carrier-equation witnesses.
Those witnesses now have executable semantics rather than serving as labels:
each currently accepted witness must justify a singleton carrier domain, and
`constant_carrier_track` additionally requires the left and right active
carrier value to be equal on every detector track.  Non-singleton domains or
nonconstant active pairs are rejected before the coboundary identity is used.
This removes another false endpoint closure and leaves the same local
nontrivial observer-existence gap: construct residual-faithful U/C/M
monodromy-coboundary observers for all surviving intervals, or produce a
normalized-law counterexample.

The rack side now has a separate central full-twist obstruction recorded in
`proofs/rack_full_twist_order_bound.md`.  For a finite rack `Y`, the action of
`Delta_n^2=(sigma_1 ... sigma_{n-1})^n` on `Y^n` has order dividing
`exp Inn(Y)`, uniformly in `n`.  The proof uses the Artin-longitude formula:
if `P=L_{y_1}...L_{y_n}`, then the full twist sends each coordinate by
`P L_{y_i}^{-1}`; the total product `P` is preserved and the coordinate left
translations are conjugated by `P`.  Thus the `exp Inn(Y)`-th power is
trivial on every arity.  Consequently any finite bijective YBE solution
dominated by a finite rack must also have uniformly bounded central
full-twist orders.  The executable helper
`rack_full_twist_order_bound_audit(Y,n)` verifies the fixed-degree identities
and divisibility.  This does not yet solve the MO problem: the remaining
obstruction route is to find a finite degenerate bijective YBE solution whose
`rho_X,n(Delta_n^2)` orders grow with `n`, or else prove that such growth is
impossible for all finite bijective YBE solutions.
That route has also been narrowed for the known whole-solution branches.
`known_branch_full_twist_order_bound_audit(X,max_n)` records exact checked
prefix orders together with the symbolic uniform bound for involutive,
permutation-form, rack-type, and left-nondegenerate derived-rack branches.
For permutation-form solutions `R(x,y)=(sigma(y),tau(x))`, the pure-longitude
formula gives `Delta_n^2=(sigma tau)^(n-1)` on every coordinate, so the order
divides `ord(sigma tau)` uniformly in `n`; involutive rows have trivial full
twist, and left-nondegenerate rows route through the derived rack.  Exhaustive
size-three checks all land in one of these bounded branches.  Thus an
unbounded full-twist obstruction, if it exists, must come from a genuinely
remaining degenerate class not covered by these known symbolic branches.
The generated affine companion audit
`proofs/affine_f2_full_twist_audit.md` checks the translated affine
four-point universe by affine block-map composition for `1 <= n <= 7`: all
`24` untagged affine rows have central full-twist prefix orders
`1,2,1,2,1,2,1`, and the maximum observed prefix order across all `481`
affine YBE tables is `4`.
The point-pushing companion
`proofs/affine_f2_point_pushing_audit.md` checks the standard pure
point-pushing generators `A_{i,q}` in the same translated affine universe for
`2 <= q <= 5`.  All `24` untagged affine rows have generator-order profile
`2,2,2,2`; the recorded untagged examples have point-pushing subgroup sizes
`2,4,8,16` and exponent `2` through `q=5`.  Thus the easy pure-generator
order route to a normalized-law counterexample also leaves this checked
four-point affine universe.
The coordinate-dependency guardrail
`proofs/coordinate_dependency_audit.md` closes the elementary triangular
degenerate shapes for this same obstruction route.  If the first output of a
finite bijective YBE table depends only on the first input, or the second
output depends only on the second input, the YBE relation and bijectivity
force the identity table.  If the dependency is on the opposite input, then
bijectivity forces nondegeneracy, so the row routes through the existing
left-nondegenerate/guitar branch.  Exact enumeration in sizes `1,2,3` finds
`0` unclosed coordinate-dependency rows, with full-twist prefix orders checked
through `n=5`.

## 2026-06-03 point-pushing and Rees flatness correction

The point-pushing route has been corrected away from a false bounded-exponent
claim for the whole finite-rack point-pushing image.  The rack-only invariant
is the operator-label Hurwitz quotient

```text
y |-> L_y in Inn(Y)
```

with a vertical kernel whose exponent divides `exp Inn(Y)`, uniformly in the
braid index.  The note
`proofs/rack_point_pushing_operator_label_invariant.md` and generated audit
`proofs/rack_point_pushing_operator_label_audit.md` record this structure and
the dihedral-rack warning example: finite racks can already have unbounded
whole point-pushing complexity, so the invariant is the bounded-exponent
vertical extension over a fixed group-Hurwitz tower.
Route (1) is now recorded explicitly in
`proofs/finite_augmented_artin_envelope_route.md`, with
`proofs/finite_augmented_artin_envelope_route_audit.md` generated from the
public helper `finite_augmented_artin_envelope_route_audit()`.  This ledger
separates the proved rack-side operator-label extension from the two missing
positive lemmas: the finite augmented Artin-envelope lemma for arbitrary
finite bijective YBE point-pushing towers, and the realization lemma turning
compatible augmented envelopes into marked quotients of actual finite rack
towers.  It also fixes the first obstruction-prefix generators
`alpha_{i,4}` and `alpha_{i,5}` for the `Q_X(3)` and `Q_X(4)` pressure tests,
so future negative attempts must defeat every fixed finite group-Hurwitz base
plus bounded-exponent vertical kernel, not merely exhibit unbounded order.
The companion pressure-test note
`proofs/finite_augmented_artin_envelope_pressure_tests.md` and generated
audit `proofs/finite_augmented_artin_envelope_pressure_audit.md` now list the
true-or-false mechanisms for this missing lemma.  Positive routes must make
either translation-pair labels `(lambda_x,rho_x)` or a finite
structure/derived-action quotient into a well-defined label-Hurwitz model
with coordinatewise vertical action in one fixed finite group.  Negative
routes must realize one of four finite mechanisms in an actual finite YBE
table: non-conjugation-stable labels, ordered-neighbor memory inside the
label kernel, point-forgetting incompatibility of vertical kernels, or a
genuinely unbounded vertical kernel.  The ledger explicitly excludes
whole-image exponent growth as a valid obstruction.
The completed external route question then sharpened the positive
nondegenerate object: use the guitar-conjugated derived Hurwitz envelope,
not raw `lambda/rho` operator groups.  The new note
`proofs/finite_derived_hurwitz_envelope.md` and generated audit
`proofs/derived_hurwitz_envelope_audit.md` record the repository convention
`J_2(x,y)=(lambda_x(y),x)`, the derived operation
`a*b=lambda_a(rho_y(b))` for the unique `y` with `lambda_b(y)=a`, and a
three-strand conjugacy check.  They also record the prefix-group issue for
interior point-forgetting: deleting an interior guitar label need not match
guitarizing the forgotten tuple, so the finite prefix group
`L_X=<lambda_x>` is the necessary tower bookkeeping.  For left-degenerate
rows, the audit records the first failure gate: the preimage `y` may be
missing or nonunique, so the derived Hurwitz operation is not a total
well-defined binary operation without extra memory.
The next note `proofs/degenerate_preimage_memory_gate.md` and generated audit
`proofs/degenerate_preimage_memory_audit.md` isolate the canonical finite
local repair for that preimage ambiguity.  For each visible pair `(a,b)`,
the fibre `P(a,b)={y:lambda_b(y)=a}` is classified as singleton, missing,
multiple-same-candidate, or ambiguous.  The finite edge-memory graph
`E_X={(a,b,y):lambda_b(y)=a}` always has `|X|^2` states and repairs the
two-strand preimage lookup locally, but the audit records that this is only a
local repair: route (1) still needs triple/quadruple compatibility and
point-forgetting compatibility to turn edge memory into a finite
group-Hurwitz tower with bounded vertical kernel.
The new edge-memory tower prefix
`proofs/edge_memory_tower_prefix.md` and generated audit
`proofs/edge_memory_tower_audit.md` check the first local tower gates for the
canonical adjacent edge label `e(x,y)=(lambda_x(y),x,y)`.  Adjacent edge
labels encode arity-3 and arity-4 tuples injectively, the arity-3 braid
relation survives edge encoding, and all arity-4 braid-generator and
point-forgetting maps are well-defined on the finite edge-memory state space.
This moves the remaining route-(1) target from local preimage ambiguity to
the real point-pushing layer: compress this memory to one fixed finite
operator/Hurwitz base with uniformly bounded-exponent vertical kernels, or
find a degenerate table where that vertical compression fails compatibly in
the `Q_X(3),Q_X(4),...` tower.
The next refinement, `proofs/prefix_edge_transducer_tower.md` with generated
audit `proofs/prefix_edge_transducer_audit.md`, replaces raw adjacent pair
memory by the finite left-prefix path transducer over the transformation
monoid `M_lambda=<lambda_x>`.  A tuple is encoded by edges
`(P,x,P lambda_x)`, the local move is endpoint-preserving because
`lambda_x lambda_y=lambda_u lambda_v` for `r(x,y)=(u,v)`, and interior
point-forgetting is handled by a finite prefix rescan.  The arity-four audit
records that forgetting fibres have size at most `|X|`.  This gives a
canonical finite transducer tower for degenerate memory, but it still is not
the finite augmented Artin-envelope lemma: a transformation-monoid transducer
must still be group-completed to a fixed finite group-Hurwitz base with
bounded-exponent vertical noise, or a compatible `Q_X(3),Q_X(4),...`
obstruction to that group-completion must be found.
The follow-up note
`proofs/prefix_group_hurwitz_compression_pressure.md` and generated audit
`proofs/prefix_group_hurwitz_compression_pressure_audit.md` record the exact
finite equations such a group-completion must satisfy.  A label map from
prefix edges `(P,x,P lambda_x)` to a conjugation-stable subset of one finite
group must descend every local move to the ordinary Hurwitz rule, preserve
the total group-label product up to the allowed vertical kernel, and remain
lumpable under interior point-forgetting prefix rescans.  The audit also
separates the group-like prefix case from genuinely degenerate rows whose
left-prefix monoid contains nonunit transformations; those nonunits cannot be
faithfully embedded as a transformation monoid inside a group, so any
positive proof must quotient or encode them with bounded vertical noise.  The
first obstruction surface remains the compatible `Q_X(3)` and `Q_X(4)`
point-pushing comparison.
That surface is now executable in `proofs/prefix_point_pushing_surface.md`
and generated audit `proofs/prefix_point_pushing_surface_audit.md`.  The
helper `prefix_point_pushing_surface_audit(X)` computes the standard
`alpha_{i,4}` and `alpha_{i,5}` marked point-pushing generator actions, checks
that prefix-path encoding sees the same action as the tuple action, and
records finite subgroup size and exponent when untruncated.  On the two-point
nondegenerate prefix witness the computed `Q_X(3),Q_X(4)` sizes are `8,16`
with exponent `2`; on the degenerate identity row the point-pushing groups are
trivial despite the nonunit prefix monoid.  Thus a negative route must use a
less trivial degenerate table whose group-Hurwitz compression failure is
visible in this marked surface and remains compatible in the tower.
The tiny-corpus follow-up
`proofs/prefix_point_pushing_tiny_corpus.md` and generated audit
`proofs/prefix_point_pushing_tiny_corpus_audit.md` exhaustively check all
whole bijective YBE tables on two and three points against that same first
surface.  There are `5` size-two and `73` size-three tables.  The only
size-two left-degenerate nonunit-prefix row is the identity table, and the
seven size-three left-degenerate nonunit-prefix rows are all involutive; in
every one of these rows `Q_X(3)` and `Q_X(4)` are trivial.  Consequently the
first whole-table obstruction, if any, begins at size at least `4`, or else
inside quotient-fibre local intervals rather than the tiny whole-table
corpus.
The next note
`proofs/prefix_artin_envelope_cohomology.md` and generated audit
`proofs/prefix_artin_envelope_cohomology_audit.md` rephrase the remaining
finite augmented Artin-envelope lemma as an action-groupoid cohomology
problem: a bounded Artin-equivariant transgression lemma.  At a fixed arity
`K_n` is free, so the obstruction is not an abstract point-pushing relator.
The missing structure is one finite operator-label groupoid or group-Hurwitz
quotient, one finite coefficient system of vertical groups, and one bounded
cohomology class whose pullbacks give the residual point-pushing extension
classes for all arities.  These classes must restrict compatibly under
point-forgetting, insertion, and relabelling maps.  The audit records this
first ledger on `Q_X(3),Q_X(4)`: for the nondegenerate prefix witness the
action-groupoid arrow counts are `128` and `512` with two orbits at both
arities, while for the degenerate identity row all tuple orbits are
singletons despite nonunit prefix memory.  This makes the next positive
target precise and makes the negative target a compatible unbounded or
nonrestricting vertical cocycle class, not merely unbounded point-pushing
order.
The restriction-surface follow-up
`proofs/prefix_point_forgetting_restriction.md` and generated audit
`proofs/prefix_point_forgetting_restriction_audit.md` compute the first
actual point-forgetting naturality comparison `Q_X(4) -> Q_X(3)`.  Deleting
stationary strand `j` sends the marked generator `alpha_{i,5}` to identity
for `i=j`, to `alpha_{i,4}` for `i<j`, and to `alpha_{i-1,4}` for `i>j`.
For the nondegenerate prefix witness all off-diagonal rows match, while the
four diagonal rows each have `32` tuple-level mismatches: the abstract braid
forgets to identity, but the labels retain vertical monodromy around the
deleted strand.  For the degenerate identity row all sixteen rows match.
Thus the first concrete vertical point-forgetting cocycle is now visible, and
the remaining theorem-level question is whether such diagonal cocycles are
always absorbed by a fixed finite operator-label base with bounded vertical
exponent.

The semigroup/Green route has also been narrowed to a precise Rees rectangle
flatness target.  Ordinary Green/Rees theory leaves a sandwich-matrix
cocycle

```text
omega(lambda,mu; i,j)
  = p[lambda,i] p[mu,i]^{-1} p[mu,j] p[lambda,j]^{-1}
```

which need not vanish in a general finite regular semigroup.  The new note
`proofs/rees_rectangle_cocycle_flatness_target.md` isolates the missing
YBE-specific lemma: Artin corridors in finite bijective YBE local intervals
must force these Rees rectangles to be trivial, or at least coboundaries
absorbed by uniformly bounded vertical noise.  The generated audit
`proofs/rees_rectangle_cocycle_audit.md` fixes the nonabelian convention and
checks the smallest algebraic obstruction, a `2 x 2` `C2` square with three
identity sandwich entries and one nonidentity entry.  This square is not
claimed to be a YBE solution; it is the finite pattern a negative route would
have to realize compatibly in the point-pushing tower.

The next Rees audit sharpens the obstruction target from a static sandwich
matrix to a local braid-cocycle pattern.  The note
`proofs/rees_braid_cocycle_obstruction_pattern.md` and generated audit
`proofs/rees_braid_cocycle_obstruction_audit.md` use four quotient states
`q00,q01,q10,q11` and two `C2`-labeled rows.  The rows satisfy
`T1 T2 T1 = T2 T1 T2`, so the local braid/YBE cocycle identity holds, but
the commutator `[sigma1^2,sigma2^2]` fixes every quotient state and adds the
nonidentity `C2` label.  This shows that braid-cocycle consistency is weaker
than Rees flatness.  The remaining all-`n` obstruction task is to realize
this finite pattern inside an actual finite bijective degenerate YBE
quotient-fibre interval and prove the resulting nonflat holonomy cannot be
absorbed by a fixed finite group-Hurwitz base with bounded-exponent vertical
kernel.  A direct-locality shadow check has also been added: a literal
three-strand coordinate quotient would give nontrivial fixed partitions for
the `sigma1` and `sigma2` rows, jointly separating the four states.  The
obstruction rows are both four-cycles and fail this direct coordinate-local
condition, so any realization must occur deeper inside a quotient-fibre
interval after the outside-coordinate partitions have been hidden or
collapsed.  The same generated audit now exhaustively checks the literal
two-element adjacent-binary realization problem: no bijection `R:A^2->A^2`
and embedding of the four states into `A^3` induces these two rows, even
before requiring `R` to satisfy YBE globally.  Thus the current obstruction
pattern is a residual quotient-fibre search target, not a direct small
set-theoretic construction.  The new outer-constant slice audit then shows
the next forced shape: with embedded states `(a0,m_q,c0)`, the four-cycle rows
need one extra outer symbol, so a raw adjacent-binary partial slice exists
for `|A|=5` and extends to a bijection of `A^2`; the displayed completion
does not satisfy YBE.  The realization problem has therefore been sharpened
to a global YBE-completion problem for that partial adjacent slice.  The
completed theoretical realization query further isolates a minimal
sideways-completion obstruction: in a singleton-boundary, type-preserving
quotient model with `R(L,m)=(L,A(m))`, `R(m,R)=(B(m),R)`, and
`R(L,R)=(L,R)`, the sideways YBE faces force the reverse maps to be identity
and then force `A=B=1`.  Therefore the four-cycle pair cannot occur in this
minimal quotient-fibre model; any realization must use nontrivial boundary
fibres, non-preserved reverse-side types, or nontrivial boundary-boundary
holonomy.

## Verification snapshot

At the latest verified snapshot:

- `python -m unittest tests.test_nonlinear_overlap` passed with 194 tests;
- `python -m unittest discover -s tests` passed with 733 tests;
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

## Point-Forgetting Square Cocycle Ledger

After the single point-forgetting surface
`proofs/prefix_point_forgetting_restriction.md`, the crossed-module pressure
test from the continuing GPT-5.5 Pro thread identified the next finite datum:
deletion-square compatibility before any genuine deletion-cube/Postnikov
class can be tested.  The new note
`proofs/prefix_deletion_square_restriction.md` and generated audit
`proofs/prefix_deletion_square_restriction_audit.md` compute this first
two-face surface:

```text
Q_X(5) <= G_X(6)   --->   Q_X(3) <= G_X(4).
```

For source generator `alpha_{i,6}` and deleted stationary strands `j<k`, the
marked target is identity exactly when `i` is one of the deleted strands, and
otherwise is the reindexed generator `alpha_{i-c,4}`.  The audit checks all
ten deleted pairs and five source generators, for `50` rows, and also checks
that the two coordinate-deletion orders commute on the source action.

For the nondegenerate two-point prefix witness, all `30`
surviving-generator rows match exactly.  The `20` rows where the source
generator is deleted each have `64` mismatches, for total mismatch `1280`.
The two deletion orders nevertheless commute in every row.  Thus the
two-face layer is ordinary face-compatible but carries vertical monodromy on
deleted-generator rows.  For the degenerate identity row all `50` rows match.

This is still not a counterexample to finite rack domination.  It records the
first square ledger that a positive finite operator-label Artin-envelope
lemma must absorb with bounded vertical exponent.  The next possible
obstruction is a genuine deletion-cube/Peiffer coherence class, where the
two-face defects must themselves be compatible under three stationary
deletions.

## Deletion-Cube Restriction Ledger

The note `proofs/prefix_deletion_cube_restriction.md` and generated audit
`proofs/prefix_deletion_cube_restriction_audit.md` compute the first direct
three-face point-forgetting ledger:

```text
Q_X(5) <= G_X(6)   --->   Q_X(2) <= G_X(3).
```

For source generator `alpha_{i,6}` and deleted stationary strands `j<k<l`,
the marked target is identity exactly when `i` is one of the three deleted
strands, and otherwise is the reindexed generator `alpha_{i-c,3}`.  The
audit checks all ten deleted triples and five source generators, for `50`
rows.  It also checks all six coordinate-deletion orders in every row.

For the nondegenerate two-point prefix witness, all `20`
surviving-generator rows match exactly.  The `30` rows where the source
generator is deleted each have `64` mismatches, for total mismatch `1920`.
All six deletion orders nevertheless commute in every row.  For the
degenerate identity row all `50` rows match.

This proves that the direct cube faces have ordinary semi-simplicial
compatibility while the same vertical point-forgetting monodromy persists on
deleted-generator rows.  It does not yet produce a gauge-invariant secondary
class.  The next genuine obstruction would have to assemble the square
defect ledgers into a Peiffer/Postnikov class and show that a base-trivial
deletion cube has nontrivial transported square-boundary in a vertical
coefficient group.
