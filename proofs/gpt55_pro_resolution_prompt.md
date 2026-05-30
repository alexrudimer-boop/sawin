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
39. `proofs/bifree_corridor_endpoint_factorization.md`
40. `proofs/artin_defect_longitudinalization_sieve.md`
41. `proofs/artin_detector_lift_criterion.md`
42. `proofs/atom_inner_detector_lift_rows.md`
43. `proofs/green_first_output_defect_criterion.md`
44. `proofs/green_defect_kernel_quotient_detection.md`
45. `proofs/green_defect_potential_coboundary.md`
46. `proofs/artin_defect_abelianization_barrier.md`
47. `proofs/green_defect_abelianization_split.md`
48. `proofs/abelian_longitude_image_criterion.md`
49. `proofs/green_balanced_defect_gauge_decomposition.md`
50. `proofs/terminal_gauge_longitudinalization_criterion.md`
51. `proofs/principal_gauge_extension_detector.md`
52. `proofs/transport_state_rackification_detector.md`
53. `proofs/continuation_congruence_descent_gate.md`
54. `proofs/elementary_continuation_closure.md`
55. `proofs/universal_continuation_derivation_certificate.md`
56. `proofs/chart_transport_collapse.md`
57. `proofs/descent_separation_transport_rack_closure.md`
58. `proofs/bifree_corridor_subgroup_certificate.md`
59. `proofs/bifree_corridor_certificate_audit.md`
60. `proofs/bifree_corridor_exact_audit.md`
61. `proofs/local_minimal_green_audit.md`
62. `proofs/dual_green_symmetry.md`
63. `proofs/opposite_detectability_closure.md`
64. `proofs/finite_semigroup_holonomy_route.md`
65. `proofs/unit_holonomy_longitude_gate.md`
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
Also read `proofs/artin_defect_longitudinalization_sieve.md`: Artin
permutation defects `beta(w)p_beta(w)^-1` lie in the normal closure of the
recursive longitudes, and every finite-group value of such a defect lies in
`V_beta(G)` by changing assignments to absorb the normal conjugators.  Thus
the sharpest current A-side endpoint target is to display each elementary
Green/corridor endpoint generator as a product of Artin permutation defect
values in fixed factors of `H(pi,Q)`.
Also read `proofs/artin_detector_lift_criterion.md`: if a fixed observer
factor carries live-strand pairs `(m_k,u_k)` and its positive and negative
crossing rows match the active `U x U` Artin detector update, then induction
gives `u_k(beta)=phi(L_k(beta))`.  This reduces the unbounded braid-word part
of the remaining endpoint problem to finite row identities in fixed detector
factors.
Also read `proofs/atom_inner_detector_lift_rows.md`: once atom descent and
totality are established, the atom quotient is rack-like and its inner group
automatically satisfies the detector-lift rows.  Positive rows are just rack
self-distributivity in the form `L_{a*b}=L_a L_b L_a^-1`; negative rows are
formal inverses.  Therefore do not spend the remaining proof effort on the
atom-inner row identity itself.  The open row checks are Green kernel-block,
Schutzenberger, and lower endpoint/unit holonomy factors.
Also read `proofs/green_first_output_defect_criterion.md`: the Green
kernel-block and Schutzenberger row checks are not independent literal Artin
row checks anymore.  A row is determined by the first-output defect
`d_C(a,q)=g(q^a)g(q)^-1`; kernel-block defects are Schutzenberger
pushforwards when no local-only edge-germs occur.  The remaining Green target
is sharpened by `proofs/green_defect_kernel_quotient_detection.md`: quotient
each observer `U_C` by the normal closure `Def_C` of all first-output
defects.  The projected rows in `U_C/Def_C` are exact side-opposite
rack-Artin rows, so detector-lift kills the quotient motion.  The intermediate
Green defect-kernel target is the finite endpoint
`D_C(beta) in V_beta(Def_C)`.  Also read
`proofs/green_defect_potential_coboundary.md`: every elementary defect is a
finite nonabelian coboundary `eta(q^a)eta(q)^-1` in `Def_C`.  This made the
potential principalness check explicit before the balanced gauge refinement.
Also read
`proofs/artin_defect_abelianization_barrier.md`: Artin permutation defect
values always lie in `[Def_C,Def_C]`, so nontrivial abelianized elementary
defects cannot be handled by Artin-defect displays alone.  The remaining proof
must use full recursive-longitude membership, endpoint cancellation, or
detector-lift labels for abelian defect data.  Also read
`proofs/green_defect_abelianization_split.md`: it identifies the finite
abelian target `Def_C/[Def_C,Def_C]` and the residual commutator endpoint.
Also read `proofs/abelian_longitude_image_criterion.md`: for finite abelian
`A`, it computes `V_beta(A)` exactly as the subgroup generated by `a^{m_ij}`
from the abelianized recursive-longitude matrix, so the `AbDef_C` endpoint
has a concrete matrix-subgroup target.
Also read `proofs/green_balanced_defect_gauge_decomposition.md`: it proves
that each raw Green/Schutzenberger first-output defect is an Artin-visible
commutator times a conjugated inverse second-output gauge, so the remaining
Green row burden is terminal gauge holonomy rather than arbitrary defect
holonomy.
Also read `proofs/terminal_gauge_longitudinalization_criterion.md`: it turns
that burden into the standard endpoint certificate target by checking gauge
telescoping and then requiring a fixed-factor longitude expression, subgroup
witness, Artin-defect display, or abelian matrix witness.
Also read `proofs/principal_gauge_extension_detector.md`: it closes the
principal lower endpoint/unit gauge subcase.  If the surviving row has
`(a,r)*(b,s)=(a*b,c(a,b)s)`, the YBE supplies the nonabelian rack-cocycle
identity, `A x U` is a finite rack, and `Inn(A x U)` is a fixed detector.
The remaining structural target is principal-gauge normal form or a
nonprincipal row upgraded to a normalized-law B sequence.
Also read `proofs/transport_state_rackification_detector.md`: it removes the
principal assumption for strand-continuing finite gauge rows.  A row
`((a,r),(b,s))->((a*b,F_{a,b,r}(s)),(a,r))` rackifies on `A x E`, so
`Inn(A x E)` is a fixed detector.  The remaining target is descent
separation: any non-strand-continuing lower motion must be completely visible
in Green kernel-block or Schutzenberger factors.
Also read `proofs/continuation_congruence_descent_gate.md`: it generates the
least admissible congruence from all continuation changes `x~v`.  Equality is
the transport-state case, proper mixed closure contradicts local-minimality,
and universal closure is the remaining corridor whose Green/Schutzenberger
visibility must be proved or converted into a normalized-law B sequence.
Also read `proofs/elementary_continuation_closure.md`: it proves that in a
local-minimal target every single nontrivial continuation seed pair has
universal closure, so the final descent-separation obstruction can be attacked
seed-by-seed.
Also read `proofs/universal_continuation_derivation_certificate.md`: it
records the finite derivation rows for every nontrivial edge in a universal
single-seed continuation closure.  This makes the remaining proof target
derived-edge-level rather than an opaque universal-corridor assertion.
Also read `proofs/continuation_readout_propagation.md`: it proves that an
admissible fixed readout relation containing one representative continuation
seed contains the entire least admissible closure generated by that seed.
Thus derived edges need no separate visibility proof after admissibility and
seed containment are proved.
Also read `proofs/readout_kernel_admissibility.md`: it gives the finite local
criterion for the admissibility input.  Fibrewise fixed detector labels define
a kernel relation, and `readout_kernel_audit(...)` verifies exact transport
through every local table, recording the first failure row if the proposed
labels do not descend.
Also read `proofs/readout_descent_separation_certificate.md`: it combines the
readout-kernel and continuation-seed checks.  The helper
`readout_descent_separation_audit(...)` records surviving continuation seed
rows in the readout quotient; if none survive and the base row is in rack-side
form, the quotient row is strand-continuing and transport-state rackification
applies.
Also read `proofs/readout_kernel_quotient_interval.md`: it constructs the
explicit local interval on readout blocks via
`quotient_interval_by_family(...)` and `readout_kernel_quotient_interval(...)`.
The descent-separation audit now stores this quotient and its continuation
audit when the readout kernel is admissible.
Also read `proofs/product_readout_kernel_assembly.md`: it proves that
tuple-valued products of fixed readout labels have kernel equal to the meet of
the factor kernels, and `product_readout_kernel_audit(...)` records the
factorwise admissibility needed before using one fixed product readout.
Also read `proofs/product_readout_descent_separation.md`: it records the
seed-level consequence of that meet identity.  A tuple-valued product readout
kills a continuation seed only when every factor kills it; the product
survival rows are the union of the factor survival rows.
Also read `proofs/readout_seed_saturation.md`: it computes the least
admissible coarsening forced by one readout factor plus all continuation
seeds.  In a local-minimal interval, a non-killing admissible equality factor
has universal seed-saturation, so any lost information must be routed through
another fixed detector component or through transport-state rackification.
Also read `proofs/local_minimal_seed_saturation_dichotomy.md`: it makes that
local-minimality consequence executable and treats forced universal collapse
as an external-routing obligation, not as faithful residual detection.
Also read `proofs/lost_edge_external_routing.md`: it separates descent
quotient labels from external endpoint labels that route the edges collapsed
by seed-saturation.  Routing labels must not be added back to the descent
quotient product unless one wants the continuation seeds to survive again.
Then read `proofs/routed_lost_edge_endpoint_witness.md`: routed lost edges
are valid for the A route only after they receive product endpoint-longitude
certificates in fixed detector factors.  Missing routed-edge witnesses are
not B evidence unless upgraded to normalized laws.
Also read `proofs/chart_transport_collapse.md`: it proves that finite chart
conjugation does not create new endpoint-longitude obligations, because
`V_beta(G)` is normal and one representative elementary-generator witness
certifies the whole chart-conjugacy orbit.  Then read
`proofs/descent_separation_transport_rack_closure.md`: it is the current
honest final A-route statement.  Transport-rack closure is proved there; the
unproved theorem is descent separation itself.
Also read `proofs/unit_section_product_detector.md`, which combines finitely
many fixed unit-section factors into one direct-product detector group.
62. `proofs/green_holonomy_factorization_gate.md`
63. `proofs/involutive_permutation_detector.md`
64. `proofs/structure_orbit_law_obstruction.md`
65. `proofs/fixed_variety_barrier.md`
66. `proofs/bounded_degree_action_image_limit.md`
Also read `proofs/diagonal_normalized_obstruction.md`, which proves that an
explicit detector-free interval diagonalizes to the normalized-law sequence
required for outcome B.  Audit the companion helpers
`diagonal_product_invisibility_audit(...)` and
`right_stabilization_longitude_audit(...)` for product and stabilization
conventions only; they are not a substitute for proving all finite detector
groups fail.
67. `proofs/affine_f2_audit.md`
68. `proofs/two_colour_fibre2_all_bases_audit.md`
69. `proofs/fibre2_product_branch.md`
70. `proofs/two_colour_fibre3_product_audit.md`
71. `proofs/three_colour_fibre2_product_audit.md`
72. `proofs/sawin_proof_log.docx`
73. `tables/reduction_audit.xlsx`
74. Relevant code in `src/`, `tools/`, and `tests`, especially modules
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
For the current local-ledger interface, require
`closed_local_detector_chain(summaries)` to succeed before using the assembly
wrapper.  It demands one explicit interval-level product group
`closed_detector_product_group` from each closed local summary and reports
open verdicts or delegated detector gaps instead of silently building a rack.

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
Also audit the closed product detector certificates in
`local_master_bottleneck_summary(interval)`.  Coboundary, one-colour
pairwise, identity-base cyclic, and known-total product details should expose
a fixed finite group object, detector order, and sharp rack factor size.
Fibre-size-two affine product details are currently marked as delegated to
`proofs/fibre2_product_branch.md`; do not treat that delegation as a local
`C_2` proof unless you supply the missing all-`n` affine detector argument.
For closed local rows, use `closed_detector_groups` and
`closed_detector_product_group` together with `closed_detector_gaps` on the
summary to check whether the current archive actually provides one finite
group object per interval ready for congruence-chain assembly.
For the remaining bi-free corridor branch, also read
`proofs/bifree_corridor_endpoint_factorization.md`.  It proves only the
assembly implication from factorwise endpoint-longitude expressions to one
fixed product detector `H(pi,Q)`.  Do not count it as proof of the Master Local
Theorem unless the missing endpoint longitudinalization lemma is supplied for
arbitrary local-minimal target intervals.
The executable helpers
`endpoint_longitude_expression_audit(...)` and
`endpoint_product_longitude_expression_audit(...)` are the group-only
certificate layer for that note.  They are useful for checking a proposed
factorwise proof, but they do not themselves construct the missing endpoint
expressions.
Also check the faithful-readout helpers
`endpoint_coordinate_readout_audit(...)` and
`endpoint_residual_readout_audit(...)`: they only verify that identity endpoint
tuples fix the residual coordinates in supplied rows.  They do not replace the
uniform all-`n` construction of those rows.
`endpoint_residual_action_audit(...)` adds braid-data and supplied-row coverage
bookkeeping for one fixed braid word; treat it as an audit of displayed rows,
not as finite-search evidence for arbitrary `n`.
Then audit the Artin-defect refinement in
`proofs/artin_defect_longitudinalization_sieve.md`.  A supplied identity

