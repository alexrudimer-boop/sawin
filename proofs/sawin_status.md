# Sawin finite-rack domination status

Date: 2026-05-29

## Required final output

The final result must be exactly one of the following.

A. A complete proof that every finite bijective set-theoretic Yang-Baxter
solution is dominated by a finite rack, with the rack independent of braid
index.

B. An explicit finite bijective YBE solution not dominated by any finite rack,
with a normalized-law obstruction sequence.

This file is a working proof log, not the final answer.  The candidate
proof-side positive assembly is recorded in
`proofs/master_local_residual_positive_closure.md`, but the proof-critic gap
audit in `proofs/proof_critic_gap_audit.md` shows that the current branch does
not yet prove outcome A.  The older `proofs/final_completion_audit.md` is
superseded.
The current repair target is stated in
`proofs/descent_endpoint_repair_contract.md`.

## External-state check

Web search on 2026-05-28 found the finite-rack domination problem as an open
MathOverflow question by Will Sawin.  A recheck on the same date found the
page still with `0` answers and no posted resolution:
https://mathoverflow.net/questions/509988/set-theoretic-solutions-to-the-yang-baxter-equations-and-racks

A linked MathOverflow question isolates a "local branch-choice rigidity"
obstruction in Green R-classes; that page also had `0` answers on recheck:
https://mathoverflow.net/questions/510916/local-branch-choice-rigidity-in-green-r-classes-of-finite-set-theoretic-yang-baxter-solutions

That obstruction matches the master local-minimal residual gap in the current
reduction program.

## Reduction audit

### 1. Quotient/residual setup

For a quotient `pi : X -> Z` and a rack `Q` dominating `Z`, the residual action
is correctly organized by

```text
N_n = ker rho_{Q,n},
X_z = product_i pi^{-1}(z_i),
delta_{n,z}: N_n -> Sym(X_z),
Delta_n(beta) = (delta_{n,z}(beta))_z.
```

This setup is sound as a bookkeeping reduction: once `beta in N_n`, the base
`Z^n` point is fixed, so all remaining motion is fibrewise.

### 2. Sharp obstruction theorem

The detector rack

```text
A_G = T_2 x (G x G),
(a,u) ▷ (b,v) = (a b a^{-1}, a v)
```

is treated as the finite-rack mechanism for finite-group Artin-longitude data.
The required kernel implication is

```text
Lambda_{G,n}(beta) = Lambda_{G,n}(1)  =>  Delta_n(beta) = 1
```

for all `n` and `beta in N_n`.  If this holds, `Q x A_G` dominates the interval.

The remaining burden is not the rack construction but the uniform existence of
one finite group `G = G(pi,Q)` independent of `n`.

The rack construction step itself is now written as
`proofs/sharp_obstruction_theorem.md`.  It proves that
`ker rho_{A_G,n}` is exactly the condition
`Lambda_{G,n}=Lambda_{G,n}(1)`, because the `T_2` factor detects the Artin
permutation and the active `G x G` factor carries the recursive image and
longitude coordinates.  Consequently, if the residual kernel implication
holds over a quotient dominated by `Q`, then `Q x A_G` dominates the total
interval.  The same note also records the equivalence between kernel form and
collision form, and the iteration `Q_i=Q_{i+1} x A_{G_i}` along a finite
congruence chain.
The construction is now executable as `sharp_obstruction_rack(Q,G)`, backed by
the generic `product_solution()` and `is_rack_solution()` helpers.  This
explicitly returns the finite rack `Q x A_G` with `|Q|*2*|G|^2` elements and
keeps the final rack-construction step separate from the still-open task of
finding the uniform local detector group `G(pi,Q)`.
The chain-level assembly is also executable as
`assemble_congruence_chain_rack(Q_m, groups)`.  It iterates
`sharp_obstruction_rack` down a supplied finite detector list, records every
factor `2*|G_i|^2`, and exposes the final rack object without accepting any
braid-index input.
The summary-level wrapper `closed_local_detector_chain(summaries)` now checks
the step immediately before this construction: each closed local bottleneck
row must supply one actual interval group `G_i`, obtained by producting any
closed detector factors for that same interval.  The wrapper
`assemble_closed_local_detector_chain_rack(Q_m,summaries)` refuses open
product/corridor verdicts and delegated detector gaps, so the global rack
assembly cannot accidentally hide an unproved local theorem step.

There is also a direct rack-action version of the same principle.  For a
finite rack `Y`, the left translations generate a finite inner group
`Inn(Y) <= Sym(Y)`.  The braid action on `Y^n` is obtained by evaluating the
recursive Artin longitudes in `Inn(Y)`: the `j`-th output is
`eval(L_j(beta))(y_{p(j)})`.  Hence
`Lambda_{Inn(Y),n}(beta)=Lambda_{Inn(Y),n}(1)` implies
`rho_{Y,n}(beta)=1`.  This is recorded in
`proofs/finite_rack_longitude_quotient.md` and implemented by
`rack_inner_group()` and `rack_longitude_action()`.  It proves the final
step for outcome B: a sequence invisible to every finite group is invisible
to every finite rack by taking `G=Inn(Y)`.

The finite-G condition can be reformulated through a verbal quotient of the
free group.  For fixed finite `G` and degree `n`, let

```text
K_G(n) = intersection_{phi:F_n -> G} ker(phi),
W_G(n) = F_n / K_G(n).
```

Then `W_G(n)` is finite, and
`Lambda_{G,n}(beta)=Lambda_{G,n}(1)` is exactly the statement that the braid
permutation is trivial and every recursive Artin longitude lies in `K_G(n)`.
Such a braid acts trivially on `W_G(n)`.  Therefore a local interval is
detected by the fixed finite group `G` if its residual action factors, for all
`n`, through the Artin action on `W_G(n)`.  This does not make the rack depend
on `n`: the proof quotient `W_G(n)` varies with `n`, while the detector rack
`A_G` is fixed.  The remaining Green/corridor task is precisely to prove this
finite-longitude factorization for a group `G(pi,Q)` built from the finite
interval data, or to construct a normalized-law sequence showing that no such
fixed finite `G` can work.
The fixed detector-action criterion now also has an executable readout
version: `exact_detector_readout_audit(...)` enumerates one fixed braid degree
and, when successful, displays a table from reachable base-kernel detector
states to residual permutations.  The rows now also check quotient-fibre
preservation and count the moved base fibres and total tuples, so the table is
directly aligned with the residual maps `delta_{n,z}`.  This clarifies the
all-`n` target: the Green/corridor proof must construct these readouts
symbolically from one fixed finite detector, rather than accumulating
fixed-degree tables.
The direct symmetric candidate now has the wrapper
`symmetric_detector_readout_audit(X,n)`, which specializes this readout test
to the one-point quotient and the single detector group `Sym(X)`.  It proves
the fixed `n=2` readout for the size-three affine stress row exactly, with
`12` reachable base-kernel detector states and `3` residual action states.
This is deliberately recorded as fixed-index evidence only; it does not make
`G` depend on `n`, and it does not prove the missing all-degree theorem.
The product-readout helper `exact_detector_product_readout_audit(...)` now
checks the same issue after multiplying finitely many displayed detector
factors into one product group: in enumerated fixed-degree cases, the factor
readout table and the direct-product readout table have the same residual
readouts and proof status.  This reinforces that the eventual local detector
must be one finite `G(pi,Q)`.

The longitude-value subgroup criterion is now explicitly functorial under
fixed finite group homomorphisms.  The note
`proofs/longitude_subgroup_functoriality.md` proves that
`f(V_beta(G)) <= V_beta(H)` for every finite homomorphism `f:G -> H`, with
equality when `f` is surjective.  This lets product-label, normalized
holonomy, unit-holonomy, Green kernel-block, and Schutzenberger factors be
related by fixed finite quotients or projections without changing the braid
index or weakening the finite-G longitude implication.
The same functoriality now has an explicit witness form:
`pushforward_longitude_subgroup_witness(...)` applies the homomorphism to
every assignment entry in a displayed longitude-subgroup word and verifies
that the pushed witness evaluates to the homomorphic image.

The direct-product version is exact as well:
`proofs/longitude_subgroup_products.md` proves
`V_beta(prod_i G_i)=prod_i V_beta(G_i)`.  Consequently, factorwise
longitude-subgroup membership for product-label, normalized holonomy,
unit-holonomy, Green, Schutzenberger, quotient, and known-branch detector
labels combines into membership in one fixed finite product detector group.
The new note `proofs/longitude_subgroup_witness_calculus.md` records the
certificate-level version: given explicit factor witnesses,
`direct_product_longitude_subgroup_witness(...)` embeds them with identity
assignments in the other coordinates and concatenates them into one product
witness.  This is now the preferred way to move from factor endpoint
certificates to the single finite product detector required by the sharp
obstruction theorem.
This justifies using a single `A_G` for the local interval after all factors
are multiplied.

The same compatibility now holds at the detector-action/readout level.
`proofs/detector_action_products.md` proves that the active state of
`A_{prod_i G_i}` projects coordinatewise to the active states of the
individual `A_{G_i}` detector actions.  Hence separate residual readouts
through fixed branch detectors can be assembled into one readout through the
single product detector rack required by the sharp obstruction theorem.

The purity convention is now isolated in
`proofs/purity_stabilization.md`.  Branch arguments that use pure-braid
formulas do not assume that `beta in ker rho_{Q,n}` is pure.  Instead the full
detector rack `A_G=T_2 x (G x G)` supplies a `T_2` factor whose kernel is the
pure braid group.  Thus the Artin permutation is killed by the
`Lambda_{G,n}(beta)=Lambda_{G,n}(1)` hypothesis, and only then may pure-braid
formulas such as the involutive/permutation branch formula be invoked.

The same condition now has a compact subgroup profile.  For a braid `beta`,
let `V_beta(G)` be the subgroup of `G` generated by all recursive-longitude
values `phi(L_i(beta))` over all assignments `F_n -> G`.  Then identity
finite-`G` longitude data is equivalent to trivial Artin permutation and
`V_beta(G)={1}`.  The helper `longitude_subgroup_profile()` records this
finite-group visibility row, and
`law_braid_longitude_subgroup_profile()` applies it after the standard
pure-braid law embedding.  The note
`proofs/longitude_subgroup_profile.md` records this profile.  It gives a
compact way to audit B candidates: every fixed finite group must eventually
have subgroup size `1`, while the YBE action still moves a tuple.
The companion mover-profile helpers attach the first moved total or residual
tuple to these subgroup rows, so a candidate obstruction can be audited as
"invisible to the listed finite groups but still moving here."  This remains
bounded diagnostic evidence unless it is upgraded to the required symbolic
all-finite-group normalized-law sequence.
The assigned-generator law separator has now been factored out as
`short_law_separating_permutation_assignment(...)`.  It searches for a word
that is a law on the listed finite detector groups but evaluates
nontrivially on the specific tuple of permutation images supplied by a
candidate construction.  This is the exact finite diagnostic used by the
structure-orbit B route, where the assigned tuple is the restriction of the
standard pure braid generators to one structure orbit.

The bounded-degree action-image limitation is now recorded in
`proofs/bounded_degree_action_image_limit.md`.  For fixed `n`, the image
`rho_{X,n}(B_n)` and the degree-`n` structure-orbit holonomy groups are finite,
but using them directly makes the detector depend on `n`.  They are valid
diagnostic objects only after one proves an all-`n` factorization through a
fixed finite group.  A regression on the three-point dihedral rack records
that degree-`4` action image growth can occur even in a rack already dominated
by its fixed inner group, so moving image growth alone is not a B
counterexample.

The normalized-law route is also constrained by a fixed-variety barrier,
recorded in `proofs/fixed_variety_barrier.md`.  If the relevant moving pure
images or residual holonomy groups all lie in the group variety generated by
one fixed finite group `G_0`, then every word that is eventually a law on
`G_0` is eventually a law on those moving groups as well.  Therefore a B
sequence through law-braid embeddings must show finite-variety escape for
every fixed `G_0`, not just growth of the finite image groups.  The helper
`short_law_escaping_variety()` gives bounded finite certificates of such
escape; absence of a short escape remains only bounded evidence.

A branch-level form of the same criterion is now isolated as
label-longitude factorization.  If the residual coordinate maps in a branch
are controlled by elements of one finite label group `H`, and each such label
element is an evaluation, or fixed finite product of evaluations, of the
recursive Artin longitudes under homomorphisms `F_n -> H`, then `A_H` detects
that branch for every braid degree.  Product-permutation label words,
Green/corridor transports, and Schutzenberger branch choices are now all
phrased against this same target: construct the finite label group from the
interval and prove the all-`n` longitude-evaluation factorization, or produce
a normalized-law sequence whose label word remains nontrivial while every
finite group sees trivial longitudes.

The factorization criterion has also been generalized to input-dependent
homomorphisms.  Since finite-G longitude identity quantifies over every
homomorphism `F_n -> G`, a proof may choose the homomorphism after seeing the
input fibre tuple.  This is how racks work: for a finite rack `Y`, assign
`x_i` to the left translation by the actual input label `y_i` in `Inn(Y)`,
and the `j`-th output is the evaluation of the recursive longitude
`L_j(beta)` on the appropriate input coordinate.  The helper
`rack_longitude_factorization()` exposes this input-dependent assignment and
the evaluated longitude values.  The note
`proofs/input_dependent_longitude_factorization.md` records the general
criterion.  This explains why multi-input dependency support is not a
negative obstruction by itself; the remaining Green/corridor task is to prove
such an input-dependent factorization through fixed finite holonomy groups.

The same bridge is now recorded in a stricter action-factor form in
`proofs/fixed_detector_action_factorization.md`.  If, for one fixed finite
group `G`, every residual action `delta_{n,z}` on `N_n` factors through the
restricted detector-rack action `rho_{A_G,n}(N_n)`, then identity finite-`G`
longitude data forces the residual action to be trivial.  A concrete readout
version allows the detector state and readout map to depend on the input
fibre tuple, but all braid-word dependence must pass through the fixed rack
`A_G`.  This gives the remaining product-holonomy and Green/corridor branches
an action-level target: construct such readouts uniformly in `n`, or produce
a normalized-law sequence whose residual motion cannot be read from any fixed
detector action.

Multiple finite detector factors can be combined without changing the sharp
criterion.  The direct product group `G=product_j G_j` has identity
finite-group longitude data exactly when every factor `G_j` has identity
longitude data, because homomorphisms `F_n -> G` are tuples of homomorphisms
to the factors and identity in `G` is coordinatewise identity.  The helper
`direct_product_group()` implements this finite group.  Thus cyclic,
product-label, affine/semidirect, Green kernel-block, Schutzenberger, and
known-branch detector factors can be multiplied into the single `G_i` needed
for one local interval; the rack step remains `Q_i=Q_{i+1} x A_{G_i}`.

Cartesian products of already dominated finite solutions are also harmless.
If `ker rho_{Y_i,n} <= ker rho_{X_i,n}` for every factor and every `n`, then
the coordinatewise product rack `prod_i Y_i` dominates the product solution
`prod_i X_i`, because the braid action on a product solution is the product
of the factor braid actions and the kernel of the product rack action is the
intersection of the factor kernels.  This all-`n` closure is recorded in
`proofs/product_domination_closure.md` and is independent of finite search.
Thus a B counterexample cannot be assembled merely as a Cartesian product of
already dominated branches.

A swapped product extension over a nondegenerate quotient is now also routed
symbolically.  In swapped product form
`T_{a,b}(x,y)=(L_{a,b}(y),R_{a,b}(x))`, left and right nondegeneracy of the
quotient colour maps lift through the fibre bijections `L` and `R` to left
and right nondegeneracy of the total solution.  Therefore arbitrary-fibre
swapped product holonomy over a nondegenerate quotient lies in the known
nondegenerate/guitar branch.  The proof is recorded in
`proofs/swapped_product_nondegenerate_base.md`; the direct product form is
explicitly excluded from this shortcut.

Domination is also hereditary along braided-set quotients and subsolutions.
For a quotient `pi:X -> Z`, the braid actions commute with projection, so
`ker rho_{X,n} <= ker rho_{Z,n}`.  For a crossing-closed subset `S <= X`,
the restricted solution has the same braid action on `S^n`, so
`ker rho_{X,n} <= ker rho_{S,n}`.  Hence any rack dominating `X` also
dominates every quotient and subsolution.  The proof is recorded in
`proofs/hereditary_domination_closure.md`; it is an all-`n` kernel inclusion
and not search evidence.  A minimal B counterexample may therefore be assumed
quotient-minimal and subsolution-minimal.

The analogous nondegenerate-cover shortcut is now ruled out.  A quotient of a
finite left or right nondegenerate solution is again left or right
nondegenerate, because the descended coordinate maps are surjections of a
finite quotient set.  Therefore a degenerate finite solution cannot be
obtained as a braided-set quotient of a finite nondegenerate solution, and the
known guitar branch cannot solve the degenerate case by passing to a hidden
nondegenerate cover.  This guardrail is recorded in
`proofs/nondegenerate_cover_obstruction.md`.

The quotient/residual setup also has an exact fixed-degree image-kernel
form.  For a finite quotient `pi:X -> Z`, the finite braid image on `X^n`
maps onto the finite braid image on `Z^n`; the kernel consists precisely of
the residual actions of base-fixing braids.  The helper
`quotient_image_kernel_summary(qmap,n)` closes this joint image and reports
the residual kernel size, projection surjectivity, and a first nonidentity
kernel word when one exists.  This is recorded in
`proofs/quotient_image_kernel_exact_sequence.md`.  It is only a fixed-`n`
certificate, but it clarifies the theorem-level target: construct one finite
group `G(pi,Q)`, independent of `n`, whose finite-G longitude identity kills
these moving kernel images for every `n`.

