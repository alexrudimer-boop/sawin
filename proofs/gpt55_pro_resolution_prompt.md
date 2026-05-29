# GPT-5.5 Pro Attachment Prompt

I am attaching a zip archive of a research/proof workspace for the Sawin
finite-rack domination problem for finite bijective set-theoretic
Yang-Baxter solutions. Treat the zip as the source of record: inspect the
proof notes, code, tests, tables, and generated artifacts before answering.

Your task is to completely resolve the problem. Return exactly one of these
two outcomes if you can prove it:

A. A complete proof of Sawin finite-rack domination.

B. An explicit finite bijective set-theoretic Yang-Baxter counterexample not
dominated by any finite rack, together with a normalized-law obstruction
sequence.

Problem statement:

For every finite bijective set-theoretic Yang-Baxter solution X, prove or
disprove the existence of a finite rack Y such that, for every braid index n,

```text
ker rho_{Y,n} subset ker rho_{X,n}.
```

Do not give finite-search-only evidence, timeout evidence, or a rack that
depends on n. Computations in the archive may be used only as audited
reductions, examples, certificates, or counterexample discovery tools; every
decisive step must be converted into a symbolic all-n proof.

## First Files To Read

Start with these files in the attached zip:

1. `proofs/progress_summary.md`
2. `README.md`
3. `proofs/sawin_status.md`
4. `proofs/finite_longitude_factorization_criterion.md`
5. `proofs/longitude_subgroup_profile.md`
Also read `proofs/longitude_subgroup_functoriality.md`, which proves that
fixed finite group homomorphisms preserve the longitude-value subgroup
criterion and that surjective detector quotients preserve it exactly.
Also read `proofs/longitude_subgroup_products.md`, which proves
`V_beta(prod_i G_i)=prod_i V_beta(G_i)` for fixed finite detector products.
Also read `proofs/longitude_subgroup_witness_calculus.md`, which upgrades
the homomorphism and product subgroup lemmas to explicit witness operations:
push a longitude-subgroup witness through a fixed homomorphism, or assemble
factor witnesses into one product witness.
Also read `proofs/normalized_law_sequence_gate.md`, which isolates the
B-side prefix condition: if word `j` is a law on every finite group of order
at most `j`, then the sequence is eventually invisible to every fixed finite
group after the pure-braid law embedding.
Also read `proofs/detector_action_products.md`, which proves that
`A_{prod_i G_i}` projects to the factor detector actions and therefore
combines factor readouts.
5. `proofs/label_longitude_factorization.md`
6. `proofs/input_dependent_longitude_factorization.md`
Also read `proofs/fixed_detector_action_factorization.md`, which states the
detector-rack action quotient/readout form of the same finite-G criterion.
Also read `proofs/fixed_detector_readout_audit.md`, which gives the exact
fixed-index residual-fibre readout table audit and explains why the remaining
Green/corridor task is a uniform all-`n` readout construction rather than a
fixed-degree table computation.  The code now also exposes
`symmetric_detector_readout_audit(X,n)`, the direct `Sym(X)` fixed-index
readout wrapper over the one-point quotient; treat it as diagnostic evidence
only unless you prove the corresponding all-`n` factorization.
7. `proofs/detector_product_groups.md`
8. `proofs/product_domination_closure.md`
9. `proofs/hereditary_domination_closure.md`
Also read `proofs/nondegenerate_cover_obstruction.md`, which rules out
solving degenerate solutions by quotienting finite nondegenerate covers.
10. `proofs/local_minimality_gate.md`
11. `proofs/rack_cover_obstruction.md`
12. `proofs/purity_stabilization.md`
13. `proofs/pairwise_linking_detector.md`
14. `proofs/universal_symmetric_detector_target.md`
15. `proofs/symmetric_detector_audit.md`
16. `proofs/direct_symmetric_known_branches.md`
17. `proofs/symmetric_law_separator_audit.md`
18. `proofs/two_strand_symmetric_gate.md`
19. `proofs/two_strand_known_branch_gate.md`
20. `proofs/two_strand_guitar_gate.md`
21. `proofs/two_strand_product_gate.md`
Also read `proofs/two_strand_cyclic_detector.md`, which proves that for
`r=ord(R_X)`, the cyclic group `C_r` detects the two-strand action.  This
rules out any pure two-strand crossing-order mismatch as outcome B.
22. `proofs/quotient_image_kernel_exact_sequence.md`
23. `proofs/residual_dependency_support.md`
24. `proofs/master_local_dichotomy.md`
24. `proofs/corridor_green_bridge.md`
25. `proofs/product_label_words.md`
Also read `proofs/swapped_product_nondegenerate_base.md`, which removes
swapped product extensions over nondegenerate quotients by lifting
nondegeneracy to the total solution.
26. `proofs/product_closed_label_cocycle.md`
27. `proofs/product_holonomy_normalization.md`
28. `proofs/product_longitude_witness_audit.md`
29. `proofs/product_longitude_route_audit.md`
30. `proofs/product_longitude_subgroup_criterion.md`
31. `proofs/product_holonomy_subgroup_audit.md`
32. `proofs/product_holonomy_exact_audit.md`
33. `proofs/product_subgroup_audit.md`
34. `proofs/product_closed_label_obstruction.md`
35. `proofs/universal_corridor_target.md`
36. `proofs/kernel_corridor_audit.md`
37. `proofs/local_master_bottleneck_ledger.md`
38. `proofs/bifree_universal_corridor_factorization_target.md`
39. `proofs/bifree_corridor_subgroup_certificate.md`
40. `proofs/bifree_corridor_certificate_audit.md`
41. `proofs/bifree_corridor_exact_audit.md`
42. `proofs/local_minimal_green_audit.md`
43. `proofs/dual_green_symmetry.md`
44. `proofs/opposite_detectability_closure.md`
45. `proofs/finite_semigroup_holonomy_route.md`
46. `proofs/unit_holonomy_longitude_gate.md`
Also read `proofs/unit_factorization_gate.md`, which proves that a product of
finite total transformations can be a residual permutation only when every
factor is already a unit/permutation.
Also read `proofs/unit_section_detection_criterion.md`, which packages
monoid membership, unit factorization, and `V_beta(U(M))` membership into the
fixed finite-`U(M)` detector implication.
Also read `proofs/unit_composite_longitude_criterion.md`, which records the
weaker endpoint target: the final residual unit/composite may lie in
`V_beta(U(M))` even when intermediate section labels do not.
Also read `proofs/unit_composite_longitude_route_audit.md`, which separates
the fixed-word endpoint routes: identity endpoint, single evaluated
longitude witness, and full longitude-subgroup membership.  Only failure of
the subgroup route is serious for B.
Also read `proofs/endpoint_longitude_expression_certificate.md`: an endpoint
displayed as a word in evaluated recursive longitudes for one assignment into
`U(M)` is a non-enumerative certificate of membership in `V_beta(U(M))`.  If
you prove A through endpoint units, this is the preferred symbolic certificate
format.  The code also includes
`evaluate_longitude_subgroup_witness(...)`, whose letters may use different
assignments; this is the literal subgroup-word format for membership in
`V_beta(G)`.
Also read `proofs/unit_section_product_detector.md`, which combines finitely
many fixed unit-section factors into one direct-product detector group.
47. `proofs/green_holonomy_factorization_gate.md`
48. `proofs/involutive_permutation_detector.md`
49. `proofs/structure_orbit_law_obstruction.md`
50. `proofs/fixed_variety_barrier.md`
51. `proofs/bounded_degree_action_image_limit.md`
Also read `proofs/diagonal_normalized_obstruction.md`, which proves that an
explicit detector-free interval diagonalizes to the normalized-law sequence
required for outcome B.  Audit the companion helpers
`diagonal_product_invisibility_audit(...)` and
`right_stabilization_longitude_audit(...)` for product and stabilization
conventions only; they are not a substitute for proving all finite detector
groups fail.
52. `proofs/affine_f2_audit.md`
53. `proofs/two_colour_fibre2_all_bases_audit.md`
54. `proofs/fibre2_product_branch.md`
55. `proofs/two_colour_fibre3_product_audit.md`
56. `proofs/three_colour_fibre2_product_audit.md`
57. `proofs/sawin_proof_log.docx`
58. `tables/reduction_audit.xlsx`
59. Relevant code in `src/`, `tools/`, and `tests`, especially modules
    concerning input-dependent longitude factorization, quotient image
    kernels, residual dependency support, local-minimal intervals, local
    bottleneck routing, coordinate-kernel corridors, product label words,
    product closed-label longitude subgroup audits, finite-longitude
    subgroup/mover profiles, semigroup holonomy, structure-orbit law
    separation, Green kernels, and finite-longitude factorization.

