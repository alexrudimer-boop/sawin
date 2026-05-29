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
closed quotient is nevertheless a total finite rack layer.  Thus the symbolic
theorem must prove either trivial descent, controlled descent-closed rack
quotients plus endpoint/unit detection for the lost lower information, or a
real normalized-law counterexample.

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

## Current bottleneck

The unresolved mathematical task is the Master Local-Minimal Residual
Theorem, now concentrated in the bi-free universal-corridor branch:

```text
For every local-minimal interval pi:X->Z with Z dominated by Q,
construct one finite group G(pi,Q), independent of n, such that
Lambda_{G(pi,Q),n}(beta)=Lambda_{G(pi,Q),n}(1)
implies Delta_n(beta)=1 for all n and beta in ker rho_{Q,n}.
```

The current best A route is to prove that all residual Green/corridor
endpoint units are explicit products of recursive Artin-longitude evaluations
in the fixed product of the finite groups above.

The current best B route is to construct a finite local-minimal interval in
this exact bottleneck branch whose unit/group-like residual holonomy admits a
normalized-law sequence invisible to every finite group but moving an explicit
tuple.

Until one of these is done, the archive supports neither final A nor final B.

## Verification snapshot

At the latest verified snapshot:

- `python -m unittest discover -s tests` passed with 277 tests;
- `python -m compileall -q src tests tools` passed;
- `node --check tools/build_reduction_audit_workbook.mjs` passed;
- the proof log DOCX and reduction audit workbook were regenerated;
- LibreOffice/`soffice` was unavailable, so DOCX visual render QA could not
  be completed;
- the Desktop zip was overwritten rather than versioned separately.