The residual action also has a fixed-degree dependency support diagnostic.
For a base-fixed braid and base tuple `z`, the helper
`residual_coordinate_dependency_summary(qmap,z,beta)` records which input
fibre coordinates each output coordinate actually depends on.  Coordinatewise
support points toward product-label, affine, coboundary, cyclic, or
pairwise-linking detectors.  Multi-input support is not itself an obstruction
to A, since racks already have multi-input coordinate dependence but are
detected by their inner groups; rather, it marks the branch where the
Green/corridor, Schutzenberger, kernel-block, and semigroup-holonomy
machinery must provide the all-`n` factorization.  The diagnostic is recorded
in `proofs/residual_dependency_support.md`.  The companion bounded classifier
`residual_detector_dependency_failures()` attaches these supports to
detector-blind residual movers; a guardrail test with a deliberately
too-small detector on a dihedral rack reports multi-input support, as
expected for a failure that the rack inner group, not product labels, should
detect.

### 2a. Direct rack-cover shortcut

A naive stronger route would be to construct a finite rack `Y` mapping onto
`X` as a braided set.  This is impossible unless `X` is already rack-type in
the second coordinate.  Indeed, if `p : Y -> X` is a braided-set homomorphism
from a rack with `R_Y(a,b)=(a ▷ b,a)`, then for `p(a)=x`, `p(b)=y`, and
`R_X(x,y)=(u,v)`, the second coordinate of the homomorphism equation forces
`v=x`.  Therefore direct rack covers solve only the rack-type branch.  The
finite-rack domination proof, if true, must use indirect detector racks such
as `Q x A_G`; failure of direct cover is not a B obstruction.

### 3. Congruence-chain induction

Given a maximal congruence chain

```text
Delta_X = kappa_0 < ... < kappa_m = Nabla_X,
```

the global theorem follows if each local-minimal interval
`X/kappa_i -> X/kappa_{i+1}` has a finite detector `G_i`, because the racks can
be pulled back down the chain by

```text
Q_i = Q_{i+1} x A_{G_i}.
```

This induction is formally valid only after the local theorem supplies
detectors for all intervals and those detectors are independent of `n`.
The executable assembly helper
`assemble_congruence_chain_rack(Q_m, groups)` now implements this recurrence
directly.  Its audit rows record `|Q_i|=|Q_{i+1}|*2*|G_i|^2` for each fixed
finite detector group and return the final rack `Q_0`.  This checks the
formal induction mechanics while leaving the master local detector theorem as
the open mathematical input.

The A/B fork is now isolated in `proofs/master_local_dichotomy.md`.  If every
local-minimal interval in a saturated congruence chain has a finite detector
group, the recursion above proves domination.  Conversely, if one explicit
finite local-minimal interval over a quotient dominated by `Q` is proved to
have no finite detector group, the diagonal normalized obstruction lemma
produces braids `beta_j in ker rho_{Q,q_j}` with `q_j -> infinity`, eventually
trivial finite-group longitude data for every finite group, and nontrivial
residual motion.  The finite-rack longitude quotient then shows that the
finite solution attached to that local interval is not dominated by any
finite rack.  Thus the remaining theorem burden is exactly the master local
theorem, or one explicit no-finite-G local interval.

### 4. Local residual table

For colours `a,b in Z`, fibres `A_a`, and

```text
R_Z(a,b) = (a.b, a*b),
T_{a,b}: A_a x A_b -> A_{a.b} x A_{a*b},
```

the local data must satisfy the coloured YBE

```text
T^{12}_{a.b,(a*b).c} T^{23}_{a*b,c} T^{12}_{a,b}
=
T^{23}_{a*(b.c),b*c} T^{12}_{a,b.c} T^{23}_{b,c}.
```

Local-minimality means that admissible congruence families `theta_a` are only
all equality or all universal.  Semisplit families, where some colours are
universal and others equality, are a required audit case; they cannot be
discarded by assuming colour transitivity or nondegeneracy.

The semisplit note now states the exact lemma used by the reduction:
semisplit families are a finite subfamily of the same admissible-congruence
condition that defines local-minimality.  Therefore a proved local-minimal
interval has no genuine admissible semisplit family.  The formulation is at
the relation-family level rather than the colour-subset level, so singleton
fibres do not create false semisplit obstructions when equality and universal
partitions coincide.
It also records the equivalent exact Boolean-CSP form: every coloured
crossing contributes the allowed equality/universal bit patterns for
`(source_a, source_b, target_c, target_d)`, and satisfying non-extreme
assignments are exactly the admissible semisplit relation families after
canonicalizing singleton-fibre coincidences.

The local branch router now also has an exact arbitrary-fibre
local-minimality gate, recorded in `proofs/local_minimality_gate.md`.  A
finite local interval is local-minimal iff every distinct pair of points in a
single fibre generates the all-universal admissible congruence family.  Thus
`local_master_bottleneck_summary()` no longer depends on full set-partition
enumeration to route large-fibre intervals: nonlocal-minimal rows are rejected
by a generated pair closure, while product, nondegenerate, and bi-free
verdicts carry exact local-minimality evidence for the finite table under
audit.  The bottleneck summary now exposes the certificate as pair-count,
pair-failure-count, and maximum closure-depth fields, so a proposed local
counterexample must show zero pair failures rather than merely assert
primitive/local-minimal status.
The generated closure certificate now also records first-derivation rows for
each nontrivial unordered relation edge.  Each row records whether the edge
was a seed, a forward transport edge, or an inverse transport edge, together
with the relevant crossing colours and source product pairs.  Hence a
universal pair closure has an inspectable finite derivation of the connected
fibre graphs, while a non-universal closure displays the precise transported
edge set at which local-minimality fails.  This strengthens the auditability
of semisplit and arbitrary-fibre local-minimality gates without changing the
remaining all-`n` Green/corridor theorem burden.

The product branch has the same certificate in product-label language:
`swapped_product_label_pair_closure_audits()` and
`direct_product_label_pair_closure_audits()` close a single fibre pair under
all product labels and inverse labels.  For product normal forms, zero
non-universal closures is exactly primitivity/local-minimality of the coloured
permutation groupoid.  This removes another bounded partition-enumeration
point from the product bottleneck; remaining product work is the all-`n`
longitude-subgroup factorization, not the local-minimality certificate.

### 5. Eliminated branches

The following branches are treated as already eliminated by the user-provided
reduction program and must not be reproved by finite search:

- nondegenerate/guitar;
- fibre size 2 affine over `F_2`;
- two-colour fibre size 3 flip base with no strict primitive nonlinear
  obstruction;
- affine, involutive/permutation, pairwise-linking, bounded
  Magnus/nilpotent, finite semidirect affine, and coboundary branches.

The involutive/permutation item is now expanded in
`proofs/involutive_permutation_detector.md`.  The involutive case is dominated
by the two-point trivial rack because the braid action factors through
`S_n`, so pure braids act trivially.  In permutation form
`R(x,y)=(sigma(y),tau(x))`, the Yang-Baxter equation forces `sigma` and `tau`
to commute; for `h=sigma tau` of order `m`, pure braid motion is
`h^{epsilon(L_j(beta))}` on the `j`-th strand, so the cyclic detector
`C_m` kills the branch through finite Artin-longitude data.  The helper
functions `permutation_solution_maps()` and
`permutation_solution_twist_order()` expose the finite branch data for
audits, and `permutation_solution_pure_longitude_factorization()` checks the
pure-longitude action formula against direct braid action in regression
tests.  The formula is used only after finite longitude identity has forced
the Artin permutation to be trivial.
The executable certificate `known_branch_detector_certificate()` now records
the fixed detector group used by these branches: `G=1` for involutive rows and
`G=C_m` for permutation-form rows, with sharp rack factor sizes `2` and
`2m^2`, respectively.  For rack-type and nondegenerate/guitar rows it records
the direct `Sym(X)` detector from `proofs/direct_symmetric_known_branches.md`.
The local bottleneck summary carries this detector reason and group order, so
a `known_total_branch` verdict is backed by an explicit finite group rather
than only by a branch tag.

## Master theorem closure

The assertion now assembled in
`proofs/master_local_residual_positive_closure.md` is:

> Every local-minimal interval `pi : X -> Z` with `Z` dominated by `Q` has a
> finite group `H = H(pi,Q)`, independent of `n`, such that finite-H
> Artin-longitude equality implies equality of the residual fibre action.

The detector group is the product of the fixed interval-level Green,
Schutzenberger, atom, known-branch, endpoint/unit, and transport-state factors.
The recurrent hidden branch class previously exposed by the Green/corridor
audit is routed by the endpoint factorization, transport-rack, triangular, and
kink-predecessor notes; no residual lower-row obstruction remains after those
symbolic reductions.  A final A answer still requires the proof-critic audit
requested in the project instructions before the goal is marked complete.

The Green audit has now sharpened this obstruction.  For each regular Green
`R`-class of the coordinate-action monoid, the code computes two finite group
layers.  The first is a proved kernel-block action: because coordinate-monoid
`R`-classes refine full-transformation kernel classes, every retained label
induces a permutation on the kernel-block quotient of the class.  The second
is the finite Schutzenberger permutation action of the right stabilizer, along
with a counter for retained edge-germs that are only local to one source.
Exhaustive size-2 and size-3 audits, including local-minimal
congruence-cover intervals, show `0` kernel-action nonpermutation cases, `0`
local-only retained edge-germs, and `0` non-group stabilizer actions.  The
only mixed source atom projections in size `3` are involutive.  This isolates
the next A-route lemma: these finite kernel-block and Schutzenberger groups
should detect all recurrent Green branch choices, while mixed atom projections
should be forced into known finite-G-measurable branches.

The Green atom quotient has now been sharpened one step further.  The helper
`atom_action_summary()` checks whether the completed-row operation
`p(a) triangleright p(q)=p(a^q)` descends from edge-germs to saturated atoms,
and whether the inverse bookkeeping operation
`p(a^q) triangleleft p(q)=p(a)` is likewise well-defined.  This is stronger
than the old fixed-edge branch-choice check because it asks for dependence
only on the two input atoms.  In the size-2 and size-3 exhaustive Green scans
there are `0` atom-action conflict solutions and `0` undefined atom-pair
audits; the size-three affine commutator fixture has a fully defined
`3 x 3` atom operation with no forward or inverse conflicts.  This is still
finite evidence, but it makes the remaining symbolic Green target more
precise: either prove this atom-action descent theoremically in the
local-minimal corridor branch and then factor its unit holonomy through the
fixed Green detector groups, or build B from an explicit normalized-law
failure of this atom layer.
When atom descent is conflict-free and total, the new helper
`atom_quotient_solution()` constructs the finite atom crossing
`(A,Q) |-> (Q,A^Q)`.  The note
`proofs/green_atom_quotient_layer.md` records the conditional theorem that
this atom quotient is a finite right-rack-like YBE layer, hence not itself a
normalized-law obstruction.  In the size-2 and size-3 exhaustive Green scans
there are `0` atom-quotient construction failures, `0` non-YBE atom
quotients, `0` non-right-rack-like atom quotients, and `0` direct rack-law
failures: every constructed atom quotient has bijective right translations
and satisfies right self-distributivity.  The remaining Green
obstruction, if any, must therefore live in section/unit holonomy below this
finite atom rack layer, or else the atom descent theorem must fail in a
larger local-minimal interval.
The descent gap is now represented by an exact closure object.  The helper
`atom_descent_closure_summary(audit)` computes the least coarsening of the
saturated atom partition under forward completed-row action and inverse
bookkeeping stability.  Its proof-side flag `proves_stable_atom_action` is
true exactly when the original atom partition already gives a total
well-defined atom action.  The regenerated Green audit records `0`
descent-closure coarsening solutions and `0` descent-closure failure
solutions in the exhaustive size-2 and size-3 scans; the examples all have
stable depth `0` and add no related pairs.  This does not prove the arbitrary
finite-fibre theorem, but it turns any future descent failure into a concrete
finite coarsening obstruction that must either be absorbed by a quotient
branch or upgraded to a normalized-law B sequence.
The new helper `atom_descent_quotient_rack_audit()` audits the absorption
side explicitly: after passing to the least descent-closed coarsening, it
checks whether the resulting atom quotient is a total right-rack-like YBE
layer.  A coarsening that still is not total remains an obstruction object;
a coarsening whose closed quotient is a rack layer pushes the remaining proof
burden down to endpoint/unit holonomy below that quotient.
The follow-up criterion `proofs/green_atom_rack_lift_criterion.md` packages
this into a local detector target.  It constructs the atom inner group
`G_A`, implemented by `atom_quotient_inner_group(audit)`, and states that a
branch is killed by the single finite product
`G_A x U(M_1) x ... x U(M_r)` once the lower endpoint units lie in the
corresponding product longitude-value subgroup.  For the size-three affine
commutator fixture, the atom quotient inner group has order `6`.  Thus the
remaining all-`n` Green proof can now be stated as: prove atom descent and
prove endpoint-unit subgroup membership below the atom rack layer.

These Green factors are now exposed as actual finite groups, not only as
summary counts.  `schutzenberger_action_groups()` returns the finite
Schutzenberger permutation groups, `atom_quotient_inner_groups()` returns the
finite inner groups of proved atom-rack quotient layers, and
`two_sided_green_detector_groups()` returns the left/right Schutzenberger
factors, full symmetric kernel-block factors, and left/right atom-quotient
inner groups with duplicate concrete group tables removed.
`two_sided_green_detector_product()` multiplies them into one finite group.
For the size-three affine commutator fixture the factor orders are `2`, `3`,
and `6`, giving a product detector of order `36`; the order-`6` atom inner
group is already represented by the full symmetric kernel-block factor and is
deduplicated.  This is still a candidate detector, not the missing all-`n`
Green residual proof.

The local-minimal Green audit now cross-tabs the Green hidden-loop data with
the output coordinate-kernel corridor closure.  In the size-2 local-minimal
cover corpus, the single universal-output interval is the involutive
identity-table interval and is the only universal-output hidden atom-trivial
loop.  In the size-3 local-minimal cover corpus, the `12` universal-output
intervals account for all `12` depth-2 hidden atom-trivial loop intervals,
the `3` hidden bijective loop intervals, and the `6` mixed source
atom-projection intervals; all `12` are involutive, and `6` are identity-table
tagged.  There are `0` untagged universal-output intervals in this Green
cross-tab.  This is finite evidence only, but it exposes the symbolic bridge
now needed: universal coordinate-kernel corridors must either force the Green
hidden-loop phenomenon into a known finite-G-measurable branch, or the
two-sided symmetric kernel-block and Schutzenberger groups must detect the
remaining corridor holonomy.

A further kernel detector audit rules out the smaller shortcut of using only
the actual kernel-action image group.  The size-3 affine commutator candidate
has actual kernel group `C_3`, which is blind to the commutator law braid even
though the braid moves `(0,0,1)` to `(1,1,2)`.  The full symmetric group on
the same three kernel blocks, `S_3`, detects that commutator.  Exhaustive
size-3 raw and local-minimal interval scans find `12` commutator movers; `9`
are blind to their actual kernel-action groups, but `0` are blind to the full
symmetric kernel-block groups.  Thus the viable detector candidate uses full
symmetric kernel-block groups, not merely the image subgroups.

The same audit now includes a bounded residual scan on all `161` braid words
on `3` strands of length at most `4`.  In the size-3 raw and local-minimal
interval scans, actual kernel-action groups have `15` blind residual movers,
but full symmetric kernel-block groups have `0`.  This is finite evidence
only, but it focuses the remaining proof obligation on the symmetric
kernel-block detector rather than the smaller image subgroup.

The audit also checks the bounded full-form implication: among the same
base-fixed words, no two words with the same symmetric kernel-block
finite-group longitude signature have different residual actions in the
size-2 or size-3 raw scans, nor in the corresponding local-minimal interval
scans.  This collision check is the bounded analogue of the sharp obstruction
theorem's equality form.

The exact finite-image diagnostic for the same detector has also been
strengthened.  For a fixed braid index `n`, it closes the finite joint image
of the braid group in the base action, the symmetric kernel-block
finite-group detector states, and the residual action.  A nontruncated run
with no kernel or collision failure is therefore an exact fixed-`n` proof of
the sharp detector implication for that diagnostic, not a bounded word scan.
For the size-3 affine commutator candidate, the `n=2` image closes with `12`
joint states, `12` detector states, and `3` residual states, with no failure.
At `n=3`, the same closure reaches the configured cap of `1000` states; this
truncated row is recorded only as a state-growth warning.

The Green detector candidate has also been made two-sided.  Applying the
Green audit to the side-opposite solution `R^op=P R P` turns the
right-coordinate maps `rho_x(y)=pr_2 R(y,x)` into first-coordinate maps, and
the YBE gives the dual relation `rho_y rho_x = rho_v rho_u` whenever
`R(x,y)=(u,v)`.  Thus the finite symmetric kernel-block group candidate now
includes both the left Green classes of `X` and the right Green classes of
`X^op`, with duplicate finite groups removed.  This group is still finite and
independent of `n`; it does not close the master theorem, but it removes a
left/right asymmetry from the proposed detector.

The side-opposite closure is now theorem-level, not only a Green audit
symmetry.  The strand-reversal automorphism `rev_n(sigma_i)=sigma_{n-i}`
and tuple reversal `J_n` satisfy
`rho_{X^op,n}(beta)=J_n rho_{X,n}(rev_n(beta)) J_n`, while finite-`G`
longitude identity is invariant under `rev_n`.  Hence any finite group that
detects `X` also detects `X^op`, with the same rack `A_G`.  This is recorded
in `proofs/opposite_detectability_closure.md`.