## Required Reductions To Audit And Use

1. Quotient/residual setup.

For a quotient `pi:X->Z`, with `Z` dominated by a finite rack `Q`, set

```text
N_n = ker rho_{Q,n}.
```

For `z in Z^n`, set

```text
X_z = product_i pi^{-1}(z_i),
delta_{n,z}: N_n -> Sym(X_z),
Delta_n(beta) = (delta_{n,z}(beta))_z.
```

Once `beta in N_n`, the base point in `Z^n` is fixed, so all remaining
motion is fibrewise.

2. Sharp obstruction theorem.

For a finite group `G`, the rack

```text
A_G = T_2 x (G x G)
```

with rack operation

```text
(a,u) triangleright (b,v) = (a b a^{-1}, a v)
```

detects finite-G Artin-longitude data `Lambda_{G,n}(beta)`.

Residual detection is equivalent to the existence of a finite group `G` such
that, for all `n` and all `beta,gamma in N_n`,

```text
Lambda_{G,n}(beta) = Lambda_{G,n}(gamma)
    => Delta_n(beta) = Delta_n(gamma).
```

The kernel form suffices:

```text
Lambda_{G,n}(beta) = Lambda_{G,n}(1)
    => Delta_n(beta) = 1.
```

Then `Q x A_G` dominates the interval.
In the code archive this rack is constructed by
`sharp_obstruction_rack(Q,G)`.  Audit this as the final finite rack
constructor after a local detector group `G` is proved; do not confuse this
explicit construction with the still-open problem of finding `G`.
The chain-level wrapper `assemble_congruence_chain_rack(Q_m, groups)` iterates
this constructor along the supplied finite detector groups and records
`|Q_i|=|Q_{i+1}|*2*|G_i|^2`.  It has no braid-index input; audit it only as
the formal assembly layer once the local groups have been proved.