```text
h_e(beta,z,x)=product_m phi_m(beta(w_m)p_beta(w_m)^-1)^{epsilon_m}
```

inside a fixed detector factor is enough to prove
`h_e(beta,z,x) in V_beta(H_s)`, because each Artin permutation defect lies in
the normal closure of the recursive Artin longitudes.  Use
`artin_permutation_defect_witness_audit(...)`,
`endpoint_artin_defect_audit(...)`, and
`endpoint_product_artin_defect_audit(...)` only as certificate verifiers for
such displays.  The missing local theorem is exactly that these displays
exist for all elementary Green/corridor endpoint generators, uniformly in
`n`.
Also audit the detector-lift version in
`proofs/artin_detector_lift_criterion.md`.  A proposed Green/corridor row may
instead carry live-strand labels `(m,u)` in a fixed group `U`; if the positive
and negative local rows are the active `U x U` Artin detector rows, then
terminal `u`-labels are evaluated recursive longitudes.  Use
`artin_detector_lift_transition_audit(...)` for the finite row check and
`artin_detector_lift_braid_audit(...)` for the braid-recursion convention.
The atom-inner rows are already closed by
`proofs/atom_inner_detector_lift_rows.md`: after atom descent and totality,
the side-opposite rack layer has inner translations satisfying the positive
Artin row, and the negative row is its inverse.  Focus any remaining
detector-lift proof on Green kernel-block, Schutzenberger, and lower
endpoint/unit holonomy rows.
The Green kernel-block and Schutzenberger row checks are now replaced by
`proofs/green_first_output_defect_criterion.md`.  Use
`schutzenberger_first_output_defect_audits(...)` and
`kernel_block_first_output_defect_audits(...)` only to verify the normal-form
algebra.  Then use `proofs/green_defect_kernel_quotient_detection.md` and
`green_defect_kernel_quotient_audit(...)`: after quotienting `U_C` by the
normal closure `Def_C` of all first-output defects, the projected rows are
exact side-opposite rack-Artin rows.  The intermediate theorem-level target is
the transported finite defect-kernel endpoint
`D_C(beta) in V_beta(Def_C)`.  Then use
`proofs/green_defect_potential_coboundary.md` and
`green_defect_kernel_potential_audit(...)`: the elementary defects are finite
coboundaries of a `Def_C`-valued potential, so the exact finite row-level
target is Artin-transport principalness of that potential.  Use
`proofs/artin_defect_abelianization_barrier.md` and
`green_defect_artin_abelianization_barrier_audit(...)` to rule out invalid
Artin-defect-only displays when elementary defects survive in
`Def_C/[Def_C,Def_C]`.  Use `proofs/green_defect_abelianization_split.md`
and `green_defect_abelianization_split_audit(...)` to isolate that finite
abelian target before attacking the commutator endpoint.  Use
`proofs/abelian_longitude_image_criterion.md` and
`abelian_longitude_image_audit(...)` for the exact matrix subgroup
`V_beta(AbDef_C)`.  Use
`proofs/green_balanced_defect_gauge_decomposition.md` and the
`second_output_gauge` row-audit fields to avoid treating raw Green defects as
independent obstructions.  Kernel-block
defects are handled by
`schutzenberger_kernel_defect_pushforward_audits(...)` when no local-only
edge-germs occur.

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
Also use `proofs/unit_continuation_final_obstruction.md` for the final
constant-observer universal-continuation case.  In the case
`Theta^cont=Nabla` and `K^O=Nabla`, nonunit/reset-like continuation factors
cannot be the moving residual obstruction because any branch that contributes
to `delta_{n,z}(beta)` has a permutation composite.  The exact remaining
target is the unit-continuation longitude theorem:
`S_beta in V_beta(U(M_cont))` for the fixed interval-level unit group, or a
normalized-law B sequence from a failure.
Also use `proofs/two_sided_unit_collapse.md`: if every remaining lower
coordinate section is bijective on both sides, the row is locally
nondegenerate and belongs to a closed branch; if it is strand-continuing, it
is already transport-rackified.  The exact surviving shape is mixed-unit
context recovery, audited by `two_sided_unit_collapse_audit(...)`.  Do not
treat a two-sided unit row or a raw nonunit/reset label as final B evidence.
Then use `proofs/mixed_unit_companion_separation.md`: every coordinate-section
kernel collision in a bijective local row is separated by the companion output.
The remaining seed is a companion-shuttle cycle, audited by
`section_kernel_companion_audit(...)`; do not treat an isolated nonunit
section as a counterexample.
Then use `proofs/rank_profile_collapse_mixed_unit.md`: proper nontrivial
section-kernel profiles are Green/Schutzenberger-visible, so a hidden
rank-losing section must be rank one/constant.  The next classification target
is constant-section triangular YBE rows, audited by
`section_rank_profile_collapse_audit(...)`.
Then use `proofs/constant_section_triangular_bundle_partition.md`: a bijective
constant-section triangular row is a finite bundle partition over the constant
map.  Audit it with `triangular_bundle_audit(...)`; the remaining obstruction
is triangular bundle holonomy, not an arbitrary triangular map.
Then use `proofs/triangular_bundle_recovery_inverse.md`: the triangular bundle
inverse recovers the block label and then the within-block companion
coordinate.  Audit it with `triangular_recovery_audit(...)`; a B seed must
move through recovery holonomy, not merely display a nontrivial bundle.
Then use `proofs/constant_column_collapse_triangular.md`: a hidden
non-bijective opposite column in a triangular row forces product/permutation
form, because proper kernels are Green/Schutzenberger-visible and one constant
column forces all opposite columns constant.  Audit it with
`triangular_column_collapse_audit(...)`.  The remaining triangular target is
the Latin-unit triangular longitude theorem for `U_triangle`; a B seed must be
a Latin-unit endpoint miss upgraded to normalized laws.
Then use `proofs/unit_continuation_abelian_kernel_lift.md`: split the final
unit endpoint through `U/[U,U]`.  The abelian projection should be handled by
the abelian longitude matrix criterion, while the residual correction must be
witnessed inside the commutator subgroup.  The code helper
`normal_quotient_longitude_lift_audit(...)` checks the quotient witness,
lifted witness, and kernel witness.
Then use `proofs/unit_continuation_derived_series_reduction.md`: iterate the
abelian-kernel lift through the finite derived series.  Solvable unit groups
reduce to abelian matrix-longitude witnesses in fixed derived quotients; a
nonsolvable case leaves only the stable perfect residual endpoint.
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
Prefer the Artin-defect form when the corridor algebra supplies it: a display
by `beta(w)p_beta(w)^-1` values automatically gives the needed subgroup
witness and is the sharpened target for the remaining bi-free corridor branch.
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