The finite-semigroup holonomy route now adds one symbolic guardrail to this
Green/corridor program.  In a finite aperiodic transformation monoid, every
permutation element is the identity: if `p` is a permutation and
`p^N=p^(N+1)`, cancellation in the finite cyclic group generated by `p` gives
`p=1`.  Since every residual map `delta_{n,z}(beta)` is a permutation of the
finite fibre block `X_z`, a purely aperiodic reset component cannot remain as
nontrivial residual motion once the group holonomy coordinates are killed.
Thus the remaining A-route is to prove that all local residual branch choices
factor, uniformly in `n`, through fixed finite holonomy groups plus aperiodic
transition data.  A genuine B route must instead exhibit moving group
holonomy that escapes every fixed finite detector; a purely aperiodic branch
cannot be the final obstruction.  The note is recorded in
`proofs/finite_semigroup_holonomy_route.md` and executable guardrails are in
`src/ybe_domination/semigroup_holonomy.py`, including extraction of the
finite permutation subgroup `monoid_permutation_group(M)` of a transition
monoid.

The Green/corridor observer now has the same group-vs-reset separation at
finite depth.  The helper
`bounded_atom_trivial_loop_group_summaries(audit,d)` extracts the finite
permutation groups generated by total bijective atom-trivial completed-context
loops, ignoring atom-trivial maps that collapse or partially forget context
words.  This is recorded in
`proofs/green_holonomy_factorization_gate.md`.  It sharpens both routes:
an A proof must factor these group-like loops through the fixed
Green/Schutzenberger detector product uniformly in `n`, while a B proof must
produce a normalized-law escape in this group-like part rather than citing
raw reset-like context collapse.

The corridor detector factor list is now explicitly tied back to a single
finite detector group.  The helper
`bifree_corridor_product_subgroup_audit()` compares the listed two-sided Green
and Schutzenberger factors with their direct product and checks
`V_beta(product_i H_i)=product_i V_beta(H_i)` when the product is small enough
to enumerate.  This is a finite guardrail only; the theorem-level step remains
the symbolic product lemma in `proofs/longitude_subgroup_products.md`.  Its
value for the final audit is that a factorwise corridor proof still constructs
one finite `H(pi,Q)`, independent of `n`, rather than a changing family of
detectors.

The semigroup bridge now has a matching longitude subgroup gate, recorded in
`proofs/unit_holonomy_longitude_gate.md`.  For a finite transformation monoid
`M`, the permutation elements form a finite unit group `U(M)`.  The helper
`unit_longitude_subgroup_audit(monoid,n,beta,labels)` computes the subgroup
`V_beta(U(M))` generated by all recursive Artin-longitude values in that unit
group and reports nonunit labels separately.  Thus a future Green/corridor A
proof can reduce a group-like semigroup label to the fixed finite group
`U(M)` by proving membership in `V_beta(U(M))`; a future B proof must realize
normalized-law escape in the unit group rather than relying on non-bijective
observer collapse.

The companion unit-factorization gate is recorded in
`proofs/unit_factorization_gate.md`.  For total maps of a finite set, a product
can be a permutation only if every factor is a permutation.  The executable
helpers `compose_transformation_word(...)` and `unit_factorization_audit(...)`
therefore rule out one tempting false obstruction: nonunit or reset-like
labels cannot hide inside a longer word whose final effect is the residual
permutation moved by a braid.  Any genuine B obstruction through this
semigroup channel must already be group-like, hence belongs in the finite
unit group audit above.

The new unit-section detection criterion combines these two gates into the
exact finite-group implication needed by a future corridor proof.  It is
recorded in `proofs/unit_section_detection_criterion.md` and implemented as
`unit_section_detection_audit(monoid,n,beta,factors)`.  The criterion says:
if a residual branch word is represented in one fixed finite transformation
monoid, its composite is a permutation, and its unit section labels lie in
`V_beta(U(M))`, then identity finite-`U(M)` longitude data kills the branch.
Therefore the remaining A obligation is not merely to extract finite
semigroup states, but to prove an all-`n` residual section factorization with
unit labels in this fixed longitude-value subgroup.

The endpoint version is recorded in
`proofs/unit_composite_longitude_criterion.md` and implemented as
`unit_composite_detection_audit(monoid,n,beta,factors)`.  It weakens the
section requirement: after a word in the fixed monoid telescopes, it is enough
for the final residual unit/composite to lie in `V_beta(U(M))`.  Individual
unit section labels may sit outside the subgroup if they cancel in the
endpoint.  This is the more flexible A target for Green, Schutzenberger, and
product-label transports, and it sharpens B: an obstruction must move through
a nonidentity endpoint unit outside the finite longitude-value subgroup, not
merely through an intermediate label outside it.
The endpoint-unit dichotomy note now makes this fork explicit.  A nonidentity
endpoint at identity finite-unit longitude data is only a finite detector
failure flag; it becomes B only after a normalized-law diagonalization
defeating every finite group.  Conversely, endpoint membership in the product
longitude-value subgroup is exactly the A-side condition for that semigroup
branch.

The bi-free corridor endpoint factorization note
`proofs/bifree_corridor_endpoint_factorization.md` now packages this endpoint
logic at the final corridor level.  It proves the algebraic implication:
factorwise endpoint-longitude expressions in the fixed groups of `H(pi,Q)`
assemble into one product-detector witness, and identity
`Lambda_{H(pi,Q),n}` kills the corresponding faithful residual readout.  Thus
the remaining corridor theorem has been narrowed to the endpoint
longitudinalization lemma: every group-like atom-trivial Green/corridor
completed-context endpoint must be displayed as a finite product of recursive
Artin-longitude evaluations in fixed factors of `H(pi,Q)`, uniformly in braid
index.  This note is an A-side assembly lemma, not a proof that the endpoint
expressions always exist.
The corresponding group-only executable layer is now
`endpoint_longitude_expression_audit(...)` and
`endpoint_product_longitude_expression_audit(...)` in
`src/ybe_domination/endpoint_factorization.py`.  These helpers take endpoint
elements in fixed finite groups, displayed longitude expressions, and
input-dependent assignments, then construct the literal direct-product witness
in `V_beta(product_s H_s)`.  This is the code-level form of the endpoint
assembly lemma for Green kernel-block, Schutzenberger, atom-inner, quotient,
and endpoint/unit factors.
The same module now records the faithful-readout clause through
`endpoint_coordinate_readout_audit(...)` and
`endpoint_residual_readout_audit(...)`: an identity endpoint tuple must fix the
corresponding residual coordinate, and coordinate rows bundle into a
residual-tuple implication.  This closes the executable shape of the
endpoint-factorization proposition while leaving the uniform construction of
the endpoint expressions as the open theorem.
The row bundle helper `endpoint_residual_action_audit(...)` now records the
fixed-braid residual-action implication for supplied rows.  It checks
braid-data consistency, endpoint-controlled killing of all supplied rows, and
an optional expected row count.  This keeps a finite readout table honest:
passing supplied rows is not confused with the missing all-`n` proof that such
rows cover every residual input.
The Artin-defect longitudinalization sieve
`proofs/artin_defect_longitudinalization_sieve.md` sharpens the remaining
endpoint target.  For `beta in B_n`, set
`D_beta=<<L_1(beta),...,L_n(beta)>>` in `F_n`.  The note proves that every
Artin permutation defect `beta(w)p_beta(w)^-1` lies in `D_beta`, and that every
finite-group value of any element of `D_beta` lies in `V_beta(G)` after
absorbing normal conjugators into input-dependent assignments.  Therefore a
display

```text
h_e(beta,z,x) =
  product_m phi_m(beta(w_m)p_beta(w_m)^-1)^{epsilon_m}
```

inside one fixed detector factor `H_s` is a certificate that
`h_e(beta,z,x) in V_beta(H_s)`.  The code now verifies supplied displays with
`artin_permutation_defect_witness_audit(...)`,
`endpoint_artin_defect_audit(...)`, and
`endpoint_product_artin_defect_audit(...)`.  This does not solve the local
theorem; it reduces the missing corridor statement to proving such
Artin-defect displays for the elementary Green kernel-block, Schutzenberger,
atom-inner, and endpoint-unit generators in fixed factors of `H(pi,Q)`.
The detector-lift criterion
`proofs/artin_detector_lift_criterion.md` proves the corresponding
unbounded braid-recursion step.  For a fixed finite group factor `U`, if an
endpoint observer carries live-strand pairs `(m_k,u_k)` and its positive and
negative crossing rows are exactly

```text
(m_i,u_i),(m_j,u_j)
  -> (m_i m_j m_i^-1, m_i u_j),(m_i,u_i)
```

and

```text
(m_i,u_i),(m_j,u_j)
  -> (m_j,u_j),(m_j^-1 m_i m_j, m_j^-1 u_i),
```

then induction gives `u_k(beta)=phi(L_k(beta))` for the initial meridian
assignment `phi(x_k)=m_k(1)`.  Thus any signed product of terminal `u`-labels
is a literal endpoint-longitude expression in `U`.  The code now exposes
`artin_detector_lift_transition_audit(...)` for the finite local row check and
`artin_detector_lift_braid_audit(...)` for the global recursion convention.
This shifts the remaining A-route burden to verifying these finite row
identities for each Green/corridor observer row in the fixed factors of
`H(pi,Q)`.
The atom-inner rack-layer portion of that burden is now closed conditionally
on atom descent and totality.  The note
`proofs/atom_inner_detector_lift_rows.md` proves that for a finite rack layer
`R(a,b)=(a*b,a)`, the inner translations satisfy
`L_{a*b}=L_a L_b L_a^-1`, so the positive Artin detector row holds in
`Inn(A)`.  Endpoint labels update by `u_i'=L_a u_{i+1}` and
`u_{i+1}'=u_i`, and the negative row is the inverse positive row.  Applying
this to the side-opposite of the right-rack-like Green atom quotient shows
that `Inn(atom quotient)` is no longer an open detector-lift row factor once
the atom action descends and is total.  The code exposes this as
`rack_inner_detector_lift_audit(...)`,
`right_rack_inner_detector_lift_audit(...)`, and
`atom_quotient_inner_detector_lift_audit(...)`.  The remaining row checks are
Green kernel-block factors, Schutzenberger factors, and lower endpoint/unit
holonomy factors.
The Green kernel-block and Schutzenberger row checks have now been reduced to
a single first-output defect endpoint.  The note
`proofs/green_first_output_defect_criterion.md` proves that for every
group-valued Green observer row,

```text
d_C(a,q)=g(q^a)g(q)^-1
```

determines the whole row: `g(q^a)=d_C(a,q)g(q)` and
`g(a^q)=g(q)^-1 d_C(a,q)^-1 g(a)g(q)`.  Thus there is no independent
second-output obstruction.  If the defect is identity, the row is exactly the
side-opposite Artin detector row.  When retained edges are globally realized
in the Schutzenberger action, kernel-block defects are homomorphic images of
Schutzenberger defects; this is exposed by
`schutzenberger_kernel_defect_pushforward_audits(...)`.  The remaining Green
theorem has now been sharpened by
`proofs/green_defect_kernel_quotient_detection.md`.  For each observer
`U_C`, let `Def_C` be the normal closure of the first-output defects.  In the
finite quotient `U_C/Def_C`, every row is the exact side-opposite rack-Artin
row, so the detector-lift theorem kills the quotient motion.  The follow-up
`proofs/green_defect_potential_coboundary.md` proves that each elementary
defect in `Def_C` is a nonabelian coboundary `eta(q^a)eta(q)^-1` for a
basepoint-normalized potential on the retained edge-germ graph.  This made
the intermediate Green theorem the principalness of that finite potential,
equivalently that the transported defect-kernel endpoint `D_C(beta)` lies in
`V_beta(Def_C)` uniformly in braid index.  The balanced gauge refinement
below now pushes the raw row-defect target into terminal gauge holonomy.
The stronger elementary Artin-defect display route is now explicitly blocked
in general by `proofs/artin_defect_abelianization_barrier.md`: Artin
permutation defect values always land in the commutator subgroup of the
target, while the affine Green stress row has abelian defect kernel `C3` and
nonidentity elementary defects.  Therefore a valid A proof must use full
recursive-longitude membership in `V_beta(Def_C)`, endpoint cancellation of
the abelianized potential transport, or a detector-lift construction for the
potential labels.
The next split is now explicit in
`proofs/green_defect_abelianization_split.md`: the abelian defect target is
`Def_C/[Def_C,Def_C]` and must be handled by ordinary finite abelian
longitude data; only after killing that layer may the remaining commutator
endpoint be attacked by Artin-defect displays or commutator-level
detector-lift arguments.
The ordinary finite abelian target is now exact:
`proofs/abelian_longitude_image_criterion.md` proves that, for a finite
abelian group `A`, `V_beta(A)` is the subgroup generated by `a^{m_ij}` for
all `a in A` and all entries `m_ij` of the abelianized recursive-longitude
matrix.  Thus the projected `AbDef_C` endpoint must be shown to lie in this
matrix subgroup, or to cancel under the residual hypotheses, before the
commutator endpoint is considered.
The raw Green/Schutzenberger row obstruction has now been compressed further
by `proofs/green_balanced_defect_gauge_decomposition.md`.  For a row with
labels `A=g(a)`, `Q=g(q)`, `B=g(q^a)`, and `C=g(a^q)`, the first-output
defect satisfies

```text
B Q^-1 = [A,Q] Q(CA^-1)^-1 Q^-1.
```

The commutator `[A,Q]` is a local Artin permutation defect value and is
therefore already longitude-visible.  Since `V_beta(U)` is normal in every
finite target group `U`, the conjugation around the second factor is harmless.
Thus the genuine remaining Green/Schutzenberger burden is terminal
second-output gauge holonomy `CA^-1`, not an independent first-output defect
endpoint.
The certificate target for this burden is now recorded in
`proofs/terminal_gauge_longitudinalization_criterion.md`.  Along one strand
or chart, labels `g_0,...,g_t` have gauge increments
`s_k=g_k g_{k-1}^-1`, and the newest-on-left product telescopes:

```text
s_t ... s_1 = g_t g_0^-1.
```

The terminal endpoint can then be killed by the same endpoint certificates
already used elsewhere: recursive-longitude expressions, literal subgroup
witnesses, Artin-defect displays, or abelian matrix witnesses in fixed gauge
factors.  The executable helpers
`terminal_gauge_telescoping_audit(...)`,
`terminal_gauge_longitude_expression_audit(...)`, and
`terminal_gauge_product_longitude_expression_audit(...)` record the single
factor and product-detector forms.
The principal lower endpoint/unit subcase is now closed in
`proofs/principal_gauge_extension_detector.md`.  If the surviving gauge row
has principal form

```text
(a,r)*(b,s) = (a*b, c(a,b)s),
```

then projecting the local YBE to the unit coordinate gives the nonabelian
rack-cocycle identity

```text
c(a,b*d)c(b,d)=c(a*b,a*d)c(a,d).
```

Thus `A x U` is a finite rack and the fixed group `Inn(A x U)` supplies the
Artin detector-lift rows for this principal terminal gauge.  The current
sharp structural burden is principal-gauge normal form for every surviving
endpoint/unit holonomy row; a failure would be an explicit nonprincipal row
that still needs a normalized-law sequence to become outcome B.
The transport-state refinement in
`proofs/transport_state_rackification_detector.md` removes the principal
restriction for genuine strand-continuing gauge.  If the lower row has form

```text
((a,r),(b,s)) -> ((a*b,F_{a,b,r}(s)),(a,r)),
```