3. Congruence-chain induction.

For a maximal congruence chain

```text
Delta_X = kappa_0 < ... < kappa_m = Nabla_X,
```

it suffices to prove the local theorem for every local-minimal interval
`X/kappa_i -> X/kappa_{i+1}`. If the local detector is `G_i`, set

```text
Q_i = Q_{i+1} x A_{G_i}.
```

4. Local residual table.

For

```text
R_Z(a,b) = (a dot b, a*b),
```

fibres `A_a`, and local bijections

```text
T_{a,b}: A_a x A_b -> A_{a dot b} x A_{a*b},
```

the coloured Yang-Baxter equation is

```text
T^{12}_{a dot b, (a*b) dot c} T^{23}_{a*b,c} T^{12}_{a,b}
=
T^{23}_{a*(b dot c), b*c} T^{12}_{a,b dot c} T^{23}_{b,c}.
```

Local-minimality means the only admissible congruence families `theta_a` are
all equality or all universal, where

```text
T_{a,b}(theta_a x theta_b) = theta_{a dot b} x theta_{a*b}.
```

Always handle semisplit families. Do not assume they vanish by colour
transitivity, nondegeneracy, or search evidence.
The archive includes an exact Boolean-CSP semisplit audit:
`LocalInterval.semisplit_constraint_rows()` lists, for each coloured crossing,
the allowed equality/universal bit patterns on
`(source_a, source_b, target_c, target_d)`, and
`LocalInterval.semisplit_boolean_assignments()` returns the satisfying
non-extreme assignments after relation-family canonicalization.  Use this as
the semisplit gate; do not replace it with a quotient-colour graph shortcut.
The archive also includes an exact arbitrary-fibre local-minimality audit:
`LocalInterval.pair_generated_local_minimality_audits()` computes the least
admissible family generated by each distinct pair in one fibre.  The interval
is local-minimal iff every such single-pair closure is all-universal.  Use
this pair-closure criterion; do not rely on bounded partition enumeration for
large fibres.
For the coordinate-kernel corridor branch, also audit the elementary
coordinate-kernel pair closures:
`coordinate_kernel_pair_closure_audits(interval)` and
`coordinate_kernel_pair_closure_failures(interval)` close each distinct
coordinate-kernel seed pair separately.  In a genuinely local-minimal
degenerate interval, every nontrivial coordinate-kernel pair must have
universal closure; a proper elementary closure means the interval was not yet
minimal and the congruence chain must be refined.

5. Known eliminated or finite-G-measurable branches.

The archive records reductions for the following branches. Audit them before
relying on them:

- nondegenerate/guitar;
- fibre size 2 affine over F_2;
- two-colour fibre size 3 flip base with no strict primitive nonlinear
  obstruction;