then the finite state `A x E` itself is the rack state whenever the completed
row is bijective YBE.  The fixed detector is `Inn(A x E)`, and the executable
hooks `transport_state_rackification_audit(...)` and
`rack_extension_detector_audit(...)` record the corresponding finite
inner-group detector.  The current bottleneck is therefore descent
separation: prove that any non-strand-continuing lower motion is already
visible in Green kernel-block or Schutzenberger readouts, with no residual
motion left outside the fixed factors.
The continuation-congruence gate
`proofs/continuation_congruence_descent_gate.md` now isolates the finite
local-minimality dichotomy behind that statement.  For a rack-base local row
`T_{a,b}(x,y)=(u,v)`, seed the relation `x~v` whenever `v != x`, and close it
to the least admissible family `Theta^cont`.  Equality gives the
strand-continuing row already handled by transport-state rackification.
Proper mixed closure is a local-minimality failure.  In a genuine
local-minimal interval, every nontrivial continuation closure is therefore
all-universal.  The current sharp bottleneck is universal continuation
visibility: prove that this universal continuation corridor is exactly the
fixed Green/Schutzenberger-visible motion, or extract the normalized-law B
sequence from it.
The elementary continuation closure note
`proofs/elementary_continuation_closure.md` sharpens this once more.  A
local-minimal interval cannot have a universal continuation corridor generated
only collectively by many seeds: every individual nontrivial continuation seed
pair has universal closure.  The helpers
`continuation_seed_pair_closure_audits(...)` and
`continuation_seed_pair_closure_failures(...)` expose this seed-level gate.
The universal-continuation derivation certificate
`proofs/universal_continuation_derivation_certificate.md` now records the
edge-by-edge derivation ledger for each universal seed closure.  The helper
`continuation_seed_universal_derivation_audits(...)` compares the universal
edge count with the recorded derivation rows, including positive-depth
transport edges.  Thus the final descent-separation target is not only
seed-by-seed but derived-edge-by-derived-edge.
The readout-propagation criterion
`proofs/continuation_readout_propagation.md` now compresses the
derived-edge target once a fixed readout relation is proposed.  An admissible
readout containing the representative seed must contain the entire generated
seed closure by the universal property of the least admissible congruence.
The helper `continuation_seed_readout_propagation_audits(...)` records the
admissibility, seed containment, generated containment, and any missing
generated edges.
The readout-kernel admissibility criterion
`proofs/readout_kernel_admissibility.md` now supplies the executable way to
check the admissibility input for finite detector labels.  The helper
`readout_kernel_audit(...)` takes fibrewise labels, forms their kernel
partition family, and applies the exact local transport test, recording the
first failed row if the labels are not a valid local quotient.
The readout descent-separation certificate
`proofs/readout_descent_separation_certificate.md` now combines the readout
kernel and seed-propagation checks.  The helper
`readout_descent_separation_audit(...)` records any continuation seed rows
that survive in the readout quotient; if none survive and the base row is in
rack-side form, the quotient lower row is strand-continuing.
The readout-kernel quotient interval note
`proofs/readout_kernel_quotient_interval.md` now constructs that quotient row
explicitly.  The helper `quotient_interval_by_family(...)` quotients any
admissible fibre congruence, while `readout_kernel_quotient_interval(...)`
specializes this to detector labels.  The descent-separation audit stores the
quotient interval and its own continuation audit when the kernel is admissible.
The product readout-kernel assembly note
`proofs/product_readout_kernel_assembly.md` now records the local analogue of
finite detector product assembly.  The helper `product_readout_kernel_audit(...)`
bundles finitely many factor labels into one tuple-valued readout, checks that
its kernel is the meet of the factor kernels, and certifies the product step
when all factor kernels are admissible.
The product descent-separation note
`proofs/product_readout_descent_separation.md` adds the corresponding
continuation-seed ledger.  Since the product kernel is a meet, a continuation
seed survives the product quotient if and only if it survives at least one
factor quotient.  The helper `product_readout_descent_separation_audit(...)`
therefore records factor seed survival, product seed survival, and the product
descent-separation certificate in one object.
The readout seed-saturation note `proofs/readout_seed_saturation.md` records
the minimal admissible coarsening forced by one factor readout together with
all continuation seeds.  The helper `readout_seed_saturation_audit(...)`
constructs the saturated block labels and re-runs descent separation on them.
For a local-minimal interval, this exposes the dichotomy that an admissible
equality factor either already kills the seeds or saturates to universal.
The local-minimal seed-saturation dichotomy note
`proofs/local_minimal_seed_saturation_dichotomy.md` now makes that dichotomy
an explicit certificate.  The helper
`local_minimal_seed_saturation_dichotomy_audit(...)` verifies the
equality/universal saturation expectation and marks forced universal collapse
as an external-routing obligation rather than a proof of faithful detection.
The lost-edge external routing note `proofs/lost_edge_external_routing.md`
records that obligation as a finite edge ledger.  The helper
`lost_edge_external_routing_audit(...)` takes descent labels and separate
external routing labels, then lists the saturation edges that are lost,
routed, or still unrouted.  These routing labels are not fed back into the
descent quotient; their all-`n` recursive-longitude visibility remains a
separate endpoint-factorization obligation.
The routed lost-edge endpoint witness note
`proofs/routed_lost_edge_endpoint_witness.md` connects that ledger to the
endpoint certificate layer.  The helper
`routed_lost_edge_endpoint_witness_audit(...)` requires each routed edge to
come with a product endpoint-longitude expression audit in fixed detector
factors, reports missing routed edges and extra witness edges, and passes only
when the routing ledger itself is valid.  This is still not an A proof: it is
the precise fixed-factor obligation for the externally routed lost
information.
The chart-transport collapse in
`proofs/chart_transport_collapse.md` removes chart-dependent copies from the
generator burden.  Since `V_beta(G)` is already normal in every finite group,
a representative elementary-generator witness gives witnesses for all finite
chart conjugates; `conjugate_longitude_subgroup_witness(...)` records the
certificate-level operation.  At this point the final A-route theorem was
stated in
`proofs/descent_separation_transport_rack_closure.md`: transport-rack closure
was proved, while descent separation remained to be routed.  The subsequent
unit-continuation, two-sided unit, mixed-unit, triangular, kink-predecessor,
and master-local positive-closure notes record that route and should be read
as superseding this intermediate open-target statement.
The final constant-observer universal-continuation corridor has now been
split by `proofs/unit_continuation_final_obstruction.md`.  In the case
`Theta^cont=Nabla` and `K^O=Nabla`, every certified observer is fibrewise
constant, but any completed-context continuation branch that actually
contributes to `delta_{n,z}(beta)` has a permutation composite.  The
unit-factorization lemma then forces every transition factor in that branch
to be a unit/permutation; nonunit or reset-like continuation labels cannot be
the moving residual obstruction.  The then-remaining unit endpoint
`S_beta in U(M_cont)` is routed by the later lower-row classification:
strand-continuing rows rackify, two-sided unit rows are nondegenerate, hidden
mixed-unit rows reduce to triangular rows, and the final Latin triangular
case collapses by one-colour and kink-predecessor cancellation.
The two-sided unit-collapse note `proofs/two_sided_unit_collapse.md` then
splits the remaining lower row by coordinate-section type.  A row whose left
and right coordinate sections are all bijections is locally nondegenerate and
is routed to the already closed nondegenerate/guitar branch; a
strand-continuing row is already closed by transport-state rackification.
Therefore the only continuation shape still capable of carrying the final
obstruction is mixed-unit context recovery, where one-sided nonunit local
information is lost and later recovered by the surrounding context.  The
helper `two_sided_unit_collapse_audit(...)` records this row split exactly.
The companion-separation refinement
`proofs/mixed_unit_companion_separation.md` identifies the exact finite edges
inside that mixed case.  Since each local row is a bijection, a collision in
one coordinate section is necessarily separated by the companion output
coordinate.  The helper `section_kernel_companion_audit(...)` records left
and right section-kernel collisions together with the companion outputs that
recover the distinction.  The remaining obstruction is therefore a
companion-shuttle cycle that escapes the fixed readouts, not an isolated
nonunit section.
The rank-profile collapse note
`proofs/rank_profile_collapse_mixed_unit.md` now removes proper rank-loss as
a hidden obstruction.  A proper nontrivial section-kernel profile is visible
to the Green/Schutzenberger kernel-block readouts; under `K^O=Nabla`, the
only remaining hidden rank-losing section has universal kernel and is
constant.  The helper `section_rank_profile_collapse_audit(...)` records the
rank, kernel blocks, kernel kind, image, and injective non-surjective side
cases.  The final continuation seed is therefore constant-section triangular
context recovery.
The triangular bundle partition note
`proofs/constant_section_triangular_bundle_partition.md` then records the
finite structure forced by bijectivity.  In a row
`T(x,y)=(alpha(x), beta_x(y))`, the constant map `alpha` is surjective, every
companion section `beta_x` is injective, and the images over each fibre
`alpha^{-1}(u)` partition the companion codomain.  The helper
`triangular_bundle_audit(...)` records these constant-map fibres, companion
image blocks, and nontrivial bundle fibres.  The final obstruction is now
triangular bundle holonomy.
The inverse formula note `proofs/triangular_bundle_recovery_inverse.md`
splits that holonomy into block-label recovery plus within-block companion
inverse.  For an output `(u,v)`, the bundle partition recovers the unique
`x=r_u(v)` whose block contains `v`, and then recovers
`y=beta_x^{-1}(v)`.  The helper `triangular_recovery_audit(...)` records the
inverse table and flags missing or ambiguous outputs.  Thus the remaining
triangular obstruction is recovery holonomy in finite block labels and
within-block coordinates.
The constant-column collapse note
`proofs/constant_column_collapse_triangular.md` removes the non-Latin half of
that remaining triangular obstruction.  If an opposite column
`C_y(x)=beta_x(y)` is non-bijective while hidden from the fixed observers,
then proper-kernel visibility forces it to be constant.  Once one opposite
column is constant, bijectivity of every companion map `beta_x` forces all
opposite columns to be constant, so the row is product/permutation holonomy.
The helper `triangular_column_collapse_audit(...)` records product-collapse
rows, proper opposite-kernel rows, and the rows that remain genuinely
Latin-unit triangular.  The final triangular theorem target is now: every
residual Latin-unit triangular endpoint lies in `V_beta(U_triangle)` for the
fixed group generated by the triangular unit transports.
The Latin triangular YBE split note `proofs/latin_triangular_ybe_split.md`
then removes alpha transport from that final target.  In left triangular
normal form, the first coordinate of the coloured YBE is exactly
`alpha_{a.b,(a*b).c} alpha_{a,b}=alpha_{a,b.c}`, so the alpha maps form a
finite product/permutation cocycle and route to the closed product holonomy
branch.  The helper `latin_triangular_ybe_audit(...)` records this alpha
cocycle plus the middle-companion and endpoint-shear equations.  The remaining
triangular theorem target is companion-shear longitude visibility in a fixed
finite group `U_shear`; a counterexample seed must survive there, not in alpha
transport.
The one-colour collapse note
`proofs/one_colour_latin_triangular_collapse.md` rules out the simplest shear
seed.  In one colour, the alpha equation gives `alpha^2=alpha`, so bijectivity
forces `alpha=id`; the middle equation then forces all companion maps
`beta_x` to be identities.  Opposite columns are constant, so no nontrivial
one-colour Latin-unit triangular YBE row exists.  The helper
`one_color_latin_triangular_collapse_audit(...)` records this product-collapse
route and the failure of the non-YBE Latin shear example.  Any remaining
companion-shear obstruction must use genuinely multi-colour transport.
The kink-predecessor cancellation note
`proofs/kink_predecessor_latin_triangular_cancellation.md` removes the
rack-base multi-colour shear obstruction.  In a rack base,
`L_{kappa(b)}=L_b`; for `c=kappa^{-1}(b)` this gives `b*c=b`, while the alpha
cocycle gives `alpha_{b,c}=id`.  Substituting this into the third-output shear
equation forces the predecessor column `y -> y circ_{b,c} z` to be constant.
Latin-unit says the same map is bijective, so `|X_b|=1`.  The helper
`rack_kink_latin_triangular_collapse_audit(...)` records the rack-form base,
kink predecessors, alpha identities, and predecessor-column constancy.  Thus,
conditional on the preceding reductions in this branch, the final lower-row
obstruction in the bi-free universal-corridor case is eliminated.
The follow-up note `proofs/unit_continuation_abelian_kernel_lift.md` now
splits that last endpoint condition through abelianization.  For the finite
unit group `U`, let `C=[U,U]` and `q:U->U/C`.  A quotient witness for
`q(S_beta)`, a lifted witness in `U`, and a kernel witness for
`S_beta*v_beta^-1` using only assignments into `C` together prove
`S_beta in V_beta(U)`.  The helper
`normal_quotient_longitude_lift_audit(...)` records the quotient value, lifted
value, kernel correction, kernel-assignment check, and combined witness.  Thus
the final unit-continuation theorem now separates into an abelian matrix
endpoint problem plus a commutator-kernel correction problem.
The derived-series note
`proofs/unit_continuation_derived_series_reduction.md` iterates this
abelian-kernel split through `U^(r+1)=[U^(r),U^(r)]`.  If the derived series
terminates at the identity, the unit endpoint is reduced to finitely many
abelian matrix-longitude witnesses.  If it stabilizes at a nontrivial perfect
residual, that residual endpoint is the only remaining nonabelian unit
obstruction in this reduction.  The executable helpers
`derived_series_audit(...)` and `subgroup_as_group(...)` expose the fixed
finite stages.
The single-endpoint route audit
`unit_composite_longitude_route_audit(monoid,n,beta,factors)` now records the
same ladder used in product-label work: endpoint identity, one evaluated
recursive-longitude witness, and membership in the full subgroup
`V_beta(U(M))`.  The subgroup condition is the theorem-level route.  Lack of
a single witness is harmless if subgroup membership holds; only subgroup
failure is a serious fixed-word B warning.
The new expression certificate
`proofs/endpoint_longitude_expression_certificate.md`, implemented by
`evaluate_longitude_expression(...)` and
`unit_composite_longitude_expression_audit(...)`, gives the non-enumerative
proof-side version of this route.  It verifies that an endpoint unit is a
displayed word in evaluated recursive longitudes for one assignment into the
fixed unit group.  Such an expression proves endpoint membership in
`V_beta(U(M))` directly, so a future all-`n` corridor proof can produce
input-dependent assignments and expressions instead of enumerating
longitude-value subgroups.  The product helper
`unit_composite_product_longitude_expression_audit(...)` now packages a
finite list of such endpoint expressions into one certificate in
`prod_i U(M_i)`.  It now also constructs the literal product subgroup witness:
each letter supplies a product-group assignment, a longitude index, and a
sign, and different letters may use different assignments.  Thus the product
endpoint membership is displayed as an actual word in
`V_beta(prod_i U(M_i))`, not inferred from enumeration of the product
subgroup.

The product version is recorded in
`proofs/unit_section_product_detector.md` and implemented as
`unit_section_product_detection_audit(monoids,n,beta,factor_words)` for the
strong section version and
`unit_composite_product_detection_audit(monoids,n,beta,factor_words)` for the
weaker endpoint version.  Both use the direct-product longitude lemma to
combine finitely many fixed unit groups `U(M_i)` into the one group
`prod_i U(M_i)` required by the sharp obstruction theorem.  This is now an
explicit audit gate for Green/corridor proofs: named unit factors are allowed
for readability, but the final detector must be one finite product group
attached to the interval and quotient, not to `n`.  When transports telescope,
the endpoint-product audit is the correct executable target.  It now records
the actual endpoint tuple `(h_i(beta))_i` in `prod_i U(M_i)` and, when the
product subgroup is enumerated, whether that tuple lies in
`V_beta(prod_i U(M_i))`.  The audit now exposes this direct product-endpoint
criterion separately as
`product_endpoint_lies_in_product_longitude_subgroup` and
`identity_longitudes_kill_product_endpoint`, so a future corridor proof can
cite endpoint membership in the one product group itself rather than only the
factorwise display.

The structure-monoid viewpoint has also been isolated.  For
`M_X=<X | xy=uv when R(x,y)=(u,v)>`, the degree-`n` structure congruence is
exactly the `B_n`-orbit relation on `X^n`, because each adjacent defining
rewrite is one braid generator and bijectivity supplies the inverse rewrite.
Thus neither A nor B can be settled by product invariants alone.  A proof
must kill all holonomy inside these finite structure orbits uniformly in `n`;
a counterexample must move a tuple inside one such orbit while remaining
invisible to every fixed finite-group longitude detector.

The structure-orbit obstruction has now been made orbit-local.  For fixed
`n`, `structure_orbit_holonomy_summary(X,n)` computes the finite
braid-action group on each degree-`n` structure orbit separately, including
group sizes and exponents when the orbit group closes under the configured
diagnostic cap.  The companion helper
`structure_orbit_factorization_summary(X,n)` computes the global fixed-degree
braid image and compares its projections with those orbit factors.  In the
size-3 affine commutator diagnostic, the orbit profiles match the dihedral
quandle through the audited range: at `n=4` the large orbit groups have sizes
`216`, `648`, and `648`, with exponents `12`, `36`, and `36`, while the
global image has size `648` and exponent `36` rather than the full product
`90699264`; at `n=5` the three large orbit closures exceed the cap.  This is
fixed-degree evidence only, but it sharpens the B route: a normalized-law
counterexample must keep a word nontrivial in moving internal
structure-orbit holonomy groups and in the correlated global image, not just
in an arbitrary product of orbit factors.

The newest local audit replaces the unsafe one-sided retraction shortcut by a
two-sided context relation.  For a local interval, the forward profile records
the maps `y -> pr_1 T(x,y)` and `y -> pr_2 T(y,x)`.  The implementation meets
this relation with the analogous profile relation for the inverse local table,
then refines by every opposite unary context in both orientations.  A symbolic
triangle argument proves that the stable two-sided relation is an exact
admissible local congruence for arbitrary finite coloured bijections; it does
not use nondegenerate one-sided cancellation or finite search.  Hence
local-minimality forces this stable relation to be either equality or
universal, and semisplit families are covered because they are admissible
families when they work.  The size-2 and size-3 local-minimal cover scans show
exactly this split: size `2` has `1` equality and `4` universal intervals;
size `3` has `24` equality and `110` universal intervals, with `0` mixed or
non-admissible stable families.  Every universal stable interval in these
scans has an explicit product-permutation witness
`T_{a,b}(x,y)=(L_{a,b}(y),R_{a,b}(x))`, with `L` and `R` fibre bijections.
The equality cases in the tiny local-minimal corpus all lie in already
measurable branches: involutive/identity, rack-type, or nondegenerate.  This
is still not a proof of the master theorem, but it sharpens the remaining
A-route: prove symbolically that a two-sided-retraction-free local-minimal
interval is in the known measurable list or is detected by the symmetric
kernel-block/Schutzenberger groups; the universal side is now explicitly
product-permutation.

The product-permutation sides now have exact braid-action normal forms.  For
`T_{a,b}(x,y)=(L_{a,b}(y),R_{a,b}(x))`, every braid word acts on fibres by a
dependency permutation of the input coordinates plus coordinatewise
composition of the finite bijections `L`, `R`, and their inverses along the
strand path.  Thus if the Artin permutation is trivial, the residual action in
this branch is coordinatewise by finitely generated coloured permutation
groupoid labels.  The swapped branch also has a formal word-level normal
form: `swapped_product_label_word_action()` records, for each coordinate, the
word in labels `L_{a,b}^{+/-1}` and `R_{a,b}^{+/-1}` whose evaluation is the
actual residual fibre map.  For the direct coretraction branch
`T_{a,b}(x,y)=(L_{a,b}(x),R_{a,b}(y))`, the dependency vector is always the
identity and the residual action is coordinatewise by the same kind of finite
coloured permutation-groupoid labels; this branch now has the analogous
formal helper `direct_product_label_word_action()` and evaluator
`evaluate_direct_product_label_word()`.  Both normal forms are implemented
and tested, reducing the universal two-sided-retraction and universal
two-sided-coretraction cases to the already logged finite permutation,
pairwise-linking, coboundary, or product-label holonomy targets.  Thus these
universal sides no longer contribute an unnamed hidden branch; any obstruction
there must appear as an explicit closed product label, while non-product
hidden holonomy must live in the bi-free side.

The finite label group for these product normal forms is now explicit rather
than implicit.  The helper module `label_detectors.py` totalizes every
coloured product label to a permutation of the tagged fibre union
`disjoint union_a {a} x A_a`, swapping source and target fibres by the label
and inverse, or acting inside one tagged fibre when the source and target
colour agree.  The groups `swapped_product_label_group()` and
`direct_product_label_group()` are finite, depend only on the interval, and
contain the evaluated formal product label words.  Tests verify that
restriction of the totalized label-word permutation to the source tagged
fibre agrees with the original partial product evaluator.  This does not
prove the product branch: it converts the missing assertion into a sharp
all-`n` statement that base-fixed words in this explicit finite group are
products of recursive Artin-longitude evaluations.

That sharp statement is now isolated as a closed-label cocycle target in
`proofs/product_closed_label_cocycle.md`.  In a base-fixed braid with trivial
Artin permutation, each residual product coordinate is a closed label
`h_{z,j}(beta)` in the finite totalized group `H_prod`.  The exact missing
lemma is that every such closed label is a finite product of recursive
Artin-longitude evaluations in a fixed finite group built from the interval.
This explicitly rules out two invalid shortcuts: finiteness of the label
groupoid alone does not imply detection, and base-fixing alone does not kill
pairwise-linking or genuinely coloured holonomy.

The failure side of the same target is now formalized in
`proofs/product_closed_label_obstruction.md`.  If no finite group detects the
closed product labels, then the usual direct-product/diagonal argument gives
braids `beta_j in B_{q_j}` with `q_j -> infinity` whose finite-group
longitudes are eventually identity for every finite group, while some closed
label remains nontrivial.  The helper
`product_closed_label_blind_movers()` is only a bounded screen for this
phenomenon; the theorem-level B route still requires proving all finite
detector groups fail for an explicit finite YBE solution.

The product-longitude witness audit now rules out one overly strong A-route
formula.  In the two-colour identity-base cyclic fixture, with colour tuple
`(0,1,0)` and braid word `sigma_1 sigma_2^2 sigma_1`, no single homomorphism
`F_3 -> H_prod` evaluates the three Artin longitudes to the three closed
product labels simultaneously.  Thus the product proof cannot require one
common assignment `phi_z` with `h_{z,j}=phi_z(L_j)` for all `j`.  This is not
a counterexample to finite-G detection, because the sharp longitude identity
quantifies over every homomorphism.  The weaker sufficient condition is:
each nonidentity closed label should be a value, or product of values, of
some Artin longitude evaluations in the fixed group `H_prod`, with the
homomorphisms allowed to depend on the coordinate and braid.  The diagnostic
helper `product_closed_label_longitude_witnesses()` finds such per-label
witnesses in the same fixture, while
`product_closed_label_common_longitude_assignments()` records failure of the
too-strong common-assignment shortcut.  This sharpened target is recorded in
`proofs/product_longitude_witness_audit.md`.

The route audit now packages this product split as one fixed-word certificate.
`product_closed_label_longitude_route_audit()` reports the common-assignment
count, the per-label single-longitude witness status, and membership in
`V_beta(H_prod)` for each nonidentity closed product label.  On the
two-colour cyclic fixture it records zero common assignments but no subgroup
failures.  This keeps the product branch aligned with the sharp obstruction
theorem: an A proof must establish subgroup membership symbolically for all
`n`, while a B construction must produce a normalized-law sequence whose
closed labels escape every finite-G longitude-value subgroup.  See
`proofs/product_longitude_route_audit.md`.

The pairwise-linking subcase of the product-permutation branch now has an
explicit cyclic detector recorded in code.  The abelianized Artin longitude
matrix `E_i(beta)_j` is computed from recursive longitudes, and
`Lambda_{C_m,n}(beta)=Lambda_{C_m,n}(1)` is equivalent to trivial permutation
and `E_i(beta)_j=0 mod m` for all `i,j`.  Choosing `m` divisible by the orders
of the relevant finite fibre permutations forces all pairwise-linking labels
to vanish.  The fully coloured product-permutation branch still requires the
bookkept coboundary/groupoid-label reduction before this cyclic argument
applies.

The same argument is now isolated in
`proofs/pairwise_linking_detector.md` as an all-`n` symbolic lemma.  Its
hypothesis is exactly that residual coordinate labels are integer linear
functions of the abelian longitude matrix, modulo fixed finite fibre
permutation orders.  The detector is `G=C_m`, independent of braid index; the
`T_2` part of `A_G` supplies the purity step before the abelian matrix formula
is invoked.  This closes the pairwise-linking branch as a finite-G-measurable
local branch, while explicitly leaving genuinely coloured holonomy to the
coboundary/product-label or bi-free corridor targets.
The local bottleneck summary now exposes this as a product certificate:
closed one-colour pairwise rows carry a
`cyclic_pairwise_linking_group` detector with order equal to the exponent of
the finite product-label group, and the associated sharp rack factor size is
recorded as `2*|G|^2`.  The certificate now stores the actual cyclic group
`C_m`, so this row can feed directly into a sharp obstruction rack factor.

The one-colour swapped product branch is now symbolic, not just audited.  For
`T(x,y)=(L(y),R(x))`, the coloured YBE reduces to `LR=RL`.  Local-minimality
is primitivity of the abelian permutation group `<L,R>` on the fibre.  A
finite abelian primitive permutation group is regular of prime order, so
`<L,R> ~= C_p` and the branch is detected by the cyclic group `C_p` through
the abelian longitude matrix.  The exact formula is now recorded:
for a pure braid, the exponent of `L` on coordinate `j` is the row sum of the
`j`-th abelian recursive longitude vector, and the exponent of `R` is the
corresponding column sum.  Hence `Lambda_{C_p,n}=1` forces both exponents to
vanish modulo `p` for all `n`.  The finite detector is independent of braid
index.

The fibre-size-two product branch is also symbolically identified.  After
choosing a coordinate on each two-point fibre, every product label is a
translation of `F_2`, so both swapped and direct product normal forms become
affine `F_2` extensions of the quotient colour solution.  The coloured YBE
cocycle equations become linear equations in the label bits, and the
base-fixed residual action is a vector translation over `F_2`.  Thus this
whole product subcase lies in the already eliminated affine `F_2`
finite-G-measurable branch; semisplit families are exactly the
equality/universal colour-status choices already checked by local
admissibility.
The product certificate layer marks these fibre-size-two affine rows as
delegated to this affine branch note rather than inventing a local detector
order inside the product wrapper.

The coloured product-permutation constraints have also been made explicit.
Expanding the coloured YBE in the swapped and direct normal forms gives
cocycle equations among the finite fibre bijections `L_{a,b}` and `R_{a,b}`.
These equations are now executable as
`swapped_product_cocycle_failures()` and
`direct_product_cocycle_failures()`.  They are the finite groupoid-label
constraints that a full coboundary reduction must use; a product normal form
alone is not enough unless these YBE cocycle equations hold.

The coboundary subcase of this coloured groupoid-label problem is now
executable too.  The audits `swapped_product_coboundary_audit()` and
`direct_product_coboundary_audit()` attempt to assign gauges `g_a` to the
colour fibres so that every product label is gauge transport.  A successful
audit means there is no extra fibre holonomy after the base action is fixed.
This is now proved at braid-action level in
`proofs/product_coboundary_telescope.md`: every composable coboundary
product-label word telescopes to `g_target^{-1}g_source`, so base-fixed
direct coboundaries and base-fixed, permutation-trivial swapped coboundaries
act trivially on fibres for every braid degree.  A failed audit is then
cleanly separated from coboundary: in the one-colour
swapped case it recovers the pairwise-linking branch handled by cyclic
abelian longitudes, while genuinely coloured failures are the remaining
finite groupoid-label obstruction.
At the ledger level, a coboundary detail now carries the trivial detector
`G=1`, while identity-base cyclic details carry the prime cyclic detector
from `proofs/identity_base_product_branch.md`.  Genuinely-coloured product
rows whose total table is already known reuse the known-branch detector
certificate.  Thus `product_finite_g_branch` is no longer just a string
verdict for these subcases: it exposes the finite detector group object and
order, or names the exact delegated affine branch.
The merged summary accessors `closed_detector_groups` and
`closed_detector_gaps` collect these product detectors together with the
known-total/nondegenerate branch detectors.  Consequently a closed local
verdict now has a direct programmatic path from the audited local table to the
finite groups that should be supplied to the congruence-chain rack assembly.
The path has been tightened further: `closed_detector_product_group` returns
the one finite product group `G_i` for the interval, and
`closed_local_detector_chain()` collects exactly one such group per local row
before `assemble_closed_local_detector_chain_rack()` calls the rack
constructor.  If a row is an open bottleneck, or if a delegated branch such as
fibre-size-two affine has no explicit group object in the local wrapper, the
chain audit records a gap instead of constructing `Q_0`.

Those failures are no longer just booleans.  The holonomy summaries
`swapped_product_holonomy_summary()` and
`direct_product_holonomy_summary()` convert each gauge-loop inconsistency into
a finite permutation of the chosen model fibre and record the finite group
generated by these permutations.  Coboundary branches have trivial holonomy;
the test one-colour pairwise-linking branch has holonomy group `C_3`.  Thus a
remaining product-branch obstruction must now present nontrivial coloured
holonomy not reducible to the cyclic pairwise-linking detector.

The generated product holonomy audit runs this split through the size-2 and
size-3 local-minimal congruence-cover corpus.  In size `3`, swapped product
rows include `57` coboundary cases, `8` one-colour pairwise cases, and `45`
genuinely coloured holonomy cases; all `45` genuinely coloured cases carry
known branch tags such as nondegenerate, involutive, rack-type, or
permutation form.  Direct product rows contribute `6` coboundary cases and no
nontrivial holonomy in the same corpus.  The same generated audit now records
`0` nonprimitive invariant-family rows, so the product rows are also checked
against the local-minimality-as-primitivity formulation.  This is finite
audit evidence only, but it sharpens the symbolic product-branch obligation:
unknown local-minimal product holonomy must either reduce to
coboundary/pairwise-linking/known measurable branches or be realized as a
genuinely coloured holonomy example outside those tags.

Finally, product-branch local-minimality has been rewritten as a finite
groupoid-primitivity condition.  In the swapped branch, admissible congruence
families are precisely partition families transported by every label
`L_{a,b}:A_b -> A_{a.b}` and `R_{a,b}:A_a -> A_{a*b}`; in the direct branch
the source colours are `a` for `L` and `b` for `R`.  Hence local-minimality is
equivalent to saying this finite coloured permutation groupoid has no
invariant partition families besides all equality and all universal.  The
implementation checks that the product-label invariant families agree with
the general `LocalInterval` admissible-family definition on the branch
fixtures.

The product longitude target has also been strengthened from individual
witnesses to a verbal subgroup condition.  For a fixed product-label group
`H_prod` and braid `beta`, let `V_beta(H_prod)` be the subgroup generated by
all values `phi(L_i(beta))` over all assignments `F_n -> H_prod` and all
recursive Artin longitudes.  If every closed product label
`h_{z,j}(beta)` lies in this subgroup, then identity `H_prod` finite-group
longitude data kills the product residual action.  The helper
`product_closed_label_longitude_subgroup_audit()` implements this fixed-word
check, and `proofs/product_longitude_subgroup_criterion.md` records the
corresponding theorem target.  This is the clean finite-product version of
the input-dependent longitude criterion; a product B candidate should first
try to produce a closed label outside this longitude-value subgroup.

The new generated audit `proofs/product_subgroup_audit.md` applies this
criterion to the smallest arbitrary product corpus: two quotient colours,
two-point fibres, and every two-point YBE quotient base.  It checks `53`
braid words on three strands through length `3`.  Since the tagged fibre
union has four points, every product label group has order at most `24`, so
the audit enumerates every assignment `F_3 -> H_prod` for each closed word.
Across `1,658,880` local tables, `629` coloured-YBE tables, `120`
local-minimal intervals, and `92` product branch scans, it finds `128` closed
nonidentity product-label words and `0` longitude-subgroup failures.  This is
finite candidate evidence only, but it supports the product subgroup lemma
and clarifies that a product B candidate should first escape this subgroup
criterion in a larger fibre or colour pattern.

The product branch also now has an exact fixed-degree closed-label image
audit.  `product_closed_label_exact_audit(interval,branch,groups,z)` closes
the finite joint image of a base detector action, product-label states, Artin
strand permutation, and finite-group longitude detector states for one colour
tuple `z`.  The base detector defaults to the quotient colour solution, but
can be replaced by a stronger finite detector such as the rack `Q` in the
sharp-kernel setup.  On the two-colour identity-base cyclic fixture it finds
the expected quotient-only failure for the too-small detector `C_2` at the
word `sigma_1^4`; adding a three-point rack as a stronger base detector
removes that fixed-degree failure, while the product label group detector
also proves the fixed-tuple implication.  The generated audit
`proofs/product_exact_closed_label_audit.md` applies this exact fixed-`n=2`
closure to all two-colour/two-point-fibre local-minimal product branches over
every two-point quotient base.  It checks `368` fixed colour tuples with no
truncations.  The raw product label group detector has `16` failures, all in
known finite-G-measurable rows tagged nondegenerate or rack/nondegenerate,
and `0` untagged failures.  This removes a word-length cutoff from the
smallest product corpus and also warns that the raw product label group alone
is not the final detector in known branches; the all-`n` product theorem must
allow the stated product with known-branch detector factors.

A regression test now pins down the first known-row failure from that exact
audit.  For the two-colour nonidentity quotient fixture, the raw swapped
product label group has order `4` and fails at `sigma_1^4` on the colour tuple
`(0,0)`.  Adding the finite symmetric detector `S_4` on the four total points
removes that fixed-degree failure.  This is finite fixed-degree evidence
only, but it protects the sharp-obstruction bookkeeping: local detector
products, not isolated branch factors, are the objects that feed into
`Q_i = Q_{i+1} x A_{G_i}`.

The product target has also been normalized by the coboundary gauges.  For a
formal label word `f:A_s->A_t`, the new helper
`product_holonomy_label_permutation()` evaluates the residual holonomy
`g_t f g_s^{-1}` on the model fibre selected by the coboundary audit, and
`product_holonomy_closed_label_permutations()` applies this to sharp-kernel
closed product paths.  Coboundary labels normalize to identity, while the
one-colour commuting swapped branch normalizes to the expected cyclic
pairwise-linking holonomy.  The remaining product theorem can therefore be
stated in the smaller fixed product holonomy groups rather than the full
tagged-fibre label group: prove all-`n` longitude-subgroup membership there,
or construct a normalized-law escape.
The helper `product_holonomy_longitude_subgroup_audit()` now implements the
finite fixed-word version of that target by evaluating all recursive
longitudes in the relevant normalized holonomy group and checking membership
of each nonidentity closed holonomy label.  In the regression fixtures,
coboundary rows have no nonidentity normalized labels, while the one-colour
commuting swapped row is detected inside its `C_3` holonomy group.
The generated `proofs/product_holonomy_subgroup_audit.md` now applies this
normalized subgroup check to the smallest arbitrary product corpus: two
quotient colours, two-point fibres, and every two-point quotient YBE base.
It records `92` local-minimal product branch scans, `2,048` nonidentity
normalized holonomy rows, and `0` normalized holonomy-subgroup failures.
This is finite diagnostic evidence only; the product theorem still requires
all-`n` membership in the fixed normalized holonomy groups.

The generated `proofs/product_holonomy_exact_audit.md` adds an exact
fixed-degree guardrail for the same normalized holonomy convention.  On five
representative tuples it closes the finite braid image with no word-length
cutoff, has `0` truncations, proves the fixed-tuple implication in four
rows, and deliberately records one raw normalized-holonomy failure in a
known nondegenerate/permutation row.  Adding the symmetric group on the four
total interval points removes that displayed miss.  Thus the product
detector target really is a detector product: raw normalized holonomy
factors plus the already-known branch factors, not raw holonomy alone.

One symbolic product subcase is now closed.  If the quotient colour table is
the identity solution and the interval is swapped product-permutation, the
coloured YBE forces fibrewise central permutations `K_a` satisfying
`R_{a,b} L_{a,b}=K_b`, `L_{a,b} R_{a,b}=K_a`, and
`L_{a,b}K_b=K_aL_{a,b}`.  The helper
`identity_base_swapped_reduction()` records this exact normal form.  If all
`K_a` are identity, the branch is involutive/coboundary.  Otherwise
local-minimality forces each `K_a` to be one prime cycle, so the branch is
handled by the cyclic pairwise-linking detector `C_p`, independent of braid
index.  Thus the identity-base swapped product branch cannot supply a new
genuinely coloured obstruction.  In the direct identity-base product form,
the cocycle equations force all fibre labels to be idempotent bijections,
hence identities; `identity_base_direct_reduction()` records this executable
triviality check.