- affine, involutive/permutation, pairwise-linking, bounded
  Magnus/nilpotent, finite semidirect affine, coboundary, product-label, and
  several Green/corridor branches.

## Main Open Target

Prove the Master Local-Minimal Residual Theorem for arbitrary finite fibres
and arbitrary quotient colours, or construct outcome B.

Master theorem:

Every local-minimal interval `pi:X->Z` with `Z` dominated by `Q` has a finite
group

```text
G = G(pi,Q),
```

independent of `n`, satisfying

```text
Lambda_{G,n}(beta) = Lambda_{G,n}(1)
    => Delta_n(beta) = 1
```

for every `n` and every `beta in N_n`.

## Current Workspace Diagnosis

The strongest positive route in the archive is the finite-longitude /
label-longitude factorization route, broadened by
`proofs/input_dependent_longitude_factorization.md`: the homomorphism
`F_n -> G` used to evaluate a longitude may depend on the input fibre tuple,
because finite-G longitude identity quantifies over all homomorphisms.

There is also a tempting direct route in
`proofs/universal_symmetric_detector_target.md`: prove that
`G_X=Sym(X)` detects the whole solution, giving the explicit rack
`A_{Sym(X)}`.  The archive records two important guardrails for this route.
First, `proofs/rack_cover_obstruction.md` and
`proofs/input_dependent_longitude_factorization.md` show that a literal
rack-style coordinate formula

```text
rho_X(beta)(x)_j = phi_x(L_j(beta))(x_{p(j)})
```

would force `R_X` to be rack-type already, because for one positive crossing
`L_{i+1}=1` and `p(i+1)=i`.  Thus a proof of the direct `Sym(X)` target must
be a genuinely global factorization through `W_{Sym(X)}(n)`, not a disguised
rack proof.  Second, `proofs/symmetric_law_separator_audit.md` finds no
length-`<=6` structure-orbit law mover against the full symmetric detector in
the smallest checked corpora; this is diagnostic only, not theorem evidence.
The helper `symmetric_detector_readout_audit(X,n)` materializes the fixed
`Sym(X)` readout at one braid degree, and its regression test proves the
size-three affine stress row at `n=2`; do not mistake that for a uniform
detector proof.
Also use `proofs/direct_symmetric_known_branches.md`: rack-type,
involutive, permutation-form, and nondegenerate/guitar solutions are directly
detected by `Sym(X)` by subgroup monotonicity or Artin-permutation
factorization.  The size-`2` and size-`3` exhaustive rows have no unknown
cases under this symbolic filter, so their exact detector truncations are not
counterexample evidence.
The executable helper `known_branch_detector_certificate(X)` makes these
closed branches concrete: it returns `G=1` for involutive rows,
`G=C_ord(sigma tau)` for permutation-form rows, and `Sym(X)` for the
rack-type/nondegenerate direct-symmetric branches, together with the sharp
rack factor size `2*|G|^2`.  Audit that any local `known_total_branch` use is
backed by one of these fixed groups, not merely by a tag.

Do not try to solve the problem by a direct rack cover of `X`, by a literal
Hurwitz-conjugation structure-group formula, or by the coordinatewise rack
longitude formula above unless you first prove that the interval is in the
rack-type or known nondegenerate/derived-rack branch.

The remaining decisive gap appears to be the symbolic branch isolated in
`proofs/bifree_universal_corridor_factorization_target.md`: after semisplit,
product, nondegenerate, and known finite-G-measurable branches are removed,
prove that every bi-free universal-corridor residual holonomy factors through
evaluations of Artin longitudes in one fixed finite group `H=H(pi,Q)`,
independent of `n`, or construct a normalized-law escape from exactly that
verdict.