The smallest non-identity-colour product stress test is now executable as
well.  The two-colour/fibre-3 product audit enumerates all `S_3` labels over
all five two-point quotient colour YBE tables in both swapped and direct
product normal forms.  On the swapped side it finds `18,612` product cocycle
solutions and `2,064` primitive/local-minimal product rows.  Of these, `1,740`
lie in standard known branch tags and the remaining `324` are exactly the
identity-base cyclic rows covered by the preceding identity-base lemma.  On
the direct side it finds `85` product cocycle solutions and `24`
primitive/local-minimal rows; all `24` primitive direct rows are involutive.
The audit now records central-router verdicts as well: all `2,064` swapped
primitive rows and all `24` direct primitive rows route to
`product_finite_g_branch`, with `0` rows in
`product_genuinely_coloured_bottleneck`.
The direct full cocycle space has nontrivial direct holonomy, so direct
holonomy is not automatically coboundary, but the primitive rows in this
structured search do not produce a new branch.  The audit finds `0` unknown
primitive product rows in either side.  This is still candidate-discovery
evidence, not a proof of the arbitrary-colour product theorem, but it removes
the smallest genuinely coloured product-search escape route.

The product audit now also runs in the complementary direction: three quotient
colours with two-point fibres.  In this case every product label is a bit, so
the swapped and direct cocycle equations are solved exactly as homogeneous
linear equations over `F_2`, then every primitive row is passed through the
central local router.  The audit checks `322985` product cocycle rows and
`2472` primitive/local-minimal rows.  After adding the closed
`*_fibre2_affine` product detail from `proofs/fibre2_product_branch.md`, all
`2472` primitive rows route to `product_finite_g_branch`: `84` swapped
coboundary, `1020` swapped identity-base cyclic, `720` swapped fibre-2
affine, `288` direct coboundary, and `360` direct fibre-2 affine.  Before this
router update, the same audit exposed `144` direct genuinely-coloured open
rows; the first such row is now a regression fixture showing that the
fibre-size-two affine subbranch must be recognized centrally rather than
treated as a new product obstruction.  This is finite corpus evidence plus a
symbolic branch-routing guard, not a proof of the arbitrary-fibre product
theorem.

There is now a dual two-sided coretraction dichotomy as well.  The
coretraction relation views a point as an input coordinate rather than as the
parameter of the one-sided operations: it compares first outputs when the
point is the right input and second outputs when the point is the left input,
again for the table and its inverse and again with two-sided context closure.
The same symbolic triangle argument proves that the stable coretraction
family is an admissible congruence for arbitrary finite coloured bijections.
Thus local-minimality also forces this family to be equality or universal.
The universal coretraction case has the direct product form
`T_{a,b}(x,y)=(L_{a,b}(x),R_{a,b}(y))`, with fibre bijections `L` and `R`, so
it is another finite coloured permutation-groupoid branch with an exact
all-`n` action normal form.  The size-3
local-minimal scan now splits as `18` equality/equality, `6`
equality/universal, and `110` universal/equality for
retraction/coretraction.  The six equality/universal cases are involutive
identity-table cases, and the eighteen bi-free cases are all already in known
branches (`6` involutive, `11` nondegenerate, `1` rack-type nondegenerate).
The remaining A-route is therefore sharper: a genuinely new primitive
counterexample must be both two-sided-retraction-free and
two-sided-coretraction-free, then still escape the symmetric
kernel-block/Schutzenberger detector.

The congruence-chain mechanics audit also found and fixed a representation
bug in local-minimality testing: equality partitions of fibres must be
canonicalized, especially when fibre points are themselves congruence blocks
represented by unordered `frozenset` objects.  A rectangular involutive
example `R((a,b),(c,d))=((a,d),(c,b))` now guards this case.  After the fix,
the exhaustive size-3 congruence-cover scan has `134` local-minimal covers,
not the earlier undercount of `96`.

A targeted two-colour/fibre-2 local enumeration was also added.  Over the
identity base, `331776` local tables contain `33` coloured-YBE tables and `32`
local-minimal intervals; all `32` have universal two-sided retraction and all `32` have
product-permutation witnesses.  Over the flip base, the same `331776` table
space contains `520` coloured-YBE tables and `12` local-minimal intervals;
all `12` are two-sided-retraction-free and all `12` lie in the involutive branch.  This
is still finite candidate search only, but it rules out the smallest
two-colour/fibre-2 primitive degenerate escape from the current branch split.

The two-colour/fibre-2 audit was then extended from the identity and flip
quotient bases to every two-point YBE quotient base.  Across all `5` bases it
checks `1658880` arbitrary local bijection tables.  Of these, `629` satisfy
the coloured YBE and `120` are local-minimal.  The local-minimal subcorpus has
`0` semisplit leaks.  Its output coordinate-kernel closures split into `80`
equality closures and `40` universal closures; every universal closure has
stable depth `0`.  No untagged universal-output example remains after the
known involutive/nondegenerate/permutation/rack tags and product/direct
witnesses are applied.  This is finite audit evidence only, but it closes the
smallest arbitrary-local-table two-colour/fibre-2 hiding place for a
transported-corridor counterexample.

The complete linear `F_2^2` universe was also enumerated.  Among all `65536`
linear maps on `F_2^2 x F_2^2`, `20160` are bijective and `97` satisfy YBE.
None gives an unknown primitive example: two-sided-retraction-free tables are
involutive, rack-type, or nondegenerate; universal tables have the
product-permutation witness; mixed two-sided-retraction tables are not local-minimal
candidates.  This again is candidate search only, but it rules out the
smallest four-point affine-linear `F_2` escape.

The translated affine `F_2^2` universe was then enumerated as well.  Among
`1048576` affine maps `R(x,y)=M(x,y)+t`, `322560` have invertible linear part
and `481` satisfy YBE.  The local-minimal subcorpus has `84` intervals, all
bi-free; every one is already in a known branch: `12` involutive, `24`
involutive nondegenerate, `46` nondegenerate, and `2` rack-type
nondegenerate.  The untagged affine examples in the full scan all have proper
mixed retraction/coretraction families, so they are not local-minimal
primitive intervals.  This remains candidate search only, and affine branches
are only bookkept as finite-G measurable when a separate all-`n` affine,
semidirect, or known-branch detector proof applies; the `affine_cyclic` audit
tag alone is not a closed detector branch.  The scan rules out the smallest
translated affine four-point escape from the current bi-free reduction.

The affine audit now also records coordinate-kernel corridor closure.  Among
the same `84` local-minimal affine intervals, `72` have output-kernel equality
closure and `12` have output-kernel universal closure.  Unlike the size-2 and
size-3 congruence-cover scans, these `12` universal closures have transported
stable depth `1`.  All `12` depth-one rows are involutive.  Therefore
transported universal corridors exist in the structured search universe, but
the smallest such examples still lie in a known finite-G-measurable branch.
The remaining symbolic target is consequently not just "depth-zero";
transported corridor holonomy must also be controlled or realized outside the
known branches.

The bi-free side now has an explicit rank/kernel-profile diagnostic.  In the
exhaustive size-3 local-minimal congruence-cover corpus there are no bi-free
intervals in size `2`, and the size-3 bi-free rows have no untagged
intermediate-rank or intermediate-kernel profile: `6` are involutive with
mixed coordinate ranks `[1,2]` and collapsed kernel shapes `[1]`, `[2]`,
`[1,1]`, while `11` are nondegenerate and `1` is rack-type nondegenerate with
full left and right output ranks `[3]` and singleton left/right output
kernels `[1,1,1]`.  This is finite candidate-search evidence only, but it
focuses the remaining symbolic A-route on a rank/Green dichotomy: prove that
any local-minimal bi-free interval is either forced into the known finite-G
measurable rank-collapsed branches or has enough finite Green kernel-block
group data to detect all residual holonomy.

The local routing has also been consolidated into
`local_master_bottleneck_summary()`, recorded in
`proofs/local_master_bottleneck_ledger.md`.  This helper is not proof
evidence; it is a reduction ledger for a single interval.  It checks coloured
YBE, semisplit leaks, local-minimality, the two-sided retraction and
coretraction dichotomies, product witnesses and product holonomy details,
coordinate-kernel closure, and whole-solution known branch tags, together
with the current two-sided Green detector group orders.  Product witnesses
are now routed first to closed finite-G product subbranches whenever a
coboundary telescope, one-colour pairwise cyclic detector, or known-total
branch detector applies.  The decisive open local verdicts are now
`product_genuinely_coloured_bottleneck` and
`bi_free_universal_corridor_bottleneck`.  The latter requires an interval
that is not semisplit, not a product finite-G subbranch, not locally
nondegenerate, has no already closed whole-solution branch tag, and has
universal coordinate-kernel closure.  Thus a final A proof must prove
finite-longitude factorization for exactly these remaining verdicts, while a
final B proof must realize a normalized-law escape from one of them.

A guardrail now records that `affine_cyclic` is only an audit tag in this
router.  It is not included in the known-total detector set unless accompanied
by an actual symbolic all-`n` detector branch such as involutive,
permutation-form, rack-type, nondegenerate/guitar, or a closed product
subbranch.  Thus a hypothetical local-minimal interval with only an affine
cyclic formula and universal coordinate-kernel closure would still remain in
the product/corridor master target, not in `known_total_branch`.

The bottleneck verdict is now expanded in
`proofs/bifree_universal_corridor_factorization_target.md`.  That target note
records the exact interval hypotheses, the fixed candidate detector
`H(pi,Q)` as a product of two-sided symmetric Green kernel-block groups,
Schutzenberger groups, quotient-detector factors, and already known branch
factors, and the matching B-certificate.  In particular, a future proof must
show the all-`n` implication

```text
Lambda_{H(pi,Q),n}(beta)=Lambda_{H(pi,Q),n}(1)
    => delta_{n,z}(beta)=1
```

for every `beta in ker rho_{Q,n}` and every base tuple `z`.  A future
counterexample must land in this same verdict and supply a normalized-law
sequence moving explicit residual tuples; a bounded detector miss or timeout
is not a certificate.

The target now has a finite subgroup-certificate helper, recorded in
`proofs/bifree_corridor_subgroup_certificate.md`.  The functions
`bifree_corridor_detector_target()`,
`bifree_corridor_detector_groups()`, and
`bifree_corridor_word_certificate()` construct the listed Green detector
factors, profile the longitude-value subgroup `V_beta(H_i)` for each factor,
and attach the first moved residual tuple for a finite braid word.  The
standard size-three affine commutator fixture has detector factor orders
`2`, `3`, and `6`: the word moves the solution, but the full symmetric
order-`6` kernel-block factor sees it, so it is not a B-shaped failure
against the fixed corridor detector list.  This is still finite diagnostic
infrastructure, not theorem evidence.
The same helper path now accepts fixed `extra_groups`.  These are the
code-level representatives for quotient-detector factors, known-branch
factors, and endpoint/unit detector groups that belong to `H(pi,Q)` but are
not generated by the Green audit.  They are appended as named `E_i` factors
before word profiles, exact-image closure, and product-subgroup checks, so
the executable detector target is the full fixed product attached to the
interval and quotient detector rather than only the Green subproduct.  A
regression checks that an extra cyclic factor changes the target/product
orders and appears inside the same direct-product subgroup audit.

The same corridor factor list is now wired into the exact finite-image
closure helper as `bifree_corridor_exact_image_audit()`, recorded in
`proofs/bifree_corridor_exact_audit.md`.  On the affine commutator stress
row, the exact `n=2` image closes with `12` visited states, `12` detector
states, `3` residual states, and no kernel or collision failure, so it proves
the fixed-`n=2` implication for that diagnostic.  The associated commutator
word in degree `3` still moves a tuple, but the order-`6` symmetric
kernel-block factor has nontrivial longitude subgroup and sees it.  This is
again fixed-degree diagnostic infrastructure, not the all-`n` corridor
factorization theorem.

The generated `proofs/bifree_corridor_certificate_audit.md` now applies that
certificate to the exhaustive size-2 and size-3 local-minimal congruence-cover
corpus.  Size `2` has `5` local-minimal covers and all route to the
closed `product_finite_g_branch`: one direct coboundary, one swapped
coboundary, and three one-colour pairwise cases.  Size `3` has `134`
local-minimal covers: `116` route to `product_finite_g_branch`, `12` to
locally nondegenerate, and the `6` formerly target-shaped rows now route to
`known_total_branch` because their total interval solutions are involutive.
The size-`3` product details are `57` swapped coboundary rows, `8`
one-colour pairwise rows, `45` genuinely coloured rows whose total interval
is already in a known branch, and `6` direct coboundary rows.  No interval in
the size-2/3 corpus now reaches either the genuinely coloured product
bottleneck or the bi-free universal-corridor verdict.  This bounded audit
narrows the finite search surface but does not replace the needed all-`n`
subgroup-factorization lemma for arbitrary fibres and quotient colours.

This rank observation has now been separated into a symbolic
coordinate-kernel closure dichotomy.  Let `theta^ker` be the least admissible
congruence family generated by kernels of the nondegeneracy coordinate maps
`y -> pr_1 T_{a,b}(x,y)` and `x -> pr_2 T_{a,b}(x,y)`.  The construction
closes these seed pairs under every local table and inverse local table, so it
is an admissible family by construction.  In a local-minimal interval,
`theta^ker` is equality or universal.  Equality means that all these
coordinate maps are injective; using
`|A_a||A_b|=|A_{a.b}||A_{a*b}|`, injectivity forces them to be bijective, hence
the interval is locally nondegenerate and already bookkept.  Therefore the
only remaining bi-free rank-collapsed side is the universal
coordinate-kernel-closure branch.  The master theorem still needs an all-`n`
detector proof for that universal kernel-closure branch, or an explicit
normalized-law escape from it.

The coordinate-kernel branch now has an elementary pair-closure certificate:
`coordinate_kernel_pair_closure_audits()` closes each distinct nontrivial
coordinate-kernel pair separately under every local table and inverse local
table.  In a local-minimal interval, any elementary coordinate-kernel pair is
non-equality, so its least admissible closure must be universal.  Consequently
the universal corridor branch is not an aggregate artifact; every individual
coordinate-kernel degeneracy must already generate the all-universal
admissible family.  A proposed B interval with a proper elementary closure is
therefore not local-minimal and must be refined before it can enter the
master local theorem.
This elementary gate is now surfaced directly in
`LocalMasterBottleneckSummary` through `output_kernel_pair_count`,
`output_kernel_pair_failure_count`, `output_kernel_pair_max_depth`, and the
derived flag `output_kernel_pairs_all_universal`.  Thus the main local
router records not only the aggregate output-kernel closure but also whether
each seed degeneracy separately opens the required universal corridor.

The generated closure audit now records a finite corridor graph for this
branch: seed coordinate-kernel pairs and their transported images under local
tables and inverse local tables are edges, and universal closure means this
graph connects every fibre.  In the exhaustive size-3 bi-free corpus, the only
universal coordinate-kernel-closure rows are already involutive and have
depth-zero corridors with edge counts `[0,1]` and diameters `[0,1]` over the
two colours.  This is still candidate-search evidence only, but it says the
first tiny-corpus symbolic target is the depth-zero universal corridor case;
any future B candidate must escape not just rank/kernel closure but the finite
transported corridor constraints.

A broader kernel-corridor audit now scans all size-2 and size-3
local-minimal congruence-cover intervals, not only the bi-free rows.  It
records the two-sided retraction/coretraction kind, branch tags, semisplit
leaks, output-kernel closure, all-coordinate closure, corridor depth, and
product/direct witnesses.  In this finite corpus there are `0` semisplit leaks
among local-minimal covers.  Size `2` has `5` local-minimal covers, with `4`
output-kernel equality closures and `1` output-kernel universal closure.
Size `3` has `134` local-minimal covers, with `122` output-kernel equality
closures and `12` output-kernel universal closures.  Every output-kernel
universal closure in both scans has stable depth `0`; the bi-free universal
rows are precisely the `6` involutive size-3 rows already isolated in the
rank audit.

This global corridor scan is not a proof and must not be used as one.  Its
value is diagnostic: it says the smallest observed universal
coordinate-kernel branch is seed-only rather than transport-generated in the
tiny congruence-cover corpus, and it does not produce an untagged
local-minimal residual-holonomy example.  The next symbolic A-route lemma can
therefore start with a seed-only universal corridor statement, while the B
route should search specifically for either transported-depth universal
corridors or seed-only corridors with residual holonomy outside the known
involutive/permutation/nondegenerate measurable branches.

The normalized-law counterexample route has also been split into pure-power
and non-power cases.  Pure powers would require a fixed finite YBE solution
whose pure-generator action orders `rho_{X,q}(A_{i,q})` acquire unbounded
prime-power divisors as `q` grows.  The new pure-power growth audit finds no
such behavior in all size-2 solutions through `q=6`, all size-3 solutions
through `q=6`, or all linear `F_2^2` solutions through `q=5`; the largest
orders in these audits are `2`, `3`, and `3`.  This is not theorem evidence,
but it rules out the easiest exponent-law B route in the current corpus.  The
broader non-power route remains alive: the known size-3 affine commutator
candidate has pure-generator subgroup sizes/exponents `(3,3)`, `(24,12)`,
and `(648,36)` for `q=2,3,4` and exceeds the diagnostic cap at `q=5`, even
though the candidate itself is nondegenerate and already eliminated.