In product branches, express this through the closed labels
`h_{z,j}(beta)` in `proofs/product_closed_label_cocycle.md` and the formal
product label words in `src/ybe_domination/product_permutation.py`: either
prove those closed labels lie in the subgroup generated by recursive
Artin-longitude values in a fixed `H_prod`, or use
`proofs/product_closed_label_obstruction.md` by proving every finite detector
group fails and then producing the normalized-law sequence that keeps one
closed product label nontrivial.
When passing between totalized label groups, normalized holonomy groups, unit
groups, detector products, and quotient factors, use
`proofs/longitude_subgroup_functoriality.md`: fixed homomorphisms send
`V_beta(G)` into `V_beta(H)`, and surjections preserve it exactly.  Do not
introduce an `n`-dependent group for these changes of detector coordinates.
When multiplying detector factors, use
`proofs/longitude_subgroup_products.md`: the product detector's
longitude-value subgroup is exactly the product of the factor subgroups, so
factorwise membership proofs combine into one fixed finite `G`.
For action/readout proofs, also use `proofs/detector_action_products.md`:
factor readouts through `A_{G_i}` assemble into one readout through
`A_{prod_i G_i}` by coordinate projection.
Use `exact_detector_product_readout_audit(...)` only as a fixed-index
convention audit that the displayed factor readouts match the single product
detector readout when the product is enumerable.
Before using a product branch as a master-theorem interval, audit the exact
product-label pair-closure gate:
`swapped_product_label_pair_closure_audits()` or
`direct_product_label_pair_closure_audits()` must have no non-universal
closures.  This is the product-groupoid form of local-minimality and does not
depend on bounded partition enumeration.

Important warning from `proofs/product_longitude_witness_audit.md`: one common
homomorphism `F_n -> H_prod` need not realize all coordinate labels at once.
The correct proof may use per-coordinate, per-factor, or input-dependent
homomorphisms, because finite-G longitude identity quantifies over all
homomorphisms.

Use `proofs/product_longitude_route_audit.md` to keep the product branch
honest: common-assignment failure is harmless, missing single-longitude
witnesses are only a stronger-target failure, and only rows outside
`V_beta(H_prod)` point toward a normalized-law B obstruction.

In the Green/corridor branch, express the same factorization using
input-dependent evaluations in the symmetric Green kernel-block groups,
Schutzenberger groups, semigroup-holonomy split, and already measured branch
factors. The semigroup note proves that purely aperiodic transition
components cannot produce nontrivial residual permutation motion after group
holonomy is killed; it does not itself prove the all-n factorization.
Also audit the atom-action layer: `atom_action_summary()` checks whether
`p(a^q)` depends only on the saturated atoms `p(a),p(q)` and whether the
inverse bookkeeping operation is well-defined.  A positive A proof should
explain this atom descent symbolically or show why residual detection does
not need it; a B proof may instead exploit an explicit atom-action or section
holonomy failure and upgrade it to normalized laws.
When the atom action is total, `atom_quotient_solution()` constructs the
finite crossing `(A,Q)->(Q,A^Q)`.  Audit
`proofs/green_atom_quotient_layer.md`: a descended total atom quotient is a
right-rack-like YBE layer; `atom_quotient_rack_audit()` records the explicit
right-translation bijectivity and right self-distributivity checks.  The
unresolved obstruction should be below this atom rack layer in section/unit
holonomy unless the atom descent theorem itself fails.
Also audit `proofs/green_atom_descent_closure.md`: the helper
`atom_descent_closure_summary()` computes the least coarsening required for
completed-row action and inverse bookkeeping to descend.  If you prove A, show
symbolically that this closure is trivial or absorbed by a controlled quotient
branch for arbitrary local-minimal intervals.  If you prove B, a nontrivial
closure must be upgraded to the normalized-law sequence, not merely exhibited
at finite size.
Then audit `proofs/green_atom_rack_lift_criterion.md`: after atom descent,
the proposed Green detector is the single product of the atom inner group
`G_A` and the lower unit groups.  The missing all-n statement is endpoint
membership in the product longitude-value subgroup, not another fixed-degree
Green table.
The helper `bifree_corridor_product_subgroup_audit()` checks the finite
factor list against its single direct-product detector in small cases, while
`proofs/longitude_subgroup_products.md` supplies the symbolic factor-to-product
step.  Do not treat separate factor checks as using an n-dependent family of
groups; if the factorwise theorem is true, the detector is their one fixed
finite product.
Use `proofs/unit_holonomy_longitude_gate.md` for semigroup labels: once a
finite transition monoid observer is fixed, only its unit/permutation group
can carry residual permutation motion, and every proposed group-like label
must be proved to lie in `V_beta(U(M))`, the subgroup generated by all
recursive Artin-longitude values in that fixed unit group.  Nonunit reset
labels are not B obstructions.  Also apply
`proofs/unit_factorization_gate.md`: if a semigroup observer word has final
residual action a permutation, then every factor in that word is already a
unit, so a proposed B construction cannot hide its motion in reset/nonunit
factors.  Then apply `proofs/unit_section_detection_criterion.md`: the actual
A target is an all-`n` residual section word in one fixed finite monoid whose
unit labels lie in `V_beta(U(M))`; the actual B target must escape this
finite unit-group detector by normalized laws.  If several fixed monoids are
used, apply `proofs/unit_section_product_detector.md` to combine their unit
groups into one finite product detector independent of `n`; when using the
endpoint target, audit this with `unit_composite_product_detection_audit(...)`
and check the recorded endpoint tuple in `V_beta(prod_i U(M_i))`.
Prefer the weaker endpoint target from
`proofs/unit_composite_longitude_criterion.md` when transports telescope:
prove the final unit/composite lies in `V_beta(U(M))`; do not require every
intermediate label to lie there unless the branch proof genuinely supplies
that stronger statement.
Use `unit_composite_longitude_route_audit(...)` only as a fixed-word
bookkeeping tool: a missing single-longitude witness is not an obstruction
when the endpoint still lies in the longitude-value subgroup.
When possible, replace endpoint subgroup enumeration by an explicit
`unit_composite_longitude_expression_audit(...)` certificate: the assignment
and expression may depend on the residual input data, but the unit group must
be fixed by the interval and quotient detector, not by `n`.
For multiple endpoint unit groups, use
`unit_composite_product_longitude_expression_audit(...)` to package the
factor expressions into one product endpoint certificate.  Audit the returned
`product_witness_value` and `product_witness_matches_endpoint`: the product
certificate should be an actual word in `V_beta(prod_i U(M_i))`, not merely an
appeal to finite subgroup enumeration.
Before treating a corridor example as B-shaped, verify that its elementary
coordinate-kernel pair closures are universal; otherwise it is a reducible
non-local-minimal interval rather than a master-local obstruction.
For two-strand detector checks, use
`two_strand_group_detector_failure_certificate(X,G)`: when
`ord(R_X)` does not divide `2 exp(G)`, it returns the explicit invisible
braid `sigma_1^(2 exp(G))` and a moved tuple.  Its symmetric specialization
is a direct certificate against `A_{Sym(X)}` if that gate ever fails, but it
does not by itself defeat every finite group.

If this factorization is proved, the finite rack is obtained by iterating

```text
Q_i = Q_{i+1} x A_{G_i}
```

along a maximal congruence chain.

## If Proving A

You must:

1. Explicitly construct `G(pi,Q)` for every local-minimal interval, or
   explicitly construct the final finite rack `Y` for `X`.
2. Prove braid-action-level detection for all `n`, not only checked `n`.
3. Handle arbitrary fibre size and arbitrary quotient colour set.
4. Prove semisplit local-minimality is fully handled.
5. Prove every detector group is independent of `n`.
6. Finish the congruence-chain induction from local intervals to arbitrary
   finite `X`.

## If Proving B

You must:

1. Give an explicit finite set `X` and explicit bijection
   `R_X:X^2->X^2`.
2. Prove the Yang-Baxter equation symbolically.
3. Construct explicit braids `beta_j in B_{q_j}`, with `q_j -> infinity`,
   such that for every finite group `G`,

```text
Lambda_{G,q_j}(beta_j) = Lambda_{G,q_j}(1)
```

eventually, but

```text
rho_{X,q_j}(beta_j) != 1.
```

4. Give explicit moved tuples.
5. Prove the obstruction sequence is normalized-law based and defeats every
   finite group `G`.
6. Explain via the sharp obstruction theorem why this defeats domination by
   every finite rack.
7. Use `proofs/diagonal_normalized_obstruction.md` only after proving the
   explicit interval defeats every finite detector group.  The code helpers
   `diagonal_product_invisibility_audit(...)` and
   `right_stabilization_longitude_audit(...)` should be used to audit the
   product `H_j=G_1 x ... x G_j` and right-strand stabilization conventions.

## Mandatory Final Audit

Before finalizing, include a short audit answering:

1. Is any decisive step merely finite-search evidence?
2. Are semisplit local-minimal families fully handled?
3. Is every detector group `G` independent of `n`?
4. If giving B, why does the sequence defeat every finite group `G`?
5. Is the congruence-chain induction valid from local intervals to all finite
   `X`?

## Output Discipline

Return outcome A or outcome B only if it is genuinely complete. If neither
can be completed from the archive plus your own reasoning, do not present a
partial argument as a resolution. Instead, identify the exact unproved lemma
or exact missing counterexample ingredient, and give the shortest route to
settle it.