The fixed-image law barrier is now a code-level certificate.  For a free word
`w` embedded by the standard pure braids `A_{r+1,k+1}`, the helper
`law_braid_action_certificate(X,w,k)` generates the finite subgroup of
`Sym(X^{k+1})` generated by those pure-braid images, evaluates `w` inside that
finite subgroup, and checks that this matches the direct action of the
embedded braid.  Therefore if `w` is a law on this fixed finite action image,
the embedded braid acts trivially on `X`.  A B-style normalized-law sequence
must consequently use moving action-image groups on which the chosen
eventual finite-group law words are not laws; fixed-image law words cannot
move a fixed finite YBE action.

The B-route has now been sharpened into a moving-variety criterion.  For each
bound `j`, one may ask for a word `w_j` that is a law on every finite group of
size at most `j`, but is not a law on the moving pure braid action image
`H_j <= Sym(X^{q_j})`.  If such words exist for a fixed finite YBE solution
and the standard pure-braid law embedding moves an explicit tuple, then
`w_j` gives the required normalized-law obstruction sequence because every
fixed finite group has size at most `j` eventually.  The helper
`short_law_separating_groups()` searches finite instances of this separation;
it is diagnostic only, but it gives the B route a precise target beyond pure
powers and beyond single fixed-image law tests.
The prefix-law quantifier is now isolated in
`proofs/normalized_law_sequence_gate.md` and implemented by
`law_sequence_prefix_audit(...)`: a sequence satisfying "word `j` is a law on
every group of order at most `j`" is eventually a law on every fixed finite
group.  The helper checks finite prefixes against listed groups only; it is a
B-candidate gate, not evidence of nontrivial YBE motion.

The moving-variety criterion has now been sharpened to structure orbits in
`proofs/structure_orbit_law_obstruction.md`.  A genuine B sequence can be
certified by finding, for `q_j -> infinity`, one structure orbit `O_j` whose
orbit-local pure image group admits a law separator for all finite groups of
size `<=j`.  The resulting braid moves a tuple inside `O_j`, so the motion is
internal holonomy rather than a change of structure invariant.  The helper
`structure_orbit_law_separation()` supplies only a bounded diagnostic version
of this test.  A new guardrail test records why the detector list must grow:
the dihedral three-point rack has orbit-local separators against only small
cyclic groups, but none in the sampled window once its finite inner group
`Inn(Y)` is included, as required by the finite-rack longitude quotient.
The helper now tests the assigned pure-generator tuple directly instead of
checking non-lawhood on the whole orbit image group, which is the exact
condition needed for the law braid to move a tuple.  With this sharper
diagnostic, the degree-`4` dihedral and size-three affine commutator rows have
the same warning pattern: the commutator separates against `C_2,C_3` in an
orbit of size `27` with pure image group order `648`, but no length-`4`
separator remains after adding `S_3` or the rack inner group.  This rules out
those rows as B evidence and focuses the moving-variety route on examples
escaping the obvious symmetric/inner detector factors.
The generated audit `proofs/symmetric_law_separator_audit.md` then applies
the same assigned-generator diagnostic against the full symmetric detector
`Sym(X)`: all size-`2` solutions at `n=3,4`, all size-`3` solutions at `n=3`,
and the two standard size-three stress rows at `n=4` have `0` length-`<=6`
symmetric-law separators and `0` truncated orbit closures.  This is bounded
finite evidence only, but it rules out the first small moving-variety attack
on the direct `A_{Sym(X)}` route.

The standard pure-braid law embedding is now recorded as a symbolic
law-longitude lemma rather than an empirical convention check.  The kernel of
`P_{k+1} -> P_k` is the free point-pushing subgroup generated by
`A_{1,k+1},...,A_{k,k+1}`; embedding a free law word `w` into that subgroup
puts every recursive Artin longitude in the verbal subgroup generated by
substitution instances of `w`.  Therefore if `w` is a law in a finite group
`G`, the embedded braid has
`Lambda_{G,k+1}(beta_w)=Lambda_{G,k+1}(1)`.  The tests now check this
convention on the sampled cyclic and `S_3` detector groups.  This does not
produce B by itself, but it removes the previous "plausible route" wording:
a future moving-variety counterexample may cite the law-longitude lemma for
the all-finite-group invisibility part.

There is also a new global positive candidate that bypasses the local
congruence-chain machinery if it can be proved: for a whole finite YBE
solution `X`, take the finite group `G_X=Sym(X)`.  The candidate assertion is
that

```text
Lambda_{Sym(X),n}(beta)=Lambda_{Sym(X),n}(1)
    => rho_{X,n}(beta)=1
```

for every braid index `n`.  If true, Sawin domination follows immediately
from the explicit rack `A_{Sym(X)}`.  A generated audit now tests this
candidate in the smallest exhaustive corpora.  Exact finite-image closure
proves the fixed-index implication for all size-`2` solutions at `n=2,3` and
all size-`3` solutions at `n=2`.  The size-`3`, `n=3` exact image scan now
separates the single identity-action row as a trivial implication proof; the
other `72` rows still truncate at `1001` detector states, with no failure
before truncation.  The named helper `symmetric_detector_readout_audit(X,n)`
now exposes the corresponding fixed-index readout form for the direct
candidate; on the size-three affine stress row at `n=2`, it materializes `12`
readout rows over `3` residual states.  The new note
`proofs/direct_symmetric_known_branches.md` adds a symbolic branch filter for
the direct candidate: rack-type, involutive, permutation-form, and
nondegenerate/guitar rows are all directly detected by `Sym(X)` because their
branch detector groups embed in `Sym(X)` or because the action factors
through the Artin permutation.  Regenerated audits show that every size-`2`
and size-`3` row is covered by this filter, so the size-`3`, `n=3`
truncations are branch-closed rather than obstruction candidates.  This is
not proof evidence for arbitrary finite `X`.  Bounded
kernel scans find no
failure for all size-`2`
and size-`3` solutions at `(n=3, length<=4)` and `(n=4, length<=4)`.  The
audit also checks the two-strand obstruction in affine
cyclic families `R(x,y)=(a*x+b*y+e,c*x+d*y+f) mod m` for `2<=m<=8`: every
YBE table found has crossing order dividing `2*lcm(1,...,m)`, the first pure
power invisible to `Sym(m)`.  This is candidate evidence only, not a proof,
but it gives a cleaner A-route target: prove that arbitrary finite YBE
actions factor through the Artin action on the relatively free quotient for
`Sym(X)`, or find the first finite solution whose action escapes this
symmetric detector.

The note `proofs/universal_symmetric_detector_target.md` records this as a
standalone theorem target.  The two-strand obstruction test is now exact and
recorded in `proofs/two_strand_symmetric_gate.md`: for any finite group `G`,
finite-`G` Artin-longitude data on `B_2` is trivial exactly on
`2*exp(G)Z`.  Thus `A_{Sym(X)}` passes the two-strand test exactly when the
crossing permutation order divides `2*lcm(1,...,|X|)`.  A solution failing
this divisibility would disprove the direct `A_{Sym(X)}` route, though not yet
the original Sawin domination theorem.
The helper `two_strand_group_detector_failure_certificate(X,G)` now gives the
explicit one-group obstruction whenever this divisibility fails for a fixed
`G`: the braid `sigma_1^(2 exp(G))`, together with a moved tuple.  Its
symmetric specialization gives the exact certificate that would kill the
direct `A_{Sym(X)}` shortcut if a failing finite YBE table is found.
The complementary note `proofs/two_strand_cyclic_detector.md` proves that
two-strand crossing-order obstructions can never be outcome B by themselves:
for `r=ord(R_X)`, the cyclic group `C_r` has finite-longitude period `2r`,
so `A_{C_r}` detects the `B_2` action of `X`.  Hence a genuine B sequence
must use unbounded braid index and normalized-law holonomy, not only a fixed
crossing-order mismatch.
The generated symmetric detector audit now records the exact crossing-order
histogram in the exhaustive size-`2` and size-`3` solution corpora; both have
`0` rows failing this gate.  This remains finite diagnostic evidence, not a
proof for arbitrary finite `X`.
The linear `F_2^2` audit now records the same gate inside its four-point
linear YBE family: the two-strand symmetric period is `24`, the crossing-order
histogram is `{1:1, 2:42, 3:12, 4:36, 6:6}`, and again there are `0` bad
rows.
The branch notes `proofs/two_strand_known_branch_gate.md` and
`proofs/two_strand_guitar_gate.md` prove the gate symbolically for rack-type,
permutation-form, and nondegenerate/guitar solutions.  In the permutation
branch, `R^2` is diagonal action by `h=sigma tau`, so the crossing order is
`2 ord(h)` for nontrivial `X`, hence divides `2 exp(Sym(X))`.  In the
nondegenerate branch, the derived rack operation
`a op b = sigma_a(rho_{sigma_b^{-1}(a)}(b))` and the two-strand guitar
bijection `J_2(x,y)=(sigma_x(y),x)` satisfy `J_2 R_X = R_D J_2`, so the
crossing action is conjugate to a rack crossing whose inner group embeds in
`Sym(X)`.
The helper `two_strand_symmetric_gate_summary(X)` now classifies exact gate
passes by known two-strand explanation.  The earlier exhaustive size-`3`
`passes_unclassified` rows are exactly nondegenerate rows and now report
`nondegenerate_derived_rack_branch`; regenerated audits have no
`passes_unclassified` rows in the size-`3` crossing gate.  Any future such
label must therefore come from outside the currently closed rack,
permutation, involutive, and nondegenerate/guitar two-strand explanations.
The new note `proofs/two_strand_product_gate.md` proves that this exact
two-strand direct-`Sym(X)` gate is also closed under Cartesian products of
solutions: the product crossing order is the least common multiple of the two
factor crossing orders, and the factor symmetric periods divide the product
symmetric period.  Thus a product construction cannot create the first
two-strand symmetric-detector failure from factors that already pass.
This two-strand gate should be kept separate from the stronger domination
closure in `proofs/product_domination_closure.md`: the latter is all-degree
but assumes the factors already have domination racks.

There is now also a diagonal normalized-obstruction lemma.  If a fixed finite
solution or local residual interval has no finite detector group at all, then
one enumerates finite groups `G_1,G_2,...`, forms products
`H_j=G_1 x ... x G_j`, and chooses a residual mover invisible to `H_j`.  The
direct-product longitude lemma makes this invisible to the first `j` groups,
and adding unused right strands forces braid indices `q_j -> infinity` while
preserving both the moved tuple and the longitude identities.  Thus a B proof
does not need a separate diagonalization argument once it proves that every
finite detector group fails for one explicit finite YBE solution; the
diagonal lemma turns that failure into the normalized-law sequence demanded
by the problem statement.
The executable checks `diagonal_product_invisibility_audit(...)` and
`right_stabilization_longitude_audit(...)` now lock the two convention-sensitive
steps of this diagonalization: finite-longitude invisibility in a direct
product is exactly factorwise invisibility, and right-strand stabilization
preserves old Artin data while adding only trivial strands.  They remain
guardrails for the formal proof, not a finite-search substitute for the
all-finite-group failure needed for outcome B.

The current terminal-gauge target has also been sharpened.  A pure display
as a product of Artin permutation defects can only see the commutator
subgroup of the fixed endpoint factor: the defect word
`beta(w)p_beta(w)^-1` is abelianization-trivial.  The note
`proofs/terminal_gauge_abelianization_barrier.md` records this guardrail and
the helper `artin_defect_abelianization_barrier_audit(...)` checks supplied
finite endpoints against `[U,U]`.  Thus abelian terminal gauge holonomy must
be handled by the ordinary abelian longitude matrix criterion and the
normal-quotient lift, not by a pure Artin-defect shortcut.  The honest final
target is now: prove the abelianized terminal endpoint in `V_beta(U/[U,U])`,
lift that witness to `U`, and prove the commutator or perfect-residual
correction in the fixed unit factor.
The helper `unit_composite_abelianization_audit(...)` now performs the
finite quotient checkpoint for a supplied terminal unit word.  It computes
`U(M)`, `[U,U]`, the abelianized endpoint, and the subgroup
`V_beta(U/[U,U])`.  Passing this audit does not prove the whole endpoint
theorem; it only certifies that the abelian quotient has been handled and
that the remaining problem is a commutator correction.  Failing it identifies
the exact finite abelian quotient where an all-`n` symbolic proof or a
normalized-law obstruction must focus.
The helper `unit_composite_derived_series_lift_audit(...)` packages the
iterated version of the same certificate.  Given lifted stage witnesses, it
checks that each derived quotient correction lands in the next subgroup and
that the final perfect-residual endpoint has its own witness.  The combined
witness is then evaluated in the original unit group.  This closes supplied
solvable-unit certificates once every derived abelian quotient stage is
witnessed, and it isolates the perfect residual in nonsolvable cases.
The helper `unit_perfect_residual_longitude_audit(...)` now records that last
checkpoint directly: it restricts the unit group to the stable perfect
residual `P`, computes `V_beta(P)`, and tests the supplied final residual
endpoint there.  A failure at this stage is the precise nonsolvable terminal
unit seed that would still need normalized-law upgrade before it could be
outcome B.
The helper `unit_composite_product_derived_series_lift_audit(...)` now
assembles several supplied terminal-unit derived-series certificates into one
direct-product detector.  It embeds each factor's combined witness in the
corresponding coordinate and verifies the endpoint tuple in
`V_beta(prod_i U(M_i))`, preserving the fixed interval-level detector
requirement.

The global point-pushing fork has now been compressed to monolithic critical
quotients.  The product-prefix profile `eta_X(k)` is finite and weakly
increasing; if it is unbounded, first failures occur at arities tending to
infinity and can be chosen as one-new-strand Brunnian point-pushing words.
Each such failure compresses to a smallest quotient `H` of `P_k(X)` that is
monolithic, with moved value in the monolith and `|H|` larger than the current
product-prefix size bound.  The monolith is either elementary abelian or a
transitive product of nonabelian simple factors.
The minimal quotient has also split by chief-layer escape mechanism:
`proofs/point_pushing_chief_layer_tail_split.md` proves that a nonabelian
monolith embeds `H` in `Aut(M)`, while an abelian monolith outside `Phi(H)`
has a complement and gives `H=M semidirect L` with `L<=Aut(M)`.  Therefore a
bounded nonabelian or bounded complemented abelian chief layer cannot be a
final product-prefix escape.  Every remaining tail is either large-chief
(`|M_j|->infinity`) or abelian Frattini-depth (`M_j<=Phi(H_j)`).

The elementary-abelian monolith case has also split.  If `M` is the
elementary-abelian monolith of such an `H`, then `[H,M]` is either `1` or `M`.
In the noncentral case `H/C_H(M)` is a faithful irreducible linear action on
`M`, and the moved value is generated by conjugation differences.  In the
central case, `proofs/point_pushing_central_monolith_depth.md` gives another
split: either abelianization separates the monolith and minimality forces `H`
to be cyclic of prime-power order, or `M <= Z(H) cap [H,H]` and the
obstruction is a stem central extension.  The cyclic case then splits again in
`proofs/point_pushing_cyclic_p_power_tail.md`: a cyclic `C_{p^e}` first
failure has either prime escape `p>b(j)` or p-power depth escape
`p<=b(j)<p^e`, and proper quotients kill the bottom monolith element.
That cyclic branch is now closed by
`proofs/point_pushing_cyclic_tail_closure.md`: every cyclic quotient of every
point-pushing action image `P_k(X)` has order dividing the fixed bound
`ord(rho_{X,2}(sigma_1^2))`, because the point-pushing generators are
braid-conjugate to crossing squares.  Hence cyclic product-prefix failures are
impossible once `b(j)` exceeds this bound.
The first-failure quotient itself has also been sharpened by
`proofs/point_pushing_bounded_normal_generator_tail.md`: after Brunnian
normalization and monolithic compression, the moved monolith `M` lies in the
normal closure of the newest point-pushing generator image `t`, and
`ord(t)` divides the same fixed bound `ord(rho_{X,2}(sigma_1^2))`.  Thus every
remaining monolithic tail is a bounded-order normal-generator tail.
The abelian-chief side is now linearized in
`proofs/point_pushing_abelian_chief_relation_module.md`.  If `R` is the
relation subgroup among detector orbit generators `o_c=c d c^{-1}`, then a
minimal abelian-chief first failure induces a nonzero, hence surjective,
`F_p[N_D]`-module quotient `R/[R,R] tensor F_p -> M` onto the elementary
abelian monolith.  Thus an abelian B tail must be an unbounded
relation-module quotient tail; the complementary chief-layer branch is a
nonabelian simple-power relation-lift tail.
The abelian relation-module tail has now been split by
`proofs/point_pushing_abelian_relation_action_split.md`: trivial detector
orbit action forces a one-dimensional central coinvariant quotient
`(Rel_D tensor F_p)_{N_D}->>F_p`, while nontrivial action gives a noncentral
irreducible module quotient with `[N_D,M]=M`.
The central trivial branch has been sharpened further in
`proofs/point_pushing_central_stem_relation_tail.md`: after cyclic closure,
the central quotient is a stem extension `F_p<=Z(H) cap [H,H]`, hence a
nonzero `p`-quotient of the Schur multiplier of a finite detector-orbit
quotient, with the actual relation lift factoring through coinvariants.
The complementary branch has now been compressed in
`proofs/point_pushing_nonabelian_chief_relation_quotient.md`: if the monolith
is `M=S^r`, then the detector orbit relation image is all of `M`, and the old
detector orbit group controls the conjugation action on `M` modulo inner
automorphisms.  Thus the nonabelian B side is a simple-power relation-group
quotient tail, not an arbitrary nonabelian action quotient.
The nonabelian side has also been put into the simple-wreath coordinate normal
form in `proofs/point_pushing_nonabelian_wreath_coordinate_lift.md`: a minimal
failure has `H<=Aut(S) wr Omega` with `Omega` transitive, succeeds modulo
`S^r`, and is witnessed by a detector relation whose lift has a nontrivial
`S`-coordinate.
The noncentral elementary-abelian branch still has the parameter split from
`proofs/point_pushing_noncentral_module_tail.md`: module prime escape,
fixed-prime module-dimension escape, or bounded-module centralizer-layer
escape.  The nonabelian simple-wreath branch still has the parameter split
from `proofs/point_pushing_nonabelian_monolith_tail.md`: simple-factor escape
or fixed-factor multiplicity escape.  Thus the negative fork is now three
structural branches, with parameter refinements: central stem
multiplier/coinvariant tails, noncentral irreducible relation-module tails,
and nonabelian simple-wreath coordinate relation-lift tails.  A positive proof
may close the global point-pushing route by ruling out all three structural
branches uniformly for finite YBE action images.
Within the noncentral module branch,
`proofs/point_pushing_module_prime_characteristic_split.md` now proves that
module-prime escape is eventually cross-characteristic: the escaping primes
do not divide the fixed point-pushing generator order bound `B_X`.
`proofs/point_pushing_active_module_generator_split.md` then separates
noncentral module rows by the newest generator's image in `H/C_H(M)`: trivial
image routes to centralizer-layer generator tails, while nontrivial image gives
a bounded-order linear operator whose conjugate commutator images generate the
irreducible module.
The centralizer-layer case has now been split in
`proofs/point_pushing_centralizer_layer_commutator_split.md`: for
`N=<<t>>_H` inside `C_H(M)` with `M<=N`, minimality forces either an abelian
centralizer layer `[N,N]=1` or a centralizer stem layer
`M<=Z(N) cap [N,N]`.  Thus the remaining noncentral module branch is now:
active bounded-order linear-generator tails, abelian centralizer-layer tails,
or centralizer-stem tails.
The abelian centralizer-layer tail is not a prime-escape mechanism:
`proofs/point_pushing_abelian_centralizer_layer_prime_bound.md` proves that
such an `N` is a finite abelian `p`-group with `exp(N)|ord(t)|B_X`, hence
`p|B_X`.  Any surviving abelian centralizer-layer tail must therefore have
bounded prime support and bounded exponent; only rank or extension structure
can still escape.
The centralizer-stem tail has also been converted into multiplier language in
`proofs/point_pushing_centralizer_stem_multiplier_tail.md`: for
`N=<<t>>_H`, the extension `1->M->N->N/M->1` is stem, so `M` is a quotient of
`H_2(N/M,Z)`, with `N/M` ambient-normally generated by the bounded-order image
of `t`.
The quotient in that stem branch cannot be cyclic:
`proofs/point_pushing_centralizer_stem_noncyclic_quotient.md` proves that a
cyclic `N/M` would make `N` abelian because `M<=Z(N)`, contradicting
`M<=[N,N]`.
The noncyclic quotient branch has now been split in
`proofs/point_pushing_centralizer_stem_transport_split.md`: either the
bounded generator image normally generates `N/M` internally, or the quotient
requires ambient transported conjugates of that internal normal closure.
On the internal side,
`proofs/point_pushing_internal_stem_abelianization_bound.md` proves that the
abelianization of `N/M` is cyclic of order dividing `B_X`; any escape there
must be in the commutator/perfect part or multiplier growth, not in
unbounded abelianization.
On the transport side,
`proofs/point_pushing_transport_residual_quotient_split.md` now forms
`E=(N/M)/<<q>>` and splits the residue into abelian-visible transport
residuals and perfect transport residuals.
The abelian-visible transport residual has also been bounded:
`proofs/point_pushing_transport_residual_abelianization_bound.md` proves that
`E_ab` is generated by transported images of the bounded generator image, so
`exp(E_ab)|B_X` and its prime support is contained in the fixed prime set of
`B_X`.  Thus transport residual abelianization cannot escape by new primes or
unbounded exponent.

## Completion audit checklist

Before claiming A, verify:

- no finite-search-only step is used for the master local theorem;
- every semisplit congruence family is covered;
- each detector `G_i` is independent of braid index `n`;
- the braid-action-level implication is proved for all `n`;
- the congruence-chain induction uses the correct kernels at every stage.

Before claiming B, verify:

- the finite set `X` and bijection `R_X` are explicit;
- YBE is proved symbolically, not only by table enumeration;
- braid words `beta_j in B_{q_j}` are explicit with `q_j -> infinity`;
- for every finite group `G`, the finite-G longitude data of `beta_j`
  eventually matches the identity;
- `rho_{X,q_j}(beta_j)` moves an explicit tuple;
- the sharp obstruction theorem really converts this into failure against
  every finite rack.

## Latest endpoint-unit refinement

The final semigroup/unit obstruction is now phrased as an actual
completed-context Artin row-defect gate in
`proofs/completed_context_artin_row_defect_gate.md`.  For one fixed endpoint
transition monoid `M`, a moving residual endpoint is a unit in `U(M)`, and the
endpoint-unit longitude theorem would follow formally if every actual
completed-context unit row factors through the active Artin detector rack

```text
A_{U(M)} = T_2 x (U(M) x U(M)).
```

Equivalently, for a supported row
`e=(s,x), f=(s tau_x,y) -> e'=(s,u), f'=(s tau_u,v)`, the two defects

```text
delta_a(e,f)=a_{f'}^-1 a_e,
delta_l(e,f)=l_{e'}^-1 a_e l_f
```

must vanish.  YBE cube coherence can make these defects flat around actual
completed-context cubes, but flatness is not the same as vanishing.  Thus the
endpoint A-route is now exactly to prove this actual `A_{U(M)}` row
factorization in every remaining local-minimal corridor.  A B-route still
needs more than a finite row miss: it must upgrade nonvanishing row defect to
a normalized-law sequence invisible to every finite group detector while
moving an explicit residual tuple.

The follow-up refinement
`proofs/completed_context_finite_artin_separation.md` weakens the positive
target from raw row-defect vanishing to the exact finite separability actually
needed.  For each remaining interval, form the universal Artin row group
`Art_I` generated by formal labels `A_e,L_e` on actual germs, with the active
Artin detector row relations imposed for every supported completed row.  The
original endpoint branch is a finite map `Ept` on the actual completed-context
path category.  Finite defect absorption is equivalent to the existence of a
finite quotient `q:Art_I->H` such that

```text
ker(q Art) <= ker(Ept).
```

YBE cube flatness proves that `Ept` is well-defined on actual paths; it does
not prove this finite Artin-null endpoint separation.  Proving this separation
for every remaining local interval closes the positive route.  Failure of
this separation, when witnessed by actual residual braid branches in
unbounded arity, is exactly the normalized-law endpoint obstruction required
for a negative route.

The same endpoint target now has a profinite-language form.  If `T` is the
finite set of terminal Artin slots and

```text
W_!=1 = { alpha(gamma) in Art_I^T : Ept(gamma) != 1 }
```

is the actual nontrivial endpoint Artin language, then finite endpoint
absorption is equivalent to

```text
1 notin closure(W_!=1) in the profinite topology of Art_I^T.
```

For each fixed nonidentity endpoint value `u`, the sublanguage
`W_u={alpha(gamma): Ept(gamma)=u}` is rational, because it is accepted by the
finite completed-context automaton with the finite endpoint value included in
the state.

The sharp braid-action target is the sublanguage

```text
W_u^br = { alpha(gamma) : gamma is actual residual-braid-realizable
                         and Ept(gamma)=u }.
```

Separating every `W_u` is sufficient; separating every `W_u^br` is exact.

Thus the positive route may be attacked by a genuine rational/profinite
separability theorem for actual YBE Artin row groups and their endpoint
languages.  A negative route must make failure of this profinite separation
actual and braid-realizable; a formal nonseparable row-language alone is only
another gap.

There is also a guardrail against an over-strong structural shortcut.  The
displayed Artin row relations, taken as a formal partial row system, can
encode arbitrary finitely presented relators through cycles of the longitude
relations `l_{e'}=a_e l_f`.  Thus row form plus YBE-cube flatness alone does
not force the universal Artin row group to be virtually free, virtually
abelian, rational-subset separable, or the adjoint group of a finite rack.
Such a formal partial-Wirtinger construction is not an actual YBE
counterexample, because the rows may not be realized by supported
completed-context germs.  It does show that a positive structural proof must
use a further actual-YBE property, not only the abstract row presentation.
The sharpened actualness requirement is recorded in
`proofs/completed_context_actualization_gate.md`: an actual row system is a
finite braided-quiver system coming from one global finite YBE table
`r:X^2->X^2`.  Thus a formal negative candidate must pass boundary
preservation, global table consistency, context-product compatibility,
inverse-row saturation, YBE cube coherence, and Artin-readout cube coherence,
and it must preserve the braid-realizable endpoint languages `W_u^br` after
actualization.  The naive supported-cube actualization theorem is false:
ordinary one-vertex YBE also imposes mixed unsupported cube constraints.  In
the explicit gate example, ordinary YBE forces an unsupported value
`r(v,z)=(p,k)` while the row system already specifies `r(w,t)=(p,k)`,
contradicting bijectivity.  Hence a formal negative candidate must first pass
ordinary finite YBE-completion, not merely quiver cube coherence.

Fixed-arity finite separation is also insufficient.  For each braid index
`n`, the image of `B_n` on `X^n` is finite, but the required detector is one
finite quotient of `Art_I` working uniformly in all arities.  A compactness
proof would need an additional bounded-width/no-high-arity endpoint theorem:
every nonidentity braid-realizable endpoint should have a bounded deletion
shadow or completed-context minor, functorial for Artin readout, that still
sees the endpoint.  YBE cube flatness does not currently prove such a theorem.
Failure of bounded width alone is not a no-rack obstruction; only failure of
direct profinite separation for `W_u^br` is equivalent to the normalized-law
negative sequence.

The exact deletion/Fadell-Neuwirth pressure test is now isolated in
`proofs/artin_null_brunnian_endpoint_cross_effect.md`.  For an actual interval
with loop groups `L_n(c)`, deletion maps `d_J`, Artin readouts `alpha_n`, and
endpoint maps `epsilon_n`, the ordinary groups
`BrEnd_{n,N}(c)=epsilon_n(K_{n,N}(c))` record high-arity endpoint branches
whose all `N`-strand deletion shadows are endpoint-trivial.  Arbitrarily large
ordinary Brunnian endpoint cross-effects are only a gap, because one fixed
finite Artin quotient may still detect the full branch.  The no-rack
condition is stronger: for some `u != 1`, the Artin-null Brunnian endpoint
languages with trivial bounded endpoint and Artin deletion shadows have `1`
in their profinite closures for every width.  That profinite Artin-null
Brunnian obstruction is equivalent to the normalized-law no-rack sequence.

There is also a bounded positive-data branch at size four, recorded in
`proofs/size4_degenerate_noninvolutive_probe.md`.  A targeted forced probe
found 40 degenerate non-involutive size-four solutions, all reported to be
bi-degenerate and of crossing order four.  The reported examples split into
two types: 16 with the same observed braid kernels as the two-element cyclic
rack `R(a,b)=(1-b,a)`, and 24 with the same observed braid image orders as
the three-element rack `L_0=L_1=id, L_2=(01)`.  The local script
`tools/audit_size4_degenerate_probe.py` verifies the rack-side image orders
`4,24,192,1920,23040` for the cyclic rack through `n=6` and
`4,48,1536,122880` for the size-three rack through `n=5`.  Since the 40
solution tables and the forced-search script are not yet committed, this is
evidence and a theorem target rather than a reproducible classification:
prove all-arity braid-equivalence for the two observed twisted-union families,
or commit the finite census and then classify its output.
The Type A side now has an explicit affine model in
`proofs/affine_f2_cyclic_rack_equivalence.md`: for
`X=F_2^2`, the formula
`r((a,b),(c,d))=((d,a+b+d),(a+c+d+1,a+1))` preserves the parities
`p_j=a_j+b_j`, and on each parity fibre the coordinates
`t_j=a_j+H_j` carry the two-element cyclic rack action.

The Type B mechanism has now been promoted from a bounded computation to a
closure theorem in `proofs/flip_twisted_union_domination.md`.  If two finite
solutions are dominated by finite racks, then their flip-across disjoint union
is dominated by the flip-across disjoint union of the rack detectors.  The
proof uses the color map `X^n -> {A,B}^n`, its equivariance through
`B_n -> S_n`, and the pure-braid decomposition obtained by deleting all
strands outside a fixed color class.  This adds a new positive family:
iterated flip-across unions of already dominated pieces.

The remaining hidden-fibre induction route has a guardrail in
`proofs/minimal_hidden_fibre_gauge_criterion.md`.  For a quotient `X -> Z`,
an unrestricted finite rack gauge `S` satisfying
`ker rho^Z_n cap ker rho^S_n <= ker rho^X_n` for all `n` is not a smaller
lemma: allowing arbitrary `S` makes the criterion equivalent to Sawin for
`X`.  A useful theorem must therefore construct a restricted finite
transducer/gauge from the quotient, fibres, and extension cocycle.  Failure of
one restricted construction is only another induction gap; failure for every
finite rack gauge is the relative normalized-law negative branch.

The restricted finite-state version is now recorded in
`proofs/finite_transducer_rackification_certificate.md`.  Suppose
`pi:X->Z` is a quotient already dominated by a rack `R_Z`.  A finite rack
`S`, a left-to-right Mealy transducer `M:X^*->S^*`, and an optional invariant
transducer `N:X^*->I^*` form a certificate when their local two-letter
equivariance/invariance equations hold and the combined output
`(pi^n,N_n,M_n):X^n->Z^n x I^n x S^n` is injective for every `n`.  The local
equations are finite table checks, and all-length injectivity is a finite
pair-automaton reachability check.  Under these hypotheses `R_Z x S`
dominates `X`.  This captures the affine size-four Type A cyclic-rack gauge,
but it is a certificate theorem, not a universal existence theorem.  The
missing positive lemma is that every remaining actual finite YBE extension
admits such a finite transducer certificate, or a similarly restricted
finite-state gauge constructed from the quotient/fibre cocycle.  The
fixed-candidate obstruction automata in the same note detect failure for a
given rack and fixed arity; the unresolved quantifier is still uniformity in
`n` and over all finite racks.
The finite conditions are now executable as
`transducer_rackification_audit(...)` in
`src/ybe_domination/transducer_certificate.py`, with a regression verifying
the affine Type A parity/offset certificate.

The exact rack-residual obstruction tower is recorded in
`proofs/rack_residual_obstruction_tower.md`.  Enumerating finite racks as
`R_1,R_2,...` and setting `P_m=R_1 x ... x R_m`, define
`N_{m,n}(X)` as the `X^n`-projection of the kernel of the finite joint image
`< (rho^X_n(sigma_i),rho^{P_m}_n(sigma_i)) > -> Sym(P_m^n)`.  Then Sawin
positive for `X` is exactly `exists m forall n, N_{m,n}(X)=1`, and the
negative normalized-law branch is exactly
`forall m exists n, N_{m,n}(X)!=1`.  The fixed-width computation is now
executable as `rack_residual_obstruction_audit(X,Y,n)` for a supplied detector
rack `Y`; it proves only fixed-width detector failure unless upgraded to the
unbounded tower condition.

The fixed-detector bounded-width route is sharpened in
`proofs/parabolic_kernel_generation_bounded_width.md`.  For a detector rack
`Y`, let `K^Y_n=ker rho^Y_n`.  If there is a bound `B` such that every
`K^Y_n` is normally generated by parabolic copies of `K^Y_k` for `k<=B`, then
checking domination only through arity `B` proves domination in all arities
against every finite target `X`.  The high-arity obstruction to this criterion
is the cross-effect `Q^Y_{B,n}=K^Y_n/J^Y_{B,n}`, and for a target `X` its
realized image `C^{X,Y}_{B,n}=rho^X_n(K^Y_n)/rho^X_n(J^Y_{B,n})`.  A first
failure after all lower arities pass must survive in this quotient.  The flip
rack satisfies the criterion with `B=2`, recovering the involutive branch.
The finite fixed-arity realized cross-effect is now executable as
`realized_parabolic_cross_effect_audit(X,Y,B,n)`: it closes the finite joint
image, extracts the detector-kernel image, embeds lower-kernel `X`-permutations
as finite block permutations `(1,h_X^[j,k])`, normally closes them inside the
finite joint image, and returns a witness braid word if the quotient is
nontrivial.  The quotient is computed in the joint image and is canonically
identified with `rho^X_n(K^Y_n)/rho^X_n(J^Y_{B,n})` because projection to the
`X` coordinate is injective on the detector-kernel image.

## Current conclusion

As of this log entry, neither A nor B is proved.  The current decisive target
is direct profinite endpoint-language separation for the braid-realizable
endpoint languages of the remaining completed-context intervals:

```text
1 notin closure(W_u^br) in Art_I^T
```

for every nonidentity endpoint value `u`.  Proving this for every actual
finite YBE interval gives the fixed finite endpoint quotient needed by the
sharp obstruction theorem and hence completes the positive route.  Refuting it
means exhibiting nonseparating actual residual braid branches in arities
tending to infinity; that gives the normalized-law no-rack sequence.
Formal partial-row nonseparability, failure of one-vertex actualization for a
formal row system, or failure of stronger structural properties such as
virtual freeness of `Art_I`, remains only a gap unless it is made actual and
braid-realizable.  Equivalently, a negative proof must exhibit a nonseparable
endpoint-labelled row system that survives ordinary finite YBE-completion and
one-vertex actualization while preserving `W_u^br`, or produce the
nonseparable actual interval directly.
